import sys
from time import sleep
import selenium
from bs4 import BeautifulSoup as bs

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

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
            print("Like button not found, moving on to the next picture.", file=sys.stdout)
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
        print("Liked, " + str(number) + " left.", file=sys.stdout)
        while number > 0:
            number -= 1
            print("Liked, " + str(number) + " left.", file=sys.stdout)
            next_el = self.next_picture()
            # if next button is there then
            if next_el != False:
                # click the next button
                sleep(2)
                # like the picture
                self.like_pic()
                sleep(2)
            else:
                print("Next picture not found.", file=sys.stdout)
                break

    def login(self, username, password):
        self.browser.find_element_by_css_selector("input[name='username']").send_keys(username)
        self.browser.find_element_by_css_selector("input[name='password']").send_keys(password)
        self.browser.find_element_by_xpath("//*[contains(text(), 'Accept All')]").click()
        sleep(1)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
