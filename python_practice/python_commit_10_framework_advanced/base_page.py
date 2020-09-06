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
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    _driver: WebDriver = None  # 一开始设置成None
    _current_element: WebElement = None


    def __init__(self, po_file=None):
        if po_file is not None:
            self._po_file=po_file

    @classmethod  #把driver对象,改造成类级别。类方法不需要实例化类就可以被类本身调用。cls表示没被实例化的类本身
    def start(cls): # 所有用到driver的地方除了初始化的时候不需要变，其余都要改成cls._driver类级别的driver，不能使用self
        caps={
            'platformName': 'android',
            'deviceName': 'demo1',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True
        }
        cls._driver=webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls._driver.implicitly_wait(20)
        return cls


    def stop(self):
        # 模拟appium的quit
        BasePage._driver.quit()

    #  text定位注意错别字！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    def find(self, by):                                                                     #  写的类型只有文本定位才需要转化成xpath, 其他类型可以写本来就支持的模式
        if by[0]=='text':
            by_new = (By.XPATH,f'//*[contains(@text, "{by[1]}")]')                                                      #  如果元组的第0个是个文本，就取它文本的真实内容，并把定位变成xpath
        else:
            by_new = by
        # self._current_element=self._driver.find_element(*by_new)
        self._current_element = BasePage._driver.find_element(*by_new)
        print(self._current_element)
        return self


    def click(self):  #  find之后再去调click, 这时候调用的就是BasePage本身的东西
        self._current_element.click()  #  就算出了异常，可以在这里加个异常捕获逻辑
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    # def back(self):
    #     BasePage._driver.po_run("back")
    #     return self

    # 解析po, 给一个关键字和方法的名字，它就可以自动解析其中的每一行每一列然后进行对应的操作

    # read yaml
    # with open('page_demo.yaml',encoding='utf-8') as f: # pege_demo.yaml写死在basepage不合理
    # 一级一级往上提，提出来一个通用的东西
    def po_run(self, po_method, **kwargs):
        with open(self._po_file, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            #yaml_data['search']
            for step in yaml_data[po_method]:
                print(step)
                if isinstance(step, dict):  #  如果这个步骤是个字典，那么就可以进行解析了
                    # id click send_keys
                    for key in step.keys():
                        # sleep(2)
                        # if key == 'id':
                        #     locator = (By.ID, step[key])
                        #     self.find(locator)
                        if key in ['id','aid','text']:
                            locator = (key, step[key])
                            self.find(locator)
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            #参数化，从参数里找出对应的值进行替换
                            text=str(step[key])
                            for k,v in kwargs.items():
                                # text.replace('{{%s}}'%k, v)
                                text = text.replace('${' + k + '}', v)
                            self.send_keys(text)
                        #  to do:可以不断地追加，更多关键词
                        else:
                            logging.error(f"dont know {step}")

    #  读取

        # find search
        # find by click send_keys
        #  pass
'''

    def po_run(self, po_method, **kwargs):
        # read yaml
        # logging.log.debug(f"po_run {po_method} {kwargs}")
        with open(self._po_file, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            # find search
            for step in yaml_data[po_method]:
                # find by click send_keys
                if isinstance(step, dict):
                    # id click send_keys
                    for key in step.keys():
                        if key in ['id', 'aid', 'text']:
                            locator = (key, step[key])
                            self.find(locator)

                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            text = str(step[key])
                            for k, v in kwargs.items():
                                text = text.replace('${' + k + '}', v)
                            self.send_keys(text)

                        # todo: 更多关键词
                        else:
                            logging.error(f"dont know {step}")
                            '''