#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

import sys
import os
from time import sleep
from selenium import webdriver
from spammer_pages import InstagramBrowser

tag = sys.argv[1]
number = int(sys.argv[2])
type = sys.argv[3]

print("Starting...", file=sys.stderr)
print("Tag: " + tag + ", Number: " + str(number) + ".", file=sys.stderr)

GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN")
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")
print("CHROMEDRIVER_PATH " + CHROMEDRIVER_PATH)
print("GOOGLE_CHROME_BINARY " + GOOGLE_CHROME_BIN)

options = webdriver.ChromeOptions()

if type and type == 'mobile':
    print('Mobile view.')
    mobile_emulation = {"deviceName": "iPad"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")
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
print('Opened Instagram.', file=sys.stderr)
print('Url: ' + instagram_browser.browser.current_url, file=sys.stderr)
print('Content: ' + instagram_browser.browser.page_source[0:500], file=sys.stderr)
instagram_browser.login("mjarmak", "B~ND9c,Q$4zscyU")
print("Logged in.", file=sys.stderr)
url = "https://www.instagram.com/explore/tags/" + tag
print("Opening '" + url + "'.", file=sys.stderr)
instagram_browser.goto(url)
print('Url: ' + instagram_browser.browser.current_url, file=sys.stderr)
print('Content: ' + instagram_browser.browser.page_source[0:500], file=sys.stderr)

instagram_browser.like_pictures(number)

sleep(5)
print("Closing browser.")
browser.close()
