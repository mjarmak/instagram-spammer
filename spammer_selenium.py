#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

import sys
import os
import time
from logger import log
from time import sleep
from selenium import webdriver
from spammer_pages import InstagramBrowser


# Nicely formatted time string
def hms_string(sec_elapsed):
    hour = int(sec_elapsed / (60 * 60))
    minute = int((sec_elapsed % (60 * 60)) / 60)
    second = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(hour, minute, second)

def wait(seconds):
    log("Wait " + str(seconds) + " seconds.")
    sleep(seconds)


url_param = sys.argv[1]
number = int(sys.argv[2])
type = sys.argv[3]
user = sys.argv[4]

now = time.strftime("%H:%M:%S")
log("Started at " + now)
log("Tag: " + url_param + ", Number: " + str(number) + ".")

USERNAME = os.environ.get("USERNAME_" + user)
PASSWORD = os.environ.get("PASSWORD_" + user)
log("USERNAME " + USERNAME)

GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN")
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
log("CHROMEDRIVER_PATH " + CHROMEDRIVER_PATH)
log("GOOGLE_CHROME_BINARY " + GOOGLE_CHROME_BIN)

options = webdriver.ChromeOptions()

mobile_emulation = {"deviceName": "iPad"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--disable-dev-shm-usage')

options.binary_location = GOOGLE_CHROME_BIN
browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

browser.implicitly_wait(1)
instagram_browser = InstagramBrowser(browser)
instagram_browser.goto('https://www.instagram.com')
wait(10)
log('Opened Instagram.')
instagram_browser.print_contents()
instagram_browser.accept_cookies()
instagram_browser.login(USERNAME, PASSWORD)
log("Logged in.")
wait(10)
instagram_browser.print_contents()

if "We couldn't connect to Instagram" in instagram_browser.browser.page_source or "Please wait a few minutes before" in instagram_browser.browser.page_source:
    log('Login failed, stopping.')
    raise Exception('Login failed.')

if type and type == 'tag':
    instagram_browser.goto("https://www.instagram.com/explore/tags/" + url_param)
elif type and type == 'url': # no more than 10 because this technique is more restricted to protect communities
    instagram_browser.goto(url_param)
instagram_browser.print_contents()
wait(10)

instagram_browser.like_pictures(number, USERNAME, PASSWORD)

sleep(5)
log("Closing browser.")
browser.close()
