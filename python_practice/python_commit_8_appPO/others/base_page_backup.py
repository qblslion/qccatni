import logging

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

'''
异常处理之弹框
拿雪球app 为例
1.增加了try catch机制捕获黑名单元素并处理

找出符合黑名单的元素，实际上只会找到一个，因为弹框不会一下弹出十个
而且页面上也不会有十个重复的元素，所以一般只会找到一个

2.测试数据的数据驱动

'''


class BasePageBackup:
    logging.basicConfig(level=logging.INFO)
    black_list = [(By.ID,"iv_close")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    '''处理异常'''
    def find(self, locator, value):
        try:
            element = self.driver.find_element(locator, value)
            return element                                        #  如果有这个元素，那么返回，如果没有那么触发黑名单，从黑名单中继续找
        except:
            for black in self.black_list:
                elements = self.driver.find_elements(*black)     #find_elements
                if len(elements)>0:
                    elements[0].click()                          #  取出我们需要的元素，也就是第一个元素点击即可，不必再用find找
                    break
            #  对黑名单处理完成之后，要再次去找原来的元素
            return self.find(locator, value)

    ''' 测试步骤的数据驱动'''
    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element=None
        for step in steps:
            #  对step进行解析
            if "by" in steps.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()






















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