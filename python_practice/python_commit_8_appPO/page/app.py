from appium import webdriver

from python_practice.python_commit_8_appPO.page.base_page import BasePage
from python_practice.python_commit_8_appPO.page.main_page import MainPage

'''
App类：
用来存放(特定app): 企业微信app 的通用功能

'''
class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-01"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            print(self.driver)
            self.driver.implicitly_wait(5)

        else:
            self.driver.launch_app()
            # 启动任何一个包和activity
            # self.driver.start_activity(app_package,app_activity)

        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()


    def goto_main_page(self):
        return MainPage(self.driver)