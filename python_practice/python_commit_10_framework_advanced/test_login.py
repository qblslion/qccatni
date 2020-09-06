'''
让PO的定义也数据驱动
所有的核心都是从测试用例驱动开始的
-- by Celia
      2020.9.6
'''



##测试用例
import pytest

from python_practice.python_commit_9_framework.demo_po_page import DemoPage
from python_practice.python_commit_9_framework.utils import Utils


class TestLogin:

    # 核心数据维护在这里
    testcase_file='test_search.yaml'
    po_file = 'page_demo.yaml' # po文件和DemoPage文件是绑定在一块的

    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.demo = DemoPage(self.po_file) #  用一个传参追加一个变量，而不是一个类,所以这里要改造DemoPage
        self.demo.start()   #  启动


    def setup(self):  #  每个case执行之前都要执行
        pass

    def teardown(self): # 每个case 执行完之后都要执行
        self.demo.back()  # 点了取消这个按钮,不是后退
        return self

    def teardown_class(self):
        self.demo.stop()

    # #  一个参数化的用例
    # #  to do:测试数据的数据驱动
    @pytest.mark.parametrize('username, password',[
        ('user1','pwd1'),
        ('user2','pwd2')
    ])
    def test_login(self, username, password):
        # to do:测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1==1

    # @pytest.mark.parametrize('keyword',[
    #     'alibaba'
    #     # 'baidu',
    #     # 'jd'
    # ])
    #  通过读数据文件，读出三条数据，动态化地传递进来
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self, keyword):
        print(self.data)
        print(self.data['keys'])
        print(self.data['values'])
        print(keyword)
        # print(self.data)
        # print(keyword)
        self.demo.serach(keyword)


