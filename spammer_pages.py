from time import sleep

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        self.browser.find_element_by_css_selector("input[name='username']").send_keys(username)
        self.browser.find_element_by_css_selector("input[name='password']").send_keys(password)
        self.browser.find_element_by_xpath("//*[contains(text(), 'Accept All')]").click()
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        # sleep(5)