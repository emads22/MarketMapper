import download_stock_data as dsd
import scrape_currency_rate as scr
from constants import ASCII_ART


def main():
    # Display logo or ASCII art
    print("\n\n\n\n", ASCII_ART, "\n\n")

    # Display the menu options to the user
    print("\n>> Select an option:\n")

    # Enumerate through the script options and print them
    for idx, item in enumerate(["download_stock_data.py", "scrape_currency_rate.py"], start=1):
        print(f"    {idx}. Run `{item}`")

    # Prompt the user to enter their choice
    choice = input("\n\n>> Enter the number of your choice: ")

    # Loop until the user enters a valid choice (1 or 2)
    while choice not in ['1', '2']:
        print("\n\n--- Invalid choice. Please select 1 or 2. --- \n")
        choice = input("\n\n>> Enter the number of your choice: ")

    # Execute the corresponding script based on the user's choice
    if choice == '1':
        dsd.main()
    elif choice == '2':
        scr.main()


if __name__ == "__main__":
    main()
