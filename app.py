from datetime import datetime
from tempfile import mkdtemp
from zoneinfo import ZoneInfo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import json
import os
import time

def lambda_handler(event, context):
    driver = webdriver.Chrome()
    f = open("cookies.json")
    cookies = json.load(f)
    driver.get('https://www.paycomonline.net/v4/ee/web.php/app/login')
    driver.implicitly_wait(2)
    for c in cookies:
        driver.add_cookie({"name" : c["name"], "value" : c["value"]})   
    driver.implicitly_wait(2)
    login(driver)
    driver.get("https://www.paycomonline.net/v4/ee/web.php/timeclock/WEB00")
    driver.implicitly_wait(2)
    # dropdown = driver.find_element(By.ID, "punch-options-dropdown")
    clockin = driver.find_element(By.NAME, "ID")
    clockin.click()
    print(driver.current_url)
 

def login(driver: webdriver):
    username_field = driver.find_element(By.ID, "txtlogin")
    username_field.send_keys(os.environ["txtlogin"])
    pass_field = driver.find_element(By.ID, "txtpass")
    pass_field.send_keys(os.environ["txtpass"])
    pin_field = driver.find_element(By.ID, "userpinid")
    pin_field.send_keys(os.environ("userpinid"))
    submit = driver.find_element(By.ID, "btnSubmit")
    submit.click()
    driver.implicitly_wait(2)
    print(driver.current_url)
    # if not driver.current_url == "https://www.paycomonline.net/v4/ee/web.php/app/1":
    #     answer_security(driver)


# def answer_security(driver):
#     driver.implicitly_wait(4)
#     question1 = driver.find_element(By.NAME, "first_security_question")
#     q1 = question1.get_dom_attribute("aria-label")
#     print(answers[q1])
#     question1.send_keys(answers[q1])
#     question2 = driver.find_element(By.NAME, "second_security_question")
#     q2 = question2.get_dom_attribute("aria-label")
#     print(answers[q2])
#     question2.send_keys(answers[q2])
#     time.sleep(3)
#     cont = driver.find_element(By.NAME, "continue")

    
main()