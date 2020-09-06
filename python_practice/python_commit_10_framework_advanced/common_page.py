
from python_practice.python_commit_10_framework_advanced.base_page import BasePage
from python_practice.python_commit_10_framework_advanced.log import log

# 当方法找不到的时候会去调用__getattr__方法
# 接着返回了一个_po_method方法，让PO去调
# 接着PO转而就去调用po_run方法
class CommonPage(BasePage):

    def __getattr__(self, item):  # python 代理方法
        #  当一个方法找不到的时候，它会自动调用__getattr__这个方法
        # print(item)
        log.debug(f'__getattr__ {item}')   #  打印内容 __getattr__ login_by_password
        self._method_name = item
        # return print #  需要返回一个可被调用的方法
        #  当方法找不到的时候，调用一个通用方法进行处理
        return self._po_method  #  返回一个我们造的通用的万能方法
                                # 不要加括号

    #  定义通用方法
    def _po_method(self, **kwargs):
        log.debug(f"_po_method {kwargs}")  # 打印内容   _po_method {'username': '15600000000', 'password': '111122'}
        self.po_run(self._method_name, **kwargs)

    #  故意省略这个方法的定义，是为了使用python代理这一特殊用法
    # def login_by_password(self, username, password):
    #     self.po_run("login_by_password", username=username, password=password)  # 这里的key就是对应yaml文件里的参数名