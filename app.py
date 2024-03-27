import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument("window-size=1920,1080")

# Initialize Chrome WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://dishatest.neophyte.ai/'

driver.get(url)
driver.maximize_window()
time.sleep(10)

# Find the phone number input field by XPath
phone_box = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[1]/input")

# Simulate entering the phone number into the input field
phone_number = "5039931677"
print("Got the user login box, entering the phone number")
phone_box.send_keys(phone_number)
time.sleep(3)

submit_otp = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/button")
submit_otp.click()
time.sleep(10)

box_one = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[1]")
box_one.send_keys("0")
time.sleep(2)

box_second = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[2]")
box_second.send_keys("3")
time.sleep(2)

box_third = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[3]")
box_third.send_keys("0")
time.sleep(2)

box_fourth = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[4]")
box_fourth.send_keys("3")
time.sleep(2)

box_fifth = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[5]")
box_fifth.send_keys("7")
time.sleep(2)

box_sixth = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[6]")
box_sixth.send_keys("6")
time.sleep(2)

submitotp_btn = driver.find_element("xpath","/html/body/div[1]/div/div/div/div/div/div[2]/form/div[3]/button")
submitotp_btn.click()
time.sleep(10)

print("Logged in successfully, taking the screenshot of the insight page")
driver.save_screenshot("./screenshots/insight_page.png")
time.sleep(2)

upkeep_score_element=driver.find_element("xpath","/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div")  
upkeep_score_element.screenshot("./screenshots/upkeep_score_element.png")
print("Took the screenshot of the upkeep score graph")
time.sleep(2)

vm_score=driver.find_element("xpath","/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div")
vm_score.screenshot("./screenshots/vm_score.png")
print("Took the screenshot of the VM score graph")
time.sleep(2)

pop_score=driver.find_element("xpath","/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[3]/div")
pop_score.screenshot("./screenshots/pop_score.png")
print("Took the screenshot of the POP score graph")
time.sleep(2)

anomalies_found= driver.find_element("xpath","/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[4]/div")
anomalies_found.screenshot("./screenshots/anomalies_found.png")
print("Took the screenshot of the anomalies found graph")
time.sleep(2)

capture_progress_graph=driver.find_element("xpath","/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[2]")
capture_progress_graph.screenshot("./screenshots/capture_progress_graph.png") 
print("Took the screenshot of the capture progress graph")
time.sleep(5)

# Quit the browser session
driver.quit()
