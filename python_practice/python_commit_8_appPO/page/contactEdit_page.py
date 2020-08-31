from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage


class ContactEditPage(BasePage):

    yes_button=(MobileBy.XPATH, "//*[@text='确定']")

    def edit_as_delete(self):
        self.find_when_scroll_and_click("删除成员")

        self.find(*self.yes_button).click()

        from python_practice.python_commit_8_appPO.page.departSearch_page import DepartSearchPage
        return DepartSearchPage(self.driver)


