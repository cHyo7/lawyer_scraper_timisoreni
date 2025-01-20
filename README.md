# Lawyer Scraper - Timisoreni

This Python script scrapes lawyer contact information (names and phone numbers) from the **Timisoreni** website. The script handles multiple pages of lawyer listings, collects the relevant data, and saves it into an Excel file for further use.

## Features

- Scrapes lawyer names and phone numbers from multiple pages on **https://www.timisoreni.ro/info/avocati**.
- Automatically handles pagination and fetches data from all available pages.
- Saves the scraped data in a neatly formatted Excel file.

## Requirements

To run the script, make sure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

You can install them using `pip`:

```bash
pip install requests beautifulsoup4 pandas openpyxl
