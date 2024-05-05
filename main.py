from selenium.webdriver.common.by import By
import time
from driver import chrome_web_driver
from dotenv import load_dotenv
from config import URL


# Load environment variables from .env file
load_dotenv()


def main():

    chrome = chrome_web_driver(url=URL)
    
    element_by_xpath = chrome.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    element_by_selector = chrome.find_element(
        by=By.CSS_SELECTOR, value="h1.animated.fadeIn.mb-4")

    print(f"\n- Scraping element usin xpath:\n\n  {element_by_xpath.text}\n")
    print(
        f"\n- Scraping element usin css selector:\n\n  {element_by_selector.text}\n")

    time.sleep(3)
    # Close the web driver session
    chrome.quit()


if __name__ == '__main__':
    main()
