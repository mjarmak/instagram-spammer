# geckodriver exe from https://github.com/mozilla/geckodriver/releases/tag/v0.29.1
# heroku buildpacks:add -a instagram-spammer-prod --index 1 https://github.com/heroku/heroku-buildpack-chromedriver
# heroku buildpacks:add -a instagram-spammer-prod --index 2 https://github.com/heroku/heroku-buildpack-google-chrome
# heroku config:set -a instagram-spammer-prod GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
# heroku config:set -a instagram-spammer-prod CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver


import sys
from time import sleep
from selenium import webdriver
from spammer_pages import InstagramBrowser

# browser_executable_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
# browser = webdriver.Firefox(executable_path=browser_executable_path)

print("Starting...", file=sys.stderr)

# GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
# CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# CHROMEDRIVER_PATH = './chromedriver.exe'

# os.chmod('./chromedriver.exe', 0o755)
options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# options.add_argument("--headless")
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.binary_location = GOOGLE_CHROME_PATH
# chrome_options.headless = True
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome(options=options)


browser.implicitly_wait(1)
browser.get('https://www.instagram.com/')

instagram_browser = InstagramBrowser(browser)
instagram_browser.login("mjarmak", "B~ND9c,Q$4zscyU")

tag = sys.argv[1]
number = int(sys.argv[2])
url = "https://www.instagram.com/explore/tags/" + tag
print("Opening '" + url + "'.", file=sys.stderr)
instagram_browser.goto(url)

# home_page.first_picture()
# home_page.like_pic()
# home_page.next_picture()
instagram_browser.like_pictures(number)

sleep(15)

browser.close()
