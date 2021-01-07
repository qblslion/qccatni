from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Base:

    #  每一次实例化的时候都会去执行__init__函数
    #  所以这是为了避免重复实例化

    _url = ""  # 定义一个类变量

    def __init__(self, driver_base=None):

        if driver_base is None:
            option=Options()
            option.add_experimental_option('w3c',False)
            option.debugger_address="localhost:9222"
            self.driver=webdriver.Chrome(options=option)
        else:
            self.driver:WebDriver =driver_base  # 加类型提示

        if self._url!="":
            self.driver.get(self._url)

        self.driver.implicitly_wait(10)


    # 由于在页面对象类中还是使用了很多重复的定位元素代码，所以可以对定位元素进行进一步封装
    def find(self,by, value):
        return self.driver.find_element(by=by, value=value)


    def finds(self,by, value):
        return self.driver.find_elements(by=by, value=value)

    def base_quit(self):
        return self.driver.quit()