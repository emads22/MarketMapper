from pathlib import Path


# Define the directory where stock data will be stored
STOCK_DATA_DIR = Path("./assets") / "stock_data"

# Define the base URL for Yahoo Finance API
YAHOO_FINANCE_API_ENDPOINT = "https://query1.finance.yahoo.com/"

# Define custom headers to mimic a web browser
# We use this to set the User-Agent header, which identifies the browser and operating system
# This helps in making web requests appear more like they're coming from a real user's browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}


# Define the base URL for x-rates website
X_RATES_ENDPOINT = "https://www.x-rates.com/calculator/"
