# URL Metadata Scraper

A terminal tool that fetches and displays metadata from any given URL, including page title, meta description, and Open Graph tags.

## Features

- Extracts page `<title>`
- Extracts meta description
- Extracts Open Graph metadata (`og:title`, `og:description`)
- Handles redirects and reports final URL
- Robust error handling for invalid URLs, timeouts, and connection issues
- Auto-prepends `https://` if no scheme is provided

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

## How to Run

```bash
python scraper.py
```

## Example Output

```
--- URL Metadata Scraper ---

Enter a website URL: github.com

Fetching: https://github.com

==================================================
          URL METADATA
==================================================
  Title       : GitHub: Let's build from here
  Description : GitHub is where over 100 million developers shape the future of software.
--------------------------------------------------
  Open Graph Metadata:
  og:title       : GitHub: Let's build from here
  og:description : GitHub is where over 100 million developers shape the future of software.
==================================================
```