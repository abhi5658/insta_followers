from selenium import webdriver
from time import sleep
from secrets import secret_username,secret_password

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--log-level=3')

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

    def get_unfollowers(self):
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(secret_username))\
            .click()

startInsta = InstaBot(secret_username, secret_password)
startInsta.get_unfollowers()