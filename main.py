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
        self.wait = WebDriverWait(self.driver, 7)
        print('opening instagram')
        self.driver.get("https://instagram.com")
        # sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            # .click()
        self.wait_find_click("//a[contains(text(), 'Log in')]")
        
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        print('logging in..')
        # sleep(1)
        # self.is_element_exist("//button[contains(text(), 'Not Now')]")
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            # .click()
        self.wait_find_click("//button[contains(text(), 'Not Now')]")
        print('come on..not now')

    def get_unfollowers(self):
        sleep(1)
        print('open personal profile')
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(secret_username))\
            .click()
        # sleep(4)
        self.is_element_exist("//a[contains(@href,'/following')]")
        print('opening follwing tab')
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        
        # some code if  there are suggestions popping in 'following' tab
        # self.is_element_exist("/html/body/div[4]/div/div[2]")
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_height, height = 0, 1
        scroll = 0
        temploop = 0
        print("scrolling", end='', flush=True)
        # while last_height != height:
        while temploop < 2:
            last_height = height
            print(".", end='',flush=True)
            sleep(1)
            temploop += 1
            scroll += 1
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
            """, scroll_box)
        print('scrolled ', scroll, 'times')
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links """if name.text != ''"""]
        print(names)
        # for link in links:
            # print(link.text)
        # print(links)

    def wait_find_click(self, xpath_text):
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath_text)))
        return self.driver.find_element_by_xpath(xpath_text).click() if elements else False

    def is_element_exist(self,xpath_text):
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath_text)))
        return None if elements else False


# the below commented code closes the browser upon completing execution
# hence assigning to variable required
# InstaBot(secret_username, secret_password)
startInsta = InstaBot(secret_username, secret_password)

startInsta.get_unfollowers()