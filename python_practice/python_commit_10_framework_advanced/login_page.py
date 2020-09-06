from python_practice.python_commit_10_framework_advanced.base_page import BasePage


class LoginPage(BasePage):
    def __getattr__(self, item):  # python 代理方法
        #  当一个方法找不到的时候，它会自动调用__getattr__这个方法
        print(item)
        return print #  需要返回一个可被调用的方法




    # def login_by_password(self, username, password):
    #     self.po_run("login_by_password", username=username, password=password)  # 这里的key就是对应yaml文件里的参数名