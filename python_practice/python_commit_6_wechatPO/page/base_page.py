from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    _url = ""

    def __init__(self, driver:WebDriver = None):
        self._driver = ""

        if driver is None:
            #  复用浏览器，在已登录企业微信的chrome浏览器上测试
            option = Options()
            option.add_experimental_option('w3c', False) # 对于Message: unknown command: Cannot call non W3C standard command while in W3C mode的解决方案
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver

        if self._url !="":
            self._driver.get(self._url)


    def find(self, by, locator):
        return self._driver.find_element(by, locator)


    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)


    def base_quit(self):
        return self._driver.quit()