import requests
from bs4 import BeautifulSoup
from constants import X_RATES_ENDPOINT, HEADERS


def get_user_inputs():
    """
    Prompt the user for the currency symbols to convert from and to.

    Returns:
        tuple: A tuple containing the currency symbols (from_currency, to_currency).
    """
    while True:
        # Prompt user for the currency symbol to convert from
        from_currency = input(
            "\n- Enter the currency symbol you want to convert from: ").upper()

        # Check if the input is not empty or only whitespace
        if from_currency.strip():
            break
        else:
            print("\n--- Currency symbol cannot be empty. Please try again. ---\n")

    while True:
        # Prompt user for the currency symbol to convert to
        to_currency = input(
            "\n- Enter the currency symbol you want to convert to: ").upper()

        # Check if the input is not empty or only whitespace
        if to_currency.strip():
            break
        else:
            print("\n--- Currency symbol cannot be empty. Please try again. ---\n")

    return from_currency, to_currency


def get_currency_rate(from_currency, to_currency):
    """
    Get the currency rate for the conversion.

    Args:
        from_currency (str): The currency symbol to convert from.
        to_currency (str): The currency symbol to convert to.

    Returns:
        float: The currency rate.
    """
    try:
        # Construct the URL for the currency conversion API
        url = f'{X_RATES_ENDPOINT}?from={
            from_currency}&to={to_currency}&amount=1'
        # Define headers for the HTTP request
        headers = HEADERS

        # Send HTTP GET request to the API
        response = requests.get(url, headers=headers)
        # Check if the response is successful
        response.raise_for_status()

        # Extract the HTML content from the response
        html_source = response.text
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')

        # Select the currency rate element from the parsed HTML
        rate_element = soup.select_one(
            "#content > div:nth-child(1) > div > div:nth-child(1) > div > div > span.ccOutputRslt")

        # Check if the currency rate element is found
        if rate_element is None:
            raise Exception("\n-- Currency rate element not found --\n\n")

        # Get the text content of the currency rate element
        rate = rate_element.get_text()
        # Clean the extracted rate and convert it to float
        cleaned_rate = rate.strip()[:-4]

        return float(cleaned_rate)

    except requests.RequestException as e:
        # Handle errors related to HTTP request
        raise Exception(f"\n-- Error during HTTP request: {e}\n\n")

    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"\n-- Error occurred: {e}\n\n")


def main():
    try:
        # Get user inputs
        from_currency, to_currency = get_user_inputs()
        # Get the currency rate
        this_rate = get_currency_rate(from_currency, to_currency)

        # Display the currency conversion result
        print(
            f"\n\n--- 1 {from_currency}  equals  {this_rate} {to_currency} ---\n\n")

    except Exception as e:
        # Handle other unexpected errors
        print("\n--- An unexpected error occurred. Please try again later. ---")
        print(f"Error details: {e}\n\n")


if __name__ == "__main__":
    main()
