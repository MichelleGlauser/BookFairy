#!/usr/bin/env python3

"""
BookFairy CLI (standalone): Fetch SFPL availability candidate and Goodreads rating for a list of books.

Inputs:
  - --file: path to a text file with lines formatted as "Title, Author"
  - --text: raw text with one "Title, Author" per line
  - --gspread: Google Sheets title, key, or full URL (uses browser OAuth via gspread.oauth)
      Optional: --worksheet name (defaults to "To Read" if present, otherwise the first sheet)

Utilities:
  - --list-locations: print allowed SFPL location codes and exit

Output:
  Prints each matched title with its Goodreads rating (or N/A if not found). Use --format json for JSON.

Notes:
  - Google Sheets auth uses gspread's OAuth flow. You'll need credentials.json available
    (see https://docs.gspread.org/en/latest/oauth2.html#for-end-users) the first time; a token.json
    will be stored locally for subsequent runs.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from typing import Iterable, List, Optional, Sequence, Tuple
from thefuzz import fuzz

# Resolve repo root so we can import shared modules
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = SCRIPT_DIR  # script resides at repo root
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# Import shared core modules from bfcore and fail gracefully if missing
try:
    from bfcore.library import get_library_details, LOCATION_MAP
    from bfcore.goodreads import find_gr_rating
except Exception as e:
    print("Error importing bfcore modules. Ensure you're running from the repo root and that 'bfcore' exists.")
    print(f"Import error: {e}")
    sys.exit(2)


def print_locations() -> None:
    print("Allowed SFPL locations (code: name):")
    for code in sorted(LOCATION_MAP, key=lambda k: int(k)):
        print(f"  {code}: {LOCATION_MAP[code]}")


def parse_book_line(line: str) -> Optional[Tuple[str, str]]:
    """Parse a single line into (title, author) using the last comma as separator."""
    if not line:
        return None
    s = line.strip()
    if not s or "," not in s:
        return None
    title, author = s.rsplit(",", 1)
    title = title.strip()
    author = author.strip()
    if not title or not author:
        return None
    return title, author


def parse_books_from_lines(lines: Iterable[str]) -> List[Tuple[str, str]]:
    books: List[Tuple[str, str]] = []
    for ln in lines:
        parsed = parse_book_line(ln)
        if parsed:
            books.append(parsed)
    return books


def load_books_from_file(path: str) -> List[Tuple[str, str]]:
    with open(path, "r", encoding="utf-8") as f:
        return parse_books_from_lines(f.readlines())


def load_books_from_text(text: str) -> List[Tuple[str, str]]:
    return parse_books_from_lines(text.splitlines())


def extract_spreadsheet_key(gsheet: str) -> Optional[str]:
    """If a Google Sheets URL is given, extract the spreadsheet key. Returns None if not a URL."""
    m = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", gsheet)
    return m.group(1) if m else None


def load_books_from_gspread(spreadsheet: str, worksheet: Optional[str]) -> List[Tuple[str, str]]:
    """Load books from Google Sheets using gspread's OAuth browser flow."""
    try:
        import gspread
    except Exception as e:
        print("gspread is required for --gspread input. Install with 'pip install gspread google-auth google-auth-oauthlib'.")
        raise

    gc = gspread.oauth()  # browser OAuth flow; requires credentials.json on first run

    key = extract_spreadsheet_key(spreadsheet)
    if key:
        sh = gc.open_by_key(key)
    else:
        sh = gc.open(spreadsheet)

    if worksheet:
        ws = sh.worksheet(worksheet)
    else:
        try:
            ws = sh.worksheet("To Read")
        except gspread.exceptions.WorksheetNotFound:
            ws = sh.get_worksheet(0)

    rows: List[List[str]] = ws.get_all_values()
    books: List[Tuple[str, str]] = []
    for r in rows:
        if not r:
            continue
        cells = [c.strip() for c in r if isinstance(c, str)]
        if not cells:
            continue
        if len(cells) >= 2 and cells[0] and cells[1]:
            books.append((cells[0], cells[1]))
        elif len(cells) >= 1:
            parsed = parse_book_line(cells[0])
            if parsed:
                books.append(parsed)
    return books


