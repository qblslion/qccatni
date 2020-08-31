''''''
'''
TestContact类
测试用例类，测试添加和删除联系人，需要在每个用例里加入断言

2.在测试用例中把一系列PO链式调用的结果传给一个变量，就可以复用driver了

-2020.8.30
 by celia

appium --session-override

'''
import pytest
import yaml

from python_practice.python_commit_8_appPO.page.app import App


def get_contact():
    with open("../testdata/memberlist.yaml",encoding="utf-8") as f:
        mydata = yaml.safe_load(f)
    return mydata


class TestContact():

    #  启动app并且进入主页
    def setup(self):
        self.app =  App()
        # self.app.start()
        self.main = self.app.start().goto_main_page()

        # self.add_contacts = self.main.goto_contact().goto_MemberInvite()  如果写了这句，它就和self.main操作的是同一个driver

    def teardown(self):
        self.app.stop()

    def start_to_test_again(self):
        self.app.restart()

    @pytest.mark.parametrize('name, gender, phone',get_contact())
    def test_add_contact(self,name, gender, phone):
        mytoast = self.main.goto_contact().goto_MemberInvite()\
            .goto_manual_add_contact().add_contact_basicinfo(name, gender, phone).click_save()

        #  第二个页面开始
        # mytoast = self.add_contacts.goto_manual_add_contact()\
        #     .add_contact_basicinfo(name, gender, phone).click_save()
        toasttext = mytoast.get_toasttext()
        assert toasttext == "添加成功"

    @pytest.mark.parametrize('name, gender, phone', get_contact())
    def test_del_contact(self,name,gender,phone):

        #  判断
        verify= self.main.goto_contact().goto_department_search_page(name).verify_search_result_before_del(name)


        if type(verify) is int:
            print("没有可删除的成员")
            return
        else:
            #  删除
            beforedel = verify.verify_before_del(name)
            op = verify.goto_contact_detail_page_to_del(name).goto_contact_detail_setting_page()\
            .goto_contact_edit_page().edit_as_delete()
            afterdel = verify.verify_after_del(name)

        assert beforedel-1 == afterdel
