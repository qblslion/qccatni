from selenium.webdriver.common.by import By

from python_practice.python_commit_6_wechatPO.page.base_page import Base


class DepartmentPage(Base):
    _add_sub_depart = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg [name='name']")
    _input_sub_depart_name = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg [name='name']")
    _submit_sub_depart_form = (By.CSS_SELECTOR, "#__dialog__MNDialog__ div:nth-child(3) [d_ck='submit']")
    _cancel_sub_depart_form = (By.CSS_SELECTOR, "#__dialog__MNDialog__ div:nth-child(3) [d_ck='cancel']")

    def add_department(self, dp):
        # self.find(By.CSS_SELECTOR, ".member_tag_dialog_inputDlg [name='name']").click()
        # self.find(By.CSS_SELECTOR,".member_tag_dialog_inputDlg [name='name']").send_keys(dp)
        # #  点击确定
        # self.find(By.CSS_SELECTOR,"#__dialog__MNDialog__ div:nth-child(3) [d_ck='submit']").click()
        self.find(*self._add_sub_depart).click()
        self.find(*self._input_sub_depart_name).send_keys(dp)
        self.find(*self._submit_sub_depart_form).click()
        from python_practice.python_commit_6_wechatPO.page.contact_page import ContactPage
        return ContactPage(self._driver)



    def add_departments(self, dp_list):
        for item in dp_list:
            self.find(*self._add_sub_depart).click()
            self.find(*self._input_sub_depart_name).send_keys(item)
            self.find(*self._submit_sub_depart_form).click()
            self.find(By.CSS_SELECTOR, ".js_add_sub_party").click()  # 还要重新点击添加子部门
        self.find(*self._cancel_sub_depart_form).click()  # 添加到最后一个元素的时候，取消弹框并返回通讯录页面
        print("添加完毕")
        from python_practice.python_commit_6_wechatPO.page.contact_page import ContactPage
        return ContactPage(self._driver)
