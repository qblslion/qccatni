from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage
from python_practice.python_commit_8_appPO.page.contactEdit_page import ContactEditPage


class ContactDetailSettingPage(BasePage):
    set_contact = (MobileBy.XPATH, "//*[@text='编辑成员']")
    def goto_contact_edit_page(self):
        self.find(*self.set_contact).click()
        return ContactEditPage(self.driver)