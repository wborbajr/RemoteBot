from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from time import sleep

from secrets import username, password

class RemoteBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://github.com/')

        sleep(2)

        # click Sign in link
        signin_btn = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
        signin_btn.click()

        # Enter username and password
        user_inpt = self.driver.find_element_by_xpath('//*[@id="login_field"]')
        user_inpt.send_keys(username)

        pwrd_inpt = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwrd_inpt.send_keys(password)

        # Sign in button
        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
        login_btn.click()


bot = RemoteBot()
bot.login()
