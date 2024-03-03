from bs4 import BeautifulSoup
import requests
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def gen_random_time():
    return random.randint(0, 2)

def init_driver():
    service = Service(executable_path="chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        service=service,
        options=options)
    
    driver.get(url)
    driver.maximize_window()

    return driver

def click_button_by_class(driver, element):
    button = driver.find_element(By.CLASS_NAME, element)
    button.click()

def move_to_element(driver, element):
    action = ActionChains(driver)
    element = driver.find_element(By.CLASS_NAME, element)
    action.move_to_element(element)
    
    action.perform()

def handle_popup(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cancel-button-top"))
        )
        click_button_by_class(driver, "cancel-button-top")
    except:
        print("No popup")
        return

def click_show_more(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-show-more"))
        )
        click_button_by_class(driver, "btn-show-more")
        handle_popup(driver)
        # time.sleep(gen_random_time())
        move_to_element(driver, "btn-show-more")
        handle_popup(driver)
        # time.sleep(gen_random_time())   
    except:
        print("No more content")
        time.sleep(100)
        return False
    return True

if __name__=="__main__":
    url = "https://cellphones.com.vn/mobile.html"
    driver = init_driver()
    # WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "btn-show-more"))
    #     )
    counter = 0
    while click_show_more(driver):
        counter += 1
        print(f"Number of clicks: {counter}")
        pass     
    driver.quit()