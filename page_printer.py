#! /bin/bash
"exec" "$(which python3)" "$0" "$*"

import os
import sys
from time import sleep

from selenium import webdriver

url = sys.argv[1]
type = sys.argv[2]

print("Starting...", file=sys.stderr)
print("URL: " + url + ".", file=sys.stderr)

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
browser.get(url)
print('Url: ' + browser.current_url, file=sys.stderr)
print('Content: ' + browser.page_source, file=sys.stderr)

sleep(5)
print("Closing browser.")
browser.close()
