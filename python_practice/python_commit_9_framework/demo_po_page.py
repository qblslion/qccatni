from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_10_framework_advanced.base_page import BasePage


class DemoPage(BasePage):

    # 改造DemoPage,让它支持一个通用的参数，但是它继承BasePage，所以我们可以去改造BasePage让它支持接受一个参数
    _search_button = (MobileBy.ID, 'home_search')


    #to do: PO的数据驱动
    def login(self, username, password):
        pass


    def forget(self):
        pass


    def back(self): # 跳回功能
        self.po_run("back")

    #  完成一个search, 实现po的数据驱动
    def search(self, keyword):

        # self.find(self._search_button)   #  找到控件，如果在这后面接着click就是调用底层的方法，容易出问题
        # self.click()  #  引入一种状态，默认找到了basepage的一个基础元素，然后再去click

        #self.find(self._search_button).click()

        #import inspect
        #inspect.currentframe()[]

        # def po_run(self, po_method, **kwargs):  传进去一个关键字search和一个kv结构
        self.po_run("search", keyword=keyword)  #  定义命中的规则
 #  给定一个yaml文件中曾经给定过的词search          #   传po的时候，需要在demo page里面传参数
                                                #   当它发现带了一个参数keyword,就会完成参数的替换
        return self   #  search要返回个特定的内容，返回搜索页

    def serach1(self, dog):
        self.po_run("search", dog=dog)  # 等价于在page_demo.yaml里面参数化部分 这么写： - send_keys: ${dog}，也可以执行
        return self
