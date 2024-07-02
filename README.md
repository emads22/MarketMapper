# MarketMapper

## Overview
MarketMapper is a Python-based tool consisting of two scripts: one for downloading historical stock data from [Yahoo Finance](https://finance.yahoo.com/) using Selenium and another for scraping currency conversion rates from [x-rates](https://www.x-rates.com/calculator/) website using BeautifulSoup. The stock data downloader allows users to specify a stock ticker symbol along with start and end dates to download historical stock data in CSV format. The currency converter prompts users to input currency symbols for conversion and then fetches the current conversion rate between the specified currencies.

## Features
- **Stock Data Downloader**: Downloads historical stock data from Yahoo Finance API using Selenium.
- **Currency Converter**: Scrapes currency conversion rates from x-rates website using BeautifulSoup.

## Technologies Used
- **Selenium**: Web automation tool used for interacting with `Yahoo Finance` website.
- **BeautifulSoup**: Python library for parsing HTML and extracting data from `x-rates` website.
- **requests**: Python library for making HTTP requests, used for fetching data from `x-rates` website.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `STOCK_DATA_DIR`, `YAHOO_FINANCE_API_ENDPOINT`, and `X_RATES_ENDPOINT` in `constants.py`.
5. Run the script using `python download_stock_data.py` for stock data downloader or `python scrape_currency_rate.py` for currency converter.

## Usage
1. Run the stock data downloader script using `python download_stock_data.py`.
   - You will be prompted to enter the stock `ticker symbol`, `start date`, and `end date`.
2. Run the currency converter script using `python scrape_currency_rate.py`.
   - You will be prompted to enter the currency symbols you want to convert from and to.
3. Follow the instructions provided by each script to complete the respective tasks.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.