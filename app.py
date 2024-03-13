import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # Corrected typo
chrome_options.add_argument('--headless')

# Separate ChromeDriverManager() and chrome_options when passing to Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://nvchad.com/'

driver.get(url)
time.sleep(5)

driver.save_screenshot("./screenshots/insight_page.png")

driver.quit()
