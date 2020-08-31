from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage
from python_practice.python_commit_8_appPO.page.contactDetail_page import ContactDetailPage


class DepartSearchPage(BasePage):


    def verify_search_result_before_del(self, name):
        sleep(3)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforedel = len(eles)
        print(beforedel)

        if beforedel < 2:
            print("没有可删除的成员")
            return beforedel
            # return self.verify_before_del()

        # return beforedel, ContactDetailPage(self.driver)
        return self

    def verify_before_del(self, name):
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforedel = len(eles)
        return beforedel

    def goto_contact_detail_page_to_del(self, name):

        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        eles1[1].click()
        sleep(2)

        return ContactDetailPage(self.driver)


    def verify_after_del(self, name):
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afterdel = len(eles1)
        return afterdel
