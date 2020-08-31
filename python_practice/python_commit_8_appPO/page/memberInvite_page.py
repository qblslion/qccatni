from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.addContact_page import AddContactPage
from python_practice.python_commit_8_appPO.page.base_page import BasePage


class MemberInvitePage(BasePage):
    add_by_manual=(MobileBy.XPATH, "//*[@text='手动输入添加']")

    #  在添加成员选择页面，选择了手动输入添加->跳转到手动输入添加
    def goto_manual_add_contact(self):
        # sleep(2)
        self.find(*self.add_by_manual).click()
        return AddContactPage(self.driver)



    def get_toast(self):
        # toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        toasttext = self.get_toasttext()
        return toasttext
