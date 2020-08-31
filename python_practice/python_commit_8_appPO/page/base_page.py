import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

'''
1.判断一个对象是否是一个已知的类型
isinstance()函数 来判断一个对象是否是一个已知的类型,并认为子类是一种父类关系，支持继承关系
type() 不会认为子类是一种父类类型，不考虑继承关系

2.加日志
logging.basicConfig(level=logging.INFO)

3.获取toast两种方式（必须用XPATH)
1>XPATH定位的class定位
self.driver.find_element(MobileBy.XPATH,"//*[@class=''android.widget.Toast]").text
2>XPATH定位的text定位
self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'toast的部分内容')]").text

'''


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        # if driver is None:
        self.driver = driver

    def find(self, by, locator=None):
        return self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)



    def find_when_scroll_and_click(self, findtext):
        logging.info("滚动查找并点击")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{findtext}").instance(0));') \
                                 .click()


    def get_toasttext(self):
        logging.info("获取toast")
        toasttext=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        logging.info(toasttext)
        return toasttext