"""
A simple example of how to use selenium

References:
- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


CHROME_PATH = '/usr/bin/google-chrome'
# CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
CHROMEDRIVER_PATH = '/home/mark/install/selenium/chromedriver.85'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH,
    options=chrome_options,
)
driver.get("https://www.python.org")
print(driver.title)
