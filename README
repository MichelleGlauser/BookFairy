This project is my way of helping myself find a book to read without having to do a lot of back-and-forth with the San Francisco Public Library website. 

There is a basic CLI for local use, as well as a Django web app


Installation:
---------
If you're editing the project use `pip install -e`

Create and activate a virtual environment, then install the project:

```bash
# from the repo root
python3 -m venv .venv
source .venv/bin/activate
```

For CLI only:
```bash
pip install .
```

For CLI with Google Sheets support:
```bash
pip install '.[sheets]'
```

For the web app (in progress):
```bash
pip install '.[web]'
```

Google Sheets OAuth (optional)
-------------------------------
For `--gspread`, you need end-user OAuth set up per gspread docs:
- https://docs.gspread.org/en/latest/oauth2.html#for-end-users

Place a `credentials.json` in the repo root (or follow gspread’s search paths). On first run, a browser window will prompt you to authorize and `token.json` will be saved for reuse.

Usage
-----

Run the CLI interactively:

```bash
bookfairy
```

Or use CLI args (disables interactive mode):

```bash
# Print allowed library locations
bookfairy --list-locations

# From a text file with lines: "Title, Author"
bookfairy --file /path/to/books.txt --lib-location 3

# From raw text (one per line)
bookfairy --text "The Night Circus, Erin Morgenstern
Dune, Frank Herbert" --lib-location 3

# From Google Sheets by URL/key/title
bookfairy --gspread "https://docs.google.com/spreadsheets/d/YOUR_KEY/edit#gid=0" --worksheet "To Read" --lib-location 3

# JSON output and a gentle delay between items
bookfairy --file books.txt --format json --delay 0.8
```

Notes
-----
- `--lib-location` is the SFPL branch code (default `3` = MAIN). Use `--list-locations` to see all.
- After installing (pip install . or -e .), you can run the `bookfairy` command from any directory.
- If running directly from source without installing, either:
	- run `python3 /full/path/to/bookfairy_cli.py` from anywhere, or
	- `cd` to the repo root and run `python3 bookfairy_cli.py`.
- Input format: either two columns in a sheet (Title | Author) or a single column / text line like "Title, Author". The parser splits on the last comma so titles can contain commas.

Troubleshooting
---------------
- ImportError: Ensure you are in the repo root and `bfcore/` exists next to `bookfairy_cli.py`.
- Goodreads errors or slow responses: Use `--delay` (e.g., `0.8s`) to be polite and reduce risk of throttling.
- No results: SFPL had no match for the given book at that branch/location.