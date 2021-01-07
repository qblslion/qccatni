from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from test_selenium.page.base import Base
from test_selenium.page.contact_page import ContactPage


class AddMember(Base):
    # PO: 不要暴露内部元素给外部使用，所以这里用下划线表示私有
    #  这些变量如果不会被case引用到，可以都加上下划线，这样在main页面里也不会有变量联想
    _username=(By.ID,"username")
    _account=(By.ID,"memberAdd_acctid")
    _phone=(By.CSS_SELECTOR,".ww_telInput_mainNumber")
    _save=(By.CSS_SELECTOR,".js_btn_save")

    def add_member(self):
        self.find(*self._username).send_keys("xiaoyin")
        self.find(*self._account).send_keys("xy")
        self.find(*self._phone).send_keys("18911111111")

        # 添加一个滑动操作
        action = TouchActions(self.driver)
        action.scroll_from_element(self.driver.find_element(By.ID,"username"),0,10000).perform()
        sleep(3)

        self.find(*self._save).click()

        return ContactPage(self.driver)


    #  通过参数传入姓名
    def add_member_by_name_parameter(self,name):
        self.driver.find_element(By.ID,"username").send_keys(name)
        #  输入错误格式的姓名之后，随便点击页面的一个其他元素，让错误信息展示在页面上
        self.driver.find_element(By.XPATH,"//label[contains(text(),'帐号')]").click()

    # 如果添加错误的姓名（如空格）会在页面上显示错误提示信息，通过这个思路去验证fail的情况
    def get_error(self):
        error_msg = self.driver.find_element(By.XPATH,"//div[text()='请填写姓名']").text

        return error_msg