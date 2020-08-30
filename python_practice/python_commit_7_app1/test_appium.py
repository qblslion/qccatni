from time import sleep

import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

'''
appium 企业微信app实战 v1.0
1.按部就班添加微信联系人，删除联系人
2.滚动查找
self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector()'
                        '.scrollable(true).instance(0))'
                        '.scrollIntoView(new UiSelector()'
                        '.text("添加成员").instance(0));').click()
3.删除联系人小逻辑：如果搜索没有可删除联系人
直接return 就退出整个函数 不会再执行后面的语句
'''


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

    # @pytest.mark.parametrize('name,gender,phone',[
    #     ('chumingyu','男','13910000001')
    # ])
    def test_add_contact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()

        #  滚动查找
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()


        # sleep(2)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));')\
        .click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys("chumyu")
        #self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/../android.widget.RelativeLayout").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys("139100000001")

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk6").click()

        toasttext = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert toasttext == "添加成功"

    def test_del_contact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys("chumyu")

        sleep(3)
        eles =self.driver.find_elements(MobileBy.XPATH, "//*[@text='chumyu']")
        sleep(3)
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
                                '.text("删除成员").instance(0));') \
                         .click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        eles1 = self.driver.find_elements(MobileBy.XPATH, "//*[@text='褚明宇']")
        sleep(3)
        afterdel= len(eles1)
        assert afterdel == beforedel-1