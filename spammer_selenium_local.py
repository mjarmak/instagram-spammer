#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

# python ./spammer_selenium_local.py https://www.instagram.com/explore/locations/213633143/brussels-belgium 5 url

import sys
from time import sleep
from selenium import webdriver
from spammer_pages import InstagramBrowser
import time


def hms_string(sec_elapsed):
    hour = int(sec_elapsed / (60 * 60))
    minute = int((sec_elapsed % (60 * 60)) / 60)
    second = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(hour, minute, second)

def wait(seconds):
    print("Wait " + str(seconds) + " seconds.", file=sys.stderr)
    sleep(seconds)


url_param = sys.argv[1]
number = int(sys.argv[2])
type = sys.argv[3]

now = time.strftime("%H:%M:%S")
print("Started at " + now, file=sys.stderr)
print("Tag: " + url_param + ", Number: " + str(number) + ".", file=sys.stderr)

options = webdriver.ChromeOptions()

mobile_emulation = {"deviceName": "iPad"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--incognito")

# options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(1)
instagram_browser = InstagramBrowser(browser)
instagram_browser.goto('https://www.instagram.com/')
print('Opened Instagram.', file=sys.stderr)
instagram_browser.print_contents()
# browser.get_screenshot_as_file("screenshot.png")
instagram_browser.login("nope", "nope")
# instagram_browser.login("mjarmak", "B~ND9c,Q$4zscyU")
wait(5)
print("Logged in.", file=sys.stderr)

if type and type == 'tag':
    instagram_browser.goto("https://www.instagram.com/explore/tags/" + url_param)
elif type and type == 'url': # no more than 10 because this technique is more restricted to protect communities
    instagram_browser.goto(url_param)

instagram_browser.print_contents()

instagram_browser.like_pictures(number)

sleep(5)
print("Closing browser.")
browser.close()
