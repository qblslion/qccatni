from time import sleep

from selenium.webdriver.common.by import By

from python_practice.python_commit_6_wechatPO.page.base_page import Base
from python_practice.python_commit_6_wechatPO.page.department_page import DepartmentPage


class ContactPage(Base):
    def goto_add_department_by_link(self):
        sleep(5)             #  如果这里不加强等，出来的是新建企业，这是企业微信的一个bug
        self.find(By.CSS_SELECTOR,".js_add_sub_party").click()
        return DepartmentPage(self._driver)


    def goto_add_department_by_file(self):
        pass


    def goto_add_department_by_click_add(self):
        # 选择所属部门直接定位self.find(By.CSS_SELECTOR,".js_parent_party_name").click()
        # 组合定位：定位下拉框里面的元素
        # 先定位外层dialog 再定位里面 $('.qui_dialog_body.ww_dialog_body [id="1688850284578717_anchor"]')
        #
        pass

    def get_departments_list(self):
        departments_name_list = self.finds(By.CSS_SELECTOR,'.jstree-children a')
        return [item.text for item in departments_name_list]

