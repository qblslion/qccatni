
'''

联系人信息页

'''
from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage
from python_practice.python_commit_8_appPO.page.contactDetail_setting_page import ContactDetailSettingPage


class ContactDetailPage(BasePage):

    dots_button =(MobileBy.ID, "com.tencent.wework:id/hjz")
    def goto_contact_detail_setting_page(self):

        self.find(*self.dots_button).click()
        return ContactDetailSettingPage(self.driver)