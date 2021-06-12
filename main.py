from selenium import webdriver
from time import sleep
import sys

username = sys.argv[1]
password = sys.argv[2]

class LoginBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
    
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)

        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

        sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()


login_bot = LoginBot()
