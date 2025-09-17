# BookFairy Standalone CLI

Fetch SFPL availability candidate and Goodreads rating for a list of books, without running Django.

## What this is

A single-command tool that leverages the existing logic in the repo (`bookapp/library.py` and `bookapp/goodreads.py`). It can read input from a text file, raw text, or a Google Sheet via browser-based OAuth.

## Requirements

- Python 3.8+
- pip

Install the standalone dependencies (separate from the Django app):

```bash
cd standalone
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Note: The CLI imports code from `../bookapp`, so run it from the repo with that folder present (i.e., don't copy this folder elsewhere without also copying the `bookapp` folder).

## Google Sheets OAuth (optional)

For `--gspread`, you need end-user OAuth set up per gspread docs:
- https://docs.gspread.org/en/latest/oauth2.html#for-end-users

Place a `credentials.json` in the current directory (or follow gspread’s search paths). On first run, a browser window will prompt you to authorize and `token.json` will be saved for reuse.

## Usage

Run the CLI:

```bash
# Print allowed library locations
python bookfairy_cli.py --list-locations

# From a text file with lines: "Title, Author"
python bookfairy_cli.py --file /path/to/books.txt --lib-location 3

# From raw text (one per line)
python bookfairy_cli.py --text "The Night Circus, Erin Morgenstern
Dune, Frank Herbert" --lib-location 3

# From Google Sheets by URL/key/title
python bookfairy_cli.py --gspread "https://docs.google.com/spreadsheets/d/YOUR_KEY/edit#gid=0" --worksheet "To Read" --lib-location 3

# JSON output and a gentle delay between items
python bookfairy_cli.py --file books.txt --format json --delay 0.8
```

- `--lib-location` is the SFPL branch code (default `3` = MAIN). Use `--list-locations` to see all.
- Input format: either two columns in a sheet (Title | Author) or a single column / text line like "Title, Author". The parser splits on the last comma so titles can contain commas.

## Troubleshooting

- ImportError: Ensure you are in the repo and `bookapp/` exists next to `standalone/`.
- Goodreads errors or slow responses: Use `--delay` (e.g., `0.8s`) to be polite and reduce risk of throttling.
- No results: It means SFPL had no match for the given book at that branch/location.

## Notes

- This CLI prints only the matched title and Goodreads rating (or `N/A`). If you want more fields (e.g., author, branch name), we can extend the script to include them.
