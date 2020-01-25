from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import secret_username,secret_password

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--log-level=3')

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
        print('opening insta')
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('logging in..')
        sleep(1)
        self.is_element_exist("//button[contains(text(), 'Not Now')]")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        print('come on..not now')

    def get_unfollowers(self):
        sleep(1)
        print('open profile')
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(secret_username))\
            .click()

    def is_element_exist(self,xpath_text):
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath_text)))
        return None if elements else False


# the below code closes the browser upon completing execution
# hence assigning to variable required
# InstaBot(secret_username, secret_password)
startInsta = InstaBot(secret_username, secret_password)

startInsta.get_unfollowers()