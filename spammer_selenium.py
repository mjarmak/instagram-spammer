# geckodriver exe from https://github.com/mozilla/geckodriver/releases/tag/v0.29.1

from time import sleep
from selenium import webdriver
from spammer_pages import HomePage

# browser_executable_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
# browser = webdriver.Firefox(executable_path=browser_executable_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
# chrome_options.headless = True
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

browser.implicitly_wait(1)
browser.get('https://www.instagram.com/')

home_page = HomePage(browser)
home_page.login("mjarmak", "B~ND9c,Q$4zscyU")

home_page.goto("https://www.instagram.com/explore/tags/nature/")

# home_page.first_picture()
# home_page.like_pic()
# home_page.next_picture()
home_page.like_pictures(100)

sleep(15)

browser.close()