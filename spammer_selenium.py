#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

import sys
from time import sleep
from selenium import webdriver
from spammer_pages import InstagramBrowser

tag = sys.argv[1]
number = int(sys.argv[2])

print("Starting...", file=sys.stderr)
print("Tag: " + tag + ", Number: " + str(number) + ".", file=sys.stderr)

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(1)
browser.get('https://www.instagram.com/')
print('Opened Instagram.')
instagram_browser = InstagramBrowser(browser)
instagram_browser.login("mjarmak", "B~ND9c,Q$4zscyU")

url = "https://www.instagram.com/explore/tags/" + tag
print("Opening '" + url + "'.", file=sys.stderr)
instagram_browser.goto(url)

instagram_browser.like_pictures(number)

sleep(5)
print("Closing browser.")
browser.close()