def fetch_book_info(title: str, author: str, lib_location: str, delay: float = 0.0) -> Optional[Tuple[str, str]]:
    """Get (matched_title, rating_str) for a given book/author.

    Returns None if library match cannot be found.
    rating_str is either a stringified float (e.g., "4.2") or "N/A".
    """
    details = get_library_details(title, author, lib_location)
    if not details:
        return None
    matched_title = details[0]
    rating = find_gr_rating(title, author)
    rating_str = f"{rating:.1f}" if isinstance(rating, (int, float)) else "N/A"
    if delay > 0:
        time.sleep(delay)
    return matched_title, rating_str


def validate_input_methods(args: argparse.Namespace) -> None:
    if args.list_locations:
        return  # allow no input method when listing
    provided = [v for v in [args.file_path, args.raw_text, args.gspread_ref] if v]
    if len(provided) == 0:
        raise SystemExit("Error: one of --file, --text, or --gspread is required.")
    if len(provided) > 1:
        raise SystemExit("Error: please provide only one of --file, --text, or --gspread.")


# --------------- Interactive mode helpers -----------------
def _input(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        return ""


def fuzzy_resolve_location(user_input: str) -> Optional[Tuple[str, str]]:
    """Return (code, name) best matching user_input using fuzzy matching over codes and names."""
    s = (user_input or "").strip()
    if not s:
        return None
    # Exact code match
    if s in LOCATION_MAP:
        return s, LOCATION_MAP[s]
    # Try case-insensitive name exact
    for code, name in LOCATION_MAP.items():
        if s.lower() == name.lower():
            return code, name
    # Fuzzy match on code or name
    best: Tuple[int, Tuple[str, str]] = (-1, ("", ""))
    for code, name in LOCATION_MAP.items():
        score = max(
            fuzz.token_set_ratio(s, code),
            fuzz.token_set_ratio(s, name),
        )
        if score > best[0]:
            best = (score, (code, name))
    return best[1] if best[0] >= 60 else None  # require a reasonable threshold


def print_locations_table() -> None:
    print("Allowed SFPL locations (code: name):")
    for code in sorted(LOCATION_MAP, key=lambda k: int(k)):
        print(f"  {code}: {LOCATION_MAP[code]}")


def interactive_wizard() -> argparse.Namespace:
    print("BookFairy interactive mode — no args provided. Let's set things up.")
    # Step 1: choose input method
    method = None
    while method is None:
        resp = _input("Input method? [F]ile / [T]ext / [G]oogle Sheet: ").strip().lower()
        if resp in ("f", "file"):
            method = "file"
        elif resp in ("t", "text"):
            method = "text"
        elif resp in ("g", "gs", "gspread", "sheet", "google"):
            method = "gspread"
        else:
            print("Sorry, please enter F, T, or G.")

    file_path = raw_text = gspread_ref = worksheet = None
    if method == "file":
        while True:
            p = _input("Path to text file with 'Title, Author' per line: ").strip()
            if not p:
                print("Please provide a file path or press Ctrl+C to abort.")
                continue
            if not os.path.exists(p):
                print(f"File not found: {p}")
                continue
            file_path = p
            break
    elif method == "text":
        while True:
            t = _input("Paste lines (Title, Author). End with an empty line:\n").rstrip("\n")
            # Allow multi-line: keep reading until blank line
            lines = [t]
            while True:
                nxt = _input("")
                if nxt.strip() == "":
                    break
                lines.append(nxt)
            joined = "\n".join(lines).strip()
            if not joined:
                print("No text received. Please try again.")
                continue
            raw_text = joined
            break
    else:  # gspread
        while True:
            g = _input("Google Sheet title, key, or full URL: ").strip()
            if not g:
                print("Please provide a Google Sheet reference.")
                continue
            gspread_ref = g
            ws = _input("Worksheet name (optional, default 'To Read' or first sheet): ").strip()
            worksheet = ws or None
            break

    # Step 2: library location (code or name), fuzzy match allowed
    lib_code = None
    lib_name = None
    while lib_code is None:
        s = _input("Library location (code or name, type 'list' to see options) [default MAIN]: ").strip()
        if not s:
            lib_code, lib_name = "3", LOCATION_MAP["3"]
            break
        if s.lower() in ("list", "ls", "l"):
            print_locations_table()
            continue
        match = fuzzy_resolve_location(s)
        if not match:
            print("Couldn't resolve that to a branch. Try again or type 'list'.")
            continue
        lib_code, lib_name = match
        # Confirm
        conf = _input(f"Use '{lib_name}' (code {lib_code})? [Y/n]: ").strip().lower()
        if conf in ("n", "no"):
            lib_code = None
        else:
            break

    # No delay prompt in interactive mode; default to 0.0
    delay = 0.0

    # Step 4: output format
    fmt = None
    while fmt is None:
        f = _input("Output format? [T]ext / [J]SON (default: Text): ").strip().lower()
        if f in ("", "t", "text"):
            fmt = "text"
        elif f in ("j", "json"):
            fmt = "json"
        else:
            print("Please enter T or J (or press Enter for Text).")

    # Review & edit
    def show_summary():
        print("\nReview your choices:")
        print(f"1) Input method: {method}")
        if method == "file":
            print(f"2) File path: {file_path}")
        elif method == "text":
            preview = (raw_text or "").splitlines()[:2]
            prev_str = " | ".join(preview) + (" ..." if len((raw_text or "").splitlines()) > 2 else "")
            print(f"2) Raw text (preview): {prev_str}")
        else:
            print(f"2) Google Sheet: {gspread_ref}  Worksheet: {worksheet or '(auto)'}")
        print(f"3) Library: {lib_name} (code {lib_code})")
        print(f"4) Format: {fmt}")

    while True:
        show_summary()
        choice = _input("Edit which? [1-4] or press Enter to continue: ").strip()
        if choice == "":
            break
        if choice not in {"1", "2", "3", "4"}:
            print("Please enter a number 1-4 or press Enter.")
            continue
        c = int(choice)
        if c == 1:
            # Re-pick method entirely
            method = None
            while method is None:
                resp = _input("Input method? [F]ile / [T]ext / [G]oogle Sheet: ").strip().lower()
                if resp in ("f", "file"):
                    method = "file"
                elif resp in ("t", "text"):
                    method = "text"
                elif resp in ("g", "gs", "gspread", "sheet", "google"):
                    method = "gspread"
                else:
                    print("Sorry, please enter F, T, or G.")
            file_path = raw_text = gspread_ref = worksheet = None
            # Recollect method-specific fields quickly
            if method == "file":
                while True:
                    p = _input("Path to text file: ").strip()
                    if not p:
                        print("Please provide a file path.")
                        continue
                    if not os.path.exists(p):
                        print(f"File not found: {p}")
                        continue
                    file_path = p
                    break
            elif method == "text":
                print("Enter new text. End with a blank line.")
                lines = []
                while True:
                    nxt = _input("")
                    if nxt.strip() == "":
                        break
                    lines.append(nxt)
                raw_text = "\n".join(lines).strip()
                if not raw_text:
                    print("No text entered; reverting to previous.")
            else:
                gspread_ref = _input("Google Sheet title/key/URL: ").strip() or gspread_ref
                ws2 = _input("Worksheet (optional): ").strip()
                worksheet = ws2 or worksheet
        elif c == 2:
            if method == "file":
                p = _input("New file path: ").strip()
                if p and os.path.exists(p):
                    file_path = p
                else:
                    print("Invalid path; keeping previous.")
            elif method == "text":
                print("Enter new text. End with a blank line.")
                lines = []
                while True:
                    nxt = _input("")
                    if nxt.strip() == "":
                        break
                    lines.append(nxt)
                new_text = "\n".join(lines).strip()
                if new_text:
                    raw_text = new_text
                else:
                    print("No text entered; keeping previous.")
            else:
                g = _input("New Google Sheet title/key/URL (leave blank to keep): ").strip()
                if g:
                    gspread_ref = g
                ws2 = _input("New worksheet (blank to keep): ").strip()
                if ws2:
                    worksheet = ws2
        elif c == 3:
            while True:
                s = _input("Library location (code or name, 'list' to see): ").strip()
                if s.lower() in ("list", "ls", "l"):
                    print_locations_table()
                    continue
                match = fuzzy_resolve_location(s)
                if not match:
                    print("Couldn't resolve; try again.")
                    continue
                lib_code, lib_name = match
                break
        elif c == 4:
            f = _input("Format [text/json]: ").strip().lower()
            if f in ("text", "json"):
                fmt = f
            else:
                print("Invalid; keeping previous.")

    # Build an argparse-like namespace to reuse downstream logic
    ns = argparse.Namespace(
        file_path=file_path,
        raw_text=raw_text,
        gspread_ref=gspread_ref,
        worksheet=worksheet,
        lib_location=lib_code,
        delay=delay,
        format=fmt,
        list_locations=False,
    )
    return ns


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="BookFairy CLI: fetch SFPL + Goodreads data")
    parser.add_argument("--file", dest="file_path", help="Path to text file with 'Title, Author' per line")
    parser.add_argument("--text", dest="raw_text", help="Raw text with 'Title, Author' per line")
    parser.add_argument("--gspread", dest="gspread_ref", help="Google Sheet title, key, or URL (OAuth in browser)")

    parser.add_argument("--worksheet", help="Worksheet name for Google Sheet (default: 'To Read' if exists)")
    parser.add_argument("--lib-location", default="3", help="SFPL location code (default: '3' MAIN; use --list-locations)")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay (seconds) between items to be kind to Goodreads")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--list-locations", action="store_true", help="Print allowed SFPL location codes and exit")

    # If no args provided, enter interactive mode
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) == 0:
        args = interactive_wizard()
    else:
        args = parser.parse_args(argv)
        validate_input_methods(args)

    if args.list_locations:
        print_locations()
        return 0

    # Gather books
    books: List[Tuple[str, str]] = []
    try:
        if args.file_path:
            if not os.path.exists(args.file_path):
                print(f"File not found: {args.file_path}")
                return 2
            books = load_books_from_file(args.file_path)
        elif args.raw_text:
            books = load_books_from_text(args.raw_text)
        elif args.gspread_ref:
            books = load_books_from_gspread(args.gspread_ref, args.worksheet)
    except Exception as e:
        print(f"Error loading input: {e}")
        return 2

    if not books:
        print("No valid books found. Expected lines like: 'Title, Author'.")
        return 1

    # Process and collect results
    results: List[Tuple[str, str, str]] = []  # (input_title, matched_title, rating_str)
    for (title, author) in books:
        try:
            info = fetch_book_info(title, author, args.lib_location, delay=args.delay)
        except Exception as e:
            print(f"Error fetching data for '{title}' by '{author}': {e}")
            info = None
        if info is None:
            continue
        matched_title, rating_str = info
        results.append((title, matched_title, rating_str))

    if not results:
        print("No matches found from SFPL for the provided books.")
        return 0

    if args.format == "json":
        import json
        payload = [
            {"input_title": it, "matched_title": mt, "rating": r}
            for (it, mt, r) in results
        ]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for (input_title, matched_title, rating_str) in results:
            if input_title != matched_title:
                print(f"{matched_title} (from '{input_title}') — Goodreads: {rating_str}")
            else:
                print(f"{matched_title} — Goodreads: {rating_str}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
