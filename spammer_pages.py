from time import sleep

import selenium
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger import log


class InstagramBrowser:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)

    def print_contents(self):
        log('Url: ' + self.browser.current_url)
        log('Title: ' + self.browser.title)
        # log('Content: ' + self.browser.page_source[0:250])

    def goto(self, url):
        log("Opening '" + url + "'.")
        self.browser.get(url)

    def first_picture(self):
        # finds the first picture
        pic = self.browser.find_element_by_class_name("kIKUG")
        pic.click()  # clicks on the first picture

    def like_pic(self):
        try:
            like = self.browser.find_element_by_class_name('fr66n')
            soup = bs(like.get_attribute('innerHTML'), 'html.parser')
            if (soup.find('svg')['aria-label'] == 'Like'):
                like.click()
        except:
            log("Like button not found, moving on to the next picture.")
            return 0

    def next_picture(self):
        try:
            self.browser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            return True
        except selenium.common.exceptions.NoSuchElementException:
            try:
                self.browser.find_element_by_class_name(
                    "l8mY4 ").click()  # other button kind in case the normal one is not used
                return True
            except selenium.common.exceptions.NoSuchElementException:
                return False

    def like_failed(self):
        return False

    def like_pictures(self, number):
        self.first_picture()
        self.like_pic()
        fail_counter = 0
        number -= 1
        log("Liked, " + str(number) + " left.")
        while number > 0:
            number -= 1
            if number % 20 == 0:
                log("Liked, " + str(number) + " left.")
            next_el = self.next_picture()
            # if next button is there then
            if next_el != False:
                # click the next button
                sleep(2)
                # like the picture
                self.like_pic()
                sleep(2)
                if self.like_failed():
                    fail_counter += 1
                    if fail_counter > 10:
                        log("Like failed 10 consecutive times, stopping.")
                        return
                else:
                    fail_counter = 0

            else:
                log("Next picture not found.")
                break

    def login(self, username, password):
        try:
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bIiDR"))).click()
            sleep(5)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
            sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        except TimeoutException:
            log('Refreshing page.')
            self.goto(self.browser.current_url)
            sleep(10)
            self.login(username, password)

    def like_pictures_in_feed(self, number):

        pics = self.gather_pictures_in_feed()
        for pic in pics:
            try:
                pic.click()
            except ElementNotInteractableException:
                log("nope")

        # scroll_count = 0
        # log("Scroll limit: " + str(number))
        # while scroll_count < number:
        #     try:
        #         el = self.browser.find_element(By.CLASS_NAME, "             qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ")
        #         el.send_keys(Keys.PAGE_DOWN)
        #         el.send_keys(Keys.PAGE_DOWN)
        #         el.send_keys(Keys.PAGE_DOWN)
        #         el.send_keys(Keys.PAGE_DOWN)
        #         el.send_keys(Keys.PAGE_DOWN)
        #         log("Scrolls: " + str(scroll_count))
        #         sleep(1)
        #         pics = self.gather_pictures_in_feed()
        #         for pic in pics:
        #             try:
        #                 pic.click()
        #             except ElementNotInteractableException:
        #                 log("nope")
        #         scroll_count += 1
        #     except Exception as err:
        #         log("ERROR")
        #         return

    def decline_notifications(self):
        log("Decline Notifications")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Not Now')]"))).click()

    def gather_pictures_in_feed(self):
        log("Gathering Posts...")
        pics = self.browser.find_elements_by_css_selector("[aria-label=Like]")
        return pics
