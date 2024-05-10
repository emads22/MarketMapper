import requests
from datetime import datetime
import time
from constants import STOCK_DATA_DIR, YAHOO_FINANCE_API_ENDPOINT, HEADERS


# Ensure that the stock data directory exists, creating it if necessary
STOCK_DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_user_inputs():
    """
    Prompt the user to enter stock ticker symbol, start date, and end date.

    Returns:
        tuple: A tuple containing the user inputs (ticker symbol, start date, end date).
    """
    while True:
        # Prompt user for the stock ticker symbol
        ticker = input("\n- Please enter the stock ticker symbol: ").upper()

        # Check if the input is not empty or only whitespace
        if ticker.strip():
            break
        else:
            # Display error message if ticker symbol is empty
            print("\n--- Ticker symbol cannot be empty. Please try again. ---\n")

    while True:
        # Prompt user for the start date
        start_date = input(
            "- Please enter the start date in dd/mm/yyyy format: ")

        # Validate the format of the start date
        if validate_date_format(start_date):
            break
        else:
            # Display error message if start date format is invalid
            print(
                "\n--- Invalid date format. Please enter the date in dd/mm/yyyy format. ---\n")

    while True:
        # Prompt user for the end date
        end_date = input('- Please enter the end date in dd/mm/yyyy format: ')

        # Validate the format of the end date
        if validate_date_format(end_date):
            break
        else:
            # Display error message if end date format is invalid
            print(
                "\n--- Invalid date format. Please enter the date in dd/mm/yyyy format. ---\n")

    return ticker, start_date, end_date


def validate_date_format(date_str):
    """
    Validate the format of a date string.

    Args:
        date_str (str): The date string to validate.

    Returns:
        bool: True if the date string has a valid format, False otherwise.
    """
    try:
        # Attempt to parse the date string
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        # If parsing fails, return False
        return False


def convert_dates_to_epoch(start_date, end_date):
    """
    Convert start and end dates from string format to epoch timestamps.
    The Yahoo Finance API requires dates to be provided in epoch format.

    Args:
        start_date (str): The start date in dd/mm/yyyy format.
        end_date (str): The end date in dd/mm/yyyy format.

    Returns:
        tuple: A tuple containing the start and end epoch timestamps.

    Raises:
        ValueError: If conversion fails.
    """
    try:
        # Convert start date and end date strings to datetime objects
        start_datetime = datetime.strptime(start_date, "%d/%m/%Y")
        end_datetime = datetime.strptime(end_date, "%d/%m/%Y")

        # Convert start datetime and end datetime to epoch timestamps using time.mktime()
        start_epoch = int(time.mktime(start_datetime.timetuple()))
        end_epoch = int(time.mktime(end_datetime.timetuple()))

        # Return the start and end epoch timestamps
        return start_epoch, end_epoch

    except Exception as e:
        # raise a ValueError with an appropriate error message
        raise ValueError(f"\n-- An unexpected error occurred: {e}\n\n")


def download_stock_data(ticker_symbol, start_epoch, end_epoch):
    """
    Download stock data from Yahoo Finance and save it to a CSV file.

    Args:
        ticker_symbol (str): The ticker symbol of the stock.
        start_epoch (int): The start date in epoch format.
        end_epoch (int): The end date in epoch format.

    Raises:
        requests.exceptions.RequestException: If a request-related error occurs.
        Exception: If any other unexpected error occurs.
    """
    try:
        # Construct the URL for the Yahoo Finance API request
        url = f"{YAHOO_FINANCE_API_ENDPOINT}v7/finance/download/{ticker_symbol}?period1={
            start_epoch}&period2={end_epoch}&interval=1d&events=history&includeAdjustedClose=true"

        # Define custom headers to mimic a web browser
        headers = HEADERS
        # Attempt to make the request to the Yahoo Finance API
        response = requests.get(url, headers=headers)
        # Check for HTTP errors and raise an exception if any occur
        response.raise_for_status()

        # If the request is successful, proceed with file handling
        stock_data = response.content
        # Save the stock data to a CSV file
        # 'wb' mode is used because it covers both binary and non-binary files, ensuring data integrity and versatile file handling.
        with open(STOCK_DATA_DIR / f'{ticker_symbol}_stock_data.csv', 'wb') as file:
            file.write(stock_data)

    except requests.exceptions.RequestException as e:
        # If a request-related error occurs, raise it
        raise requests.exceptions.RequestException(
            f"\n-- Request error occurred: {e}\n\n")

    except Exception as e:
        # If any other unexpected error occurs, raise it with an appropriate error message
        raise Exception(f"\n-- An unexpected error occurred: {e}\n\n")


def main():
    """
    Main function for downloading stock data.

    Prompts the user for input, converts dates to epoch format,
    downloads stock data, and displays success or error messages.

    """
    try:
        # Get user inputs
        ticker_symbol, start_date, end_date = get_user_inputs()
        # Convert dates to epoch
        start_epoch, end_epoch = convert_dates_to_epoch(start_date, end_date)
        # Download stock data
        download_stock_data(ticker_symbol, start_epoch, end_epoch)
        # Display success message
        print("\n--- Stock data downloaded successfully! ---\n")

    except Exception as e:
        # Handle any unexpected errors
        print("\n--- An unexpected error occurred. Please try again later. ---\n")
        # Print error details for debugging
        print(f"-- Error details: {e}\n\n")


if __name__ == "__main__":
    main()
