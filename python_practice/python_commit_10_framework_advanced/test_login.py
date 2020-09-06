'''
让PO的定义也数据驱动
所有的核心都是从测试用例驱动开始的
-- by Celia
      2020.9.6



'''



##测试用例
import pytest

from python_practice.python_commit_10_framework_advanced.base_page import BasePage
from python_practice.python_commit_10_framework_advanced.common_page import CommonPage
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

        # self.demo.start()   #  启这句加上就会找不到_driver
        print(BasePage._driver) # test_login.py::TestLogin::test_login None
        print(DemoPage._driver) # <appium.webdriver.webdriver.WebDriver (session="6110dc9d-8065-4581-8316-06d76f859897")>


    def setup(self):  #  每个case执行之前都要执行
        pass


    def teardown_class(self):
        # self.demo.stop()
        self.app.stop()

    # 一个参数化的用例
    # todo:测试数据的数据驱动
    @pytest.mark.parametrize('username, password',[
        ('user1','pwd1'),
        ('user2','pwd2')
    ])
    def test_login1(self, username, password):
        # todo:测试步骤的数据驱动
        self.demo.login(username, password) # 把初始化放到以前老的case里面
        assert 1==1

    # @pytest.mark.parametrize('keyword',[
    #     'alibaba'
    #     # 'baidu',
    #     # 'jd'
    # ])

    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self, keyword):
        self.demo = DemoPage(self.po_file)  # 用一个传参追加一个变量，而不是一个类,所以这里要改造DemoPage
        self.demo.search(keyword)
        self.demo.back()                    # 点了取消这个按钮,不是后退


    #用CommonPage代替DemoPage,重写test_search方法
    #注意，一旦使用了CommonPage，调用方法里面的参数就要做适应的调整
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common_page(self, keyword):
        #todo: python元编程实现python语句的数据驱动
        demo = CommonPage(self.po_file) ## 这里用了commonPage，CommonPage既没有search方法，也没有back方法，但是它会去找。CommonPage就会调用__getattr__方法，然后就会调用po_run()，其实我们就是间接地调用po_run()
        demo.search(keyword=keyword)    ## 调用了CommonPage,这里的参数就要稍微改造一下，改成keyword=keyword
        demo.back()  # 点了取消这个按钮,不是后退


    def test_login(self):
        po_file="page_login.yaml"
        login=CommonPage(po_file)  #  LoginPage可以复用以前的类级别的类变量_driver
        #  login.start() 因为之前已经有app启动过了所以不需要再启动


        # login.xxxxx => login.__getattr__
        # 借助于__getattr__方法实现任意方法的代理
        # login.login_by_password => print
        # print('15600000000','111122')
        #login.login_by_password('15600000000','111122')

        login.login_by_password(username='15600000000', password='111122')

