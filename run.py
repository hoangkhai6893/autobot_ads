from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

import sys





class View_video:
    def __init__(self,GmailAcc,Gmailpass):
        # self.driver= webdriver.Chrome()
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://www.youtube.com")
        print("enter " + self.driver.title)
        self.email_acc = str(GmailAcc)
        self.email_pass = str(Gmailpass)
        self.time_delay_step = 3
        self.time_waiting_network = 2

    def login_acc(self):
        # click SIGN IN button
        item = self.driver.find_element_by_css_selector(
            "ytd-masthead div#buttons ytd-button-renderer a")
        item.click()
        sleep(self.time_waiting_network)
        # login google account
        self.driver.find_element_by_id("identifierId").send_keys(self.email_acc)
        self.driver.find_element_by_id("identifierNext").click()
        sleep(self.time_waiting_network)
        password_locator = (
            By.CSS_SELECTOR, 'div#password input[name="password"]')
        WebDriverWait(self.driver, 10).until(
            expect.presence_of_element_located(password_locator)
        )

        password = self.driver.find_element(*password_locator)
        WebDriverWait(self.driver, 10).until(
            expect.element_to_be_clickable(password_locator)
        )
        # fill the password
        password.send_keys(self.email_pass)
        self.driver.find_element_by_id("passwordNext").click()
        sleep(self.time_waiting_network)
        print("wait for login ...")
        WebDriverWait(self.driver, 300).until(
            expect.presence_of_element_located(
                (By.CSS_SELECTOR, "ytd-masthead button#avatar-btn"))
        )
        print("login ok")

    def skip_adds(self):
        try:
            adds_text = self.driver.find_element_by_class_name(
                'ytp-ad-simple-ad-badge')
            sleep(6)
            adds = self.driver.find_element_by_class_name(
                'ytp-ad-skip-button-container')
            adds.click()
            print('skip adds')
        except:
            print("No adds in the video")

    def search_video(self,search_text,search_code,time_to_view):
        href_code = '//a[contains(@href,"/watch?v='+search_code+'")]'
        search = self.driver.find_element_by_css_selector(  # search feature
            "ytd-masthead form#search-form input#search")
        search.click()
        print("search keyword: ", search_text)
        search.send_keys(str(search_text))
        search.submit()
        sleep(self.time_delay_step)
        item = self.driver.find_element_by_xpath(href_code)
        item.click()
        sleep(self.time_delay_step)
        self.skip_adds()
        print('start view video')
        sleep(time_to_view)
        element = self.driver.find_element_by_css_selector("ytd-player")
        element.click()
        print("Stop video ...")

    def subscribe_video(self):
        subs = self.driver.find_element_by_class_name(
            "style-scope ytd-subscribe-button-renderer")
        # subs = driver.find_element_by_css_selector("paper-button.ytd-subscribe-button-renderer")
        subs.click()
        print("subs channel")

    def like_video(self):
        like = self.driver.find_element_by_css_selector(
            "ytd-toggle-button-renderer yt-icon-button#button")
        like.click()
        print("like video")

    def RUN(self,search_text,search_code,time_to_view):
        self.login_acc()
        sleep(self.time_delay_step)
        self.search_video(search_text,search_code,time_to_view)
        sleep(self.time_delay_step)
        self.subscribe_video()
        sleep(self.time_delay_step)
        self.like_video()
        sleep(5)

if __name__ == "__main__":

    _email_acc = "kevinnguyenjp2020@gmail.com"
    _email_pass = "fibo12358"
    _search_text = "Trăm Nhớ Ngàn Thương"
    _search_code = "5WsyFOF5acY"
    _time_to_view = 10
    View_video(_email_acc,_email_pass).RUN(_search_text,_search_code,_time_to_view)
    sys.exit()  # end process
