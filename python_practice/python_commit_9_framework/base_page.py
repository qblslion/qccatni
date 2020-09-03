'''

appium和所有UI自动化测试框架都一样，是底层提供自动化的，不是真正给我们测试去用的
测试人员要用它需要二次封装，如果不封装，基本上是用不起来的
因为真实场景就是如何帮正业务流程的顺利进行，对异常的处理，像手工测试一样智能

1.adb shell dumpsys window |findstr mCurrentFocus
mCurrentFocus=Window{1c3c3fd u0 com.xueqiu.android/com.xueqiu.android.common.MainActivity}

2.adb logcat | findstr -i displayed
找启动入口
'''
import logging

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    #  这部分的内容是我们能够稳定操控的，封装了所有页面的比较核心的内容
    #  无法数据驱动
    #  它是个底层，它的主要作用是替换appium， 解决appium的各种问题

    _driver: WebDriver = None  # 一开始设置成None
    _current_element: WebElement

    #  把app本身的启动封装进来
    def start(self):
        caps={
            'platformName': 'android',
            'deviceName': 'demo1',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True
        }
        self._driver=webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self._driver.implicitly_wait(10)
        return self


    def stop(self):
        # 模拟appium的quit
        self._driver.quit()


    def find(self, by):
        self._current_element=self._driver.find_element(*by)
        return self


    def click(self):  #  find之后再去调click, 这时候调用的就是BasePage本身的东西
        self._current_element.click()  #  就算出了异常，可以在这里加个异常捕获逻辑
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    # 解析po, 给一个关键字和方法的名字，它就可以自动解析其中的每一行每一列然后进行对应的操作
    def po_run(self, po_method, **kwargs):  # po_method  PO的方法名  # **kwargs    kv结构
    # def po_steps(self, po_method): # po_method  PO的方法名
        # read yaml
        with open('page_demo.yaml',encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            #yaml_data['search']
            for step in yaml_data[po_method]:
                if isinstance(step, dict):  #  如果这个步骤是个字典，那么就可以进行解析了
                    # id click send_keys
                    for key in step.keys():
                        if key == 'id':
                            locator = (By.ID, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            #参数化，从参数里找出对应的值进行替换
                            text=str(step[key])
                            # for k,v in kwargs: # 如果这里不.items(),会出现ValueError: too many values to unpack (expected 2)
                            for k,v in kwargs.items():
                                # text.replace('{{%s}}'%k, v)
                                text = text.replace('${' + k + '}', v)
                                # text.replace(f'${text}')
                            self.send_keys(text)
                            # self.send_keys(step[key])
                        #  to do:可以不断地追加，更多关键词
                        else:
                            logging.error(f"dont know {step}")

    #  读取







        # find search
        # find by click send_keys
        pass
