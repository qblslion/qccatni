from test_selenium.page.add_member_page import AddMember
from test_selenium.page.main_page import MainPage


class TestAddMember:

    #一条用例对应一个场景
    def test_add_member(self):
        self.main = MainPage()  # 实例化一个MainPage对象，用实例化的对象去调用MainPage里面的方法

        #   1.跳转到添加成员  2.添加成员
        result = self.main.go_to_addmember().add_member().get_member_list()

        assert "xiaoyin" in result


    def test_add_member_fail(self):
        self.main=MainPage()
        self.main.go_to_addmember().add_member_by_name_parameter(" ")

        # 这里需要实例化一个AddMember对象，原因是在MainPage里，return AddMember的前提是点击主页面里面的添加成员元素，而在添加成员页面是没有这个元素的
        # 所以这里不能使用链式调用 即这么写result=self.main.go_to_addmember().get_error()是错的
        result=AddMember(self.main.driver).get_error()
        assert result == "请填写姓名"


    def test_contact_add_member(self):
        #   2.跳转到通讯录页面 2.跳转到添加成员 3.添加成员
        self.main.go_to_contact().go_to_add_member().add_member()


    def teardown(self):
        self.main.base_quit()