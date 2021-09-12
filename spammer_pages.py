import sys
from time import sleep
import selenium
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InstagramBrowser:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)

    def goto(self, url):
        self.browser.get(url)

    def first_picture(self):
        # finds the first picture
        pic = self.browser.find_element_by_class_name("kIKUG")
        pic.click()   # clicks on the first picture

    def like_pic(self):
        try:
            like = self.browser.find_element_by_class_name('fr66n')
            soup = bs(like.get_attribute('innerHTML'),'html.parser')
            if(soup.find('svg')['aria-label'] == 'Like'):
                like.click()
        except:
            print("Like button not found, moving on to the next picture.", file=sys.stderr)
            return 0

    def next_picture(self):
        try:
            self.browser.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def like_pictures(self, number):
        self.first_picture()
        self.like_pic()
        number -= 1
        print("Liked, " + str(number) + " left.", file=sys.stderr)
        while number > 0:
            number -= 1
            print("Liked, " + str(number) + " left.", file=sys.stderr)
            next_el = self.next_picture()
            # if next button is there then
            if next_el != False:
                # click the next button
                sleep(2)
                # like the picture
                self.like_pic()
                sleep(2)
            else:
                print("Next picture not found.", file=sys.stderr)
                break

    def login(self, username, password):

        # WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW  bIiDR  ']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bIiDR"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
        # WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(username)
        # WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password)
        # self.browser.find_element_by_class_name('bIiDR').click()
        # self.browser.find_element_by_css_selector("input[name='username']").send_keys(username)
        # self.browser.find_element_by_css_selector("input[name='password']").send_keys(password)
        sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        # self.browser.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
