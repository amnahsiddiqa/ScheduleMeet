import pandas as pd
import requests
import io

def fetch_google_sheet_csv(url, sheet_name=None):
    """Fetch CSV data from a specific sheet in a Google Sheet."""
    if sheet_name:
        sheet_url = f"{url}&sheet={sheet_name}"
    else:
        sheet_url = url
    response = requests.get(sheet_url)
    response.raise_for_status()
    return pd.read_csv(io.StringIO(response.text))

def update_markdown(df, filename="README.md"):
    """Convert DataFrame to Markdown and update README.md."""
    with open(filename, 'w') as f:
        f.write("# 2025\n\n")
        f.write(df.to_markdown(index=False))
    print("README.md has been updated.")

if __name__ == "__main__":
    #actual copy link of google sheet would look like thuis : https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/edit?usp=sharing
    # Use the CSV export link for your Google Sheet
    #Solution: Update the URL to include the /export?format=csv parameter:
    CSV_URL = "https://docs.google.com/spreadsheets/d/1cGfIostiPJAxmo_zINnHGHSthbUZ8x9R90-C4oZvTt0/edit?usp=sharing/export?format=csv"
    df = fetch_google_sheet_csv(CSV_URL, sheet_name='Sheet1')

    update_markdown(df)
