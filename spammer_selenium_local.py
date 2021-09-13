#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

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


tag = sys.argv[1]
number = int(sys.argv[2])
type = sys.argv[3]

now = time.strftime("%H:%M:%S")
print("Started at " + now, file=sys.stderr)
print("Tag: " + tag + ", Number: " + str(number) + ".", file=sys.stderr)

options = webdriver.ChromeOptions()

if type and type == 'mobile':
    print('Mobile view.')
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

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(1)
instagram_browser = InstagramBrowser(browser)
instagram_browser.goto('https://www.instagram.com/accounts/login')
print('Opened Instagram.', file=sys.stderr)
instagram_browser.print_contents()
# browser.get_screenshot_as_file("screenshot.png")
instagram_browser.login("mjarmak", "B~ND9c,Q$4zscyU")
wait(5)
print("Logged in.", file=sys.stderr)
instagram_browser.goto("https://www.instagram.com/explore/tags/" + tag)
instagram_browser.print_contents()

instagram_browser.like_pictures(number)

sleep(5)
print("Closing browser.")
browser.close()
