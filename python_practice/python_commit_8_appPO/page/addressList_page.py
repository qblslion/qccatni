from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage

#通讯录page object
from python_practice.python_commit_8_appPO.page.departSearch_page import DepartSearchPage
from python_practice.python_commit_8_appPO.page.memberInvite_page import MemberInvitePage


class AddressListPage(BasePage):

    search_button=(MobileBy.ID, "com.tencent.wework:id/hk9")
    search_bar=(MobileBy.ID, "com.tencent.wework:id/g75")
    #  通讯录->点击添加成员->跳转到添加成员选择页面
    def goto_MemberInvite(self):
        sleep(2)
        self.find_when_scroll_and_click("添加成员")  #  滚动查找添加成员link
        return MemberInvitePage(self.driver)


    def goto_department_search_page(self, name):
        self.find(*self.search_button).click()
        self.find(*self.search_bar).send_keys(name)

        return DepartSearchPage(self.driver)




