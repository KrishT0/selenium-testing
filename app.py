from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def loging_screen(website_url, phone_number, submitted_otp):
    edge_path = EdgeChromiumDriverManager().install()
    print(edge_path)
    driver = webdriver.Edge(executable_path=edge_path)
    website_link = website_url
    driver.get(website_link)
    driver.maximize_window()
    time.sleep(10)
    phone_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[1]/input")
    print("Got the user login box, entering the phone number")
    phone_box.send_keys(phone_number)
    time.sleep(3)

    submit_otp = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/button")
    submit_otp.click()
    time.sleep(10)

    box_one = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[1]")
    box_one.send_keys("0")
    time.sleep(2)

    box_second = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[2]")
    box_second.send_keys("3")
    time.sleep(2)

    box_third = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[3]")
    box_third.send_keys("0")
    time.sleep(2)

    box_fourth = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[4]")
    box_fourth.send_keys("3")
    time.sleep(2)

    box_fifth = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[5]")
    box_fifth.send_keys("7")
    time.sleep(2)

    box_sixth = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/div/input[6]")
    box_sixth.send_keys("6")
    time.sleep(2)

    submitotp_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/form/div[3]/button")
    submitotp_btn.click()
    time.sleep(10)

    print("Logged in successfully, taking the screenshot of the insight page")
    driver.execute_script("document.body.style.zoom='50%'")
    driver.save_screenshot("./screenshots/insight_page.png")
    time.sleep(2)

#selecting date from calendar
    # calendar_input = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[1]/div/div/div/div/div/input")
    # calendar_input.click()
    # time.sleep(5)
    # new_date = "21/02/2024"
    # driver.execute_script("arguments[0].value = arguments[1]", calendar_input, new_date)
    # time.sleep(5)

#upkeep score graph
    upkeep_score_element=driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[1]/div")
    upkeep_score_element.screenshot("./screenshots/upkeep_score_element.png")
    print("Took the screenshot of the upkeep score graph")
    time.sleep(2)

#vm score graph
    vm_score=driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[2]/div")
    vm_score.screenshot("./screenshots/vm_score.png")
    print("Took the screenshot of the VM score graph")
    time.sleep(2)

#pop score graph
    # pop_score=driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[3]/div")
    # pop_score.screenshot("./screenshots/pop_score.png")
    # print("Took the screenshot of the POP score graph")
    # time.sleep(2)

#anomalies found graph
    anomalies_found= driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[4]/div")
    anomalies_found.screenshot("./screenshots/anomalies_found.png")
    print("Took the screenshot of the anomalies found graph")
    time.sleep(2)

    # bays_found_upkeep_score =  driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/div/div/div/div/div")
    # bays_found_upkeep_score.screenshot("./screenshots/bays_found_upkeep_score.png")
    # print("Took the screenshot of the bays found graph")
    # time.sleep(2)
    # driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/div").click()
    # time.sleep(5)
    # driver.find_element_by_xpath("/html/body/div[3]/div[3]/ul/li[2]").click()
    # time.sleep(5)
    # bays_found_vm_score = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/div/div/div/div/div")
    # bays_found_vm_score.screenshot("./screenshots/bays_found_vm_score.png")
    # print("Took the screenshot of the bays found vm score graph")
    # time.sleep(2)

    anomalies_remaining_graph=driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/div/svg/foreignObject")
    anomalies_remaining_graph.screenshot("./screenshots/anomalies_remaining_graph.png")
    print("Took the screenshot of the anomalies remaining graph")
    time.sleep(2)

    capture_progress_graph=driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[2]")
    capture_progress_graph.screenshot("./screenshots/capture_progress_graph.png")
    print("Took the screenshot of the capture progress graph")
    time.sleep(5)

    driver.quit()


def main():
    loging_screen("https://dishatest.neophyte.ai/", "5039931677", "xxxxxxx")


if __name__ == '__main__':
    main()

