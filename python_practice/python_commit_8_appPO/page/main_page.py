

from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.addressList_page import AddressListPage
from python_practice.python_commit_8_appPO.page.base_page import BasePage

'''
MainPage类：企业微信app首页
类中的变量记得加self.xxxx

adb shell dumpsys window |findstr mCurrentFocus
查看当前运行的android activity

'''
class MainPage(BasePage):

    addresstext = (MobileBy.XPATH, "//*[@text='通讯录']")

    #  主页->通讯录（address list）page object
    def goto_contact(self):
        self.find(*self.addresstext).click()  #  点击通讯录
        return AddressListPage(self.driver)




