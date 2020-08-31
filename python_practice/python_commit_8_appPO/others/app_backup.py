import yaml
from appium import webdriver

from python_practice.python_commit_8_appPO.page.base_page import BasePage
from python_practice.python_commit_8_appPO.page.main_page import MainPage

'''
App_backup类：改造../page/app.py文件
配置的数据驱动，抽离公共数据
把配置的数据放在yaml中，让yaml驱动测试数据
udid可以算是一个公共变量

########
数据的数据驱动，把测试数据放到yaml中
步骤的数据驱动，把page的编写放到yaml中，让yaml驱动page
'''
class App_backup(BasePage):

    def start(self):
        if self.driver is None:

            caps = dict()
            # caps["udid"] = "127.0.0.1:7555"  # adb devices查看 udid
            caps["udid"] = yaml.safe_load(open("./configuration.yaml"))['caps']['udid']



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