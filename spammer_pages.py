from time import sleep

import selenium
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger import log


class InstagramBrowser:

    def __init__(self, browser, type, url_param, number):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.type = type
        self.url_param = url_param
        self.number = number

    def print_contents(self):
        log('Url: ' + self.browser.current_url)
        log('Title: ' + self.browser.title)
        # log('Content: ' + self.browser.page_source[0:250])

    def goto(self, url):
        log("Opening '" + url + "'.")
        self.browser.get(url)

    def first_picture(self):
        try:
            # finds the first picture
            # other css selectors: x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd
            first_picture = "_aagw"
            pic = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, first_picture)))
            pic.click()  # clicks on the first picture
        except:
            log('first_picture failed, Refreshing page.')
            self.like_pictures()

    def like_pic(self):
        try:
            # like_button = '._ae1h, ._ae2q'
            # TODO not working
            like_btn = self.wait.until(EC.element_to_be_clickable(By.XPATH, "//button[@class='_abl-']"))

            # like_btn = self.browser.find_element_by_css_selector(".x1n2onr6[type='svg']")
            like_btn.click()

            # like = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, like_button)))
            # like.click()
            # like = self.browser.find_elements_by_css_selector("[aria-label=Like]")
            # like.click()
            # soup = bs(like.get_attribute('innerHTML'), 'html.parser')
            # if (soup.find('svg')['aria-label'] == 'Like'):
            #     like.click()
        except:
            log("Like button not found, moving on to the next picture.")
            return 0

    def next_picture(self):
        try:
            next_button = "coreSpriteRightPaginationArrow"
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, next_button))).click()
            return True
        except selenium.common.exceptions.NoSuchElementException:
            try:
                next_button_alternative = "l8mY4 "
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                            next_button_alternative))).click()  # other button kind in case the normal one is not used
                return True
            except selenium.common.exceptions.NoSuchElementException:
                return False

    def like_failed(self):
        return False

    def like_pictures(self):

        if self.type and self.type == 'tag':
            self.goto("https://www.instagram.com/explore/tags/" + self.url_param)
        elif self.type and self.type == 'url': # no more than 10 because this technique is more restricted to protect communities
            self.goto(self.url_param)
        self.print_contents()
        try:
            sleep(10)
            self.first_picture()
            self.like_pic()
            fail_counter = 0
            self.number -= 1
            log("Liked, " + str(self.number) + " left.")
            while self.number > 0:
                self.number -= 1
                if self.number % 20 == 0:
                    log("Liked, " + str(self.number) + " left.")
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
        except TimeoutException:
            log('like_pictures failed, Refreshing page.')
            self.like_pictures()

    def login(self, username, password):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
            sleep(1)
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            # other css selectors: _acan _acap _acas _aj1-
            login_button = "_acas"
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, login_button))).click()
        except TimeoutException:
            log('login failed, Refreshing page.')
            self.goto(self.browser.current_url)
            sleep(10)
            self.login(username, password)

    def like_pictures_in_feed(self, number):

        pics = self.gather_pictures_in_feed()
        for pic in pics:
            try:
                pic.click()
                sleep(2)
                log("liked")
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
        try:
            log("Decline Notifications")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Not Now')]"))).click()
        except Exception:
            log("There is no decline notifications button")

    def gather_pictures_in_feed(self):
        log("Gathering Posts...")
        pics = self.browser.find_elements_by_css_selector("[aria-label=Like]")
        return pics

    def accept_cookies(self):
        try:
            accept_cookies_button = "_a9--"
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, accept_cookies_button))).click()
            sleep(2)
        except TimeoutException:
            log('Accept cookies button was not found. Skipping.')
