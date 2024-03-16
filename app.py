import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

# Initialize Chrome WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://dishatest.neophyte.ai/'

driver.get(url)
driver.maximize_window()
time.sleep(10)

# Find the phone number input field by XPath
phone_box = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[1]/input")

# Simulate entering the phone number into the input field
phone_number = "YourPhoneNumberHere"  # Replace with your phone number
print("Got the user login box, entering the phone number")
phone_box.send_keys(phone_number)
time.sleep(3)

# Save a screenshot of the page
driver.save_screenshot("./screenshots/insight_page.png")
time.sleep(2)

# Quit the browser session
driver.quit()
