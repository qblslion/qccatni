from time import sleep

import pytest
from selenium.webdriver.common.by import By

from python_practice.python_commit_6_wechatPO.page.main_page import MainPage


class TestAddDepartment:

    def setup_class(self):
        self.main = MainPage()

    #  单个添加子部门
    @pytest.mark.skip
    def test_add_depart(self):
        self.dp = "电商测试部门"
        self.main.goto_contact().goto_add_department_by_link().add_department(self.dp)
        sleep(2)           #  给页面等待时间，更新元素结构
        expected_dpname = self.main.find(By.XPATH,"//ul[@class='jstree-children']//li[last()]").text
        assert expected_dpname.strip() == self.dp.strip()      #  去掉字符串前后的空格


    #  批量添加子部门
    def test_add_departs(self):
        self.dp_list = ["资管线测试部门","重构部门","性能测试部门"]
        assert_flg = False
        actual_name_list = self.main.goto_contact().goto_add_department_by_link().add_departments(self.dp_list).get_departments_list()
        print(actual_name_list)
        for i in self.dp_list:
            if i in actual_name_list:
                assert_flg = True
            else:
                assert_flg = False
        assert assert_flg


    #  添加无效子部门名称（不超过32个字符），失败判断
    def test_add_depart_failed(self):
        invalid_depart_name = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        self.main.goto_contact().goto_add_department_by_link().add_department(invalid_depart_name)
        name_list = self.main.finds(By.CSS_SELECTOR, '.jstree-children a')

        #  失败判断之一：输入框仍然显示在页面上
        assert self.main.find(By.CSS_SELECTOR,'.member_tag_dialog_inputDlg').is_displayed()
        self.main.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ div:nth-child(3) [d_ck='cancel']").click()
        #  失败判断之二：遍历所有子部门，无效部门名称不会出现在子部门列表里
        assert invalid_depart_name not in [item.text for item in name_list]


    def teardown(self):
        self.main.base_quit()



