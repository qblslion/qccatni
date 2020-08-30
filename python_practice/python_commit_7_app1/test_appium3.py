from time import sleep

import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver


'''
appium 企业微信app实战 v3.0
在第一版的基础上，增加了：
1.数据驱动，从yaml文件中读取
2.在xpath中字面量插值，滚动查找字面量插值
'''


def get_data():
    with open("./contact.yaml",encoding='UTF-8') as f:
        mydata = yaml.safe_load(f)
        print(mydata)
    return mydata


class TestAppium:

    def setup(self):
        caps={}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-01"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,gender,phone',get_data())
    def test_add_contact(self, name, gender, phone):
        operator = "添加成员"
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()

        #  滚动查找
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()


        # sleep(2)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                            f'.text("{operator}").instance(0));')\
                            .click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/../android.widget.RelativeLayout").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()

        if gender=='男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(phone)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk6").click()

        toasttext = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert toasttext == "添加成功"


    @pytest.mark.parametrize('name,gender,phone', get_data())
    def test_del_contact(self, name,gender,phone):
        operator="删除成员"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)
        sleep(3)
        eles =self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforedel = len(eles)
        print(beforedel)

        if beforedel < 2:
            print("没有可删除的成员")
            return

        eles[1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                                f'.text("{operator}").instance(0));') \
                         .click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afterdel= len(eles1)
        assert afterdel == beforedel-1