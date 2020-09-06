'''
让PO的定义也数据驱动
所有的核心都是从测试用例驱动开始的
-- by Celia
      2020.9.6



'''



##测试用例
import pytest

from python_practice.python_commit_10_framework_advanced.base_page import BasePage
from python_practice.python_commit_10_framework_advanced.login_page import LoginPage
from python_practice.python_commit_10_framework_advanced.demo_po_page import DemoPage
from python_practice.python_commit_10_framework_advanced.utils import Utils


class TestLogin:

    # 核心数据维护在这里
    testcase_file='test_search.yaml'
    po_file = 'page_demo.yaml' # po文件和DemoPage文件是绑定在一块的

    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.app=BasePage() # 用basepage模拟app
        self.app.start() # 这样调用start会存到basepage里面，这时候再访问子变量的_driver都是basepage的driver

        self.demo = DemoPage(self.po_file) #  用一个传参追加一个变量，而不是一个类,所以这里要改造DemoPage
        # self.demo.start()   #  启这句加上就会找不到_driver
        print(BasePage._driver) # test_login.py::TestLogin::test_login None
        print(DemoPage._driver) # <appium.webdriver.webdriver.WebDriver (session="6110dc9d-8065-4581-8316-06d76f859897")>


    def setup(self):  #  每个case执行之前都要执行
        pass


    def teardown_class(self):
        # self.demo.stop()
        self.app.stop()

    # #  一个参数化的用例
    # #  to do:测试数据的数据驱动
    # @pytest.mark.parametrize('username, password',[
    #     ('user1','pwd1'),
    #     ('user2','pwd2')
    # ])
    # def test_login1(self, username, password):
    #     # to do:测试步骤的数据驱动
    #     self.demo.login(username, password)
    #     assert 1==1

    # @pytest.mark.parametrize('keyword',[
    #     'alibaba'
    #     # 'baidu',
    #     # 'jd'
    # ])
    #  通过读数据文件，读出三条数据，动态化地传递进来
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self, keyword):
        self.demo.search(keyword)
        self.demo.back()  # 点了取消这个按钮,不是后退
        # print(self.data)
        # print(self.data['keys'])
        # print(self.data['values'])
        # print(keyword)
        # print(self.data)
        # print(keyword)

    def test_login(self):
        po_file="page_login.yaml"
        login=LoginPage(po_file)  #  LoginPage可以复用以前的类级别的类变量_driver
        #  login.start() 因为之前已经有app启动过了所以不需要再启动
        login.login_by_password('15600000000','111122')

