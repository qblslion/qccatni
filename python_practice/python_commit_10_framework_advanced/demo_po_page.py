from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_10_framework_advanced.base_page import BasePage


class DemoPage(BasePage):

    # 这句用不到了，就删掉
    #_search_button = (MobileBy.ID, 'home_search')


    #to do: PO的数据驱动
    def login(self, username, password):
        pass


    def forget(self):
        pass


    # def serach1(self, dog):
    #     self.po_run("search", dog=dog)  # 等价于在page_demo.yaml里面参数化部分 这么写： - send_keys: ${dog}，也可以执行
    #     return self

'''  
#之所以删掉back和search这两个方法，是因为它们最后都会调用po_run方法，而且back没有参数。search有参数。
如果采用PO，用common_page实现的话，只要传的时候传入对应的yaml，写对应的名字就可以了，根本不用去写对应的类
   
    def back(self): # 跳回功能
        self.po_run("back")

    #  完成一个search, 实现po的数据驱动
    def search(self, keyword):
        # def po_run(self, po_method, **kwargs):  传进去一个关键字search和一个kv结构
        #  给定一个yaml文件中曾经给定过的词search。传po的时候，需要在demo page里面传参数
        self.po_run("search", keyword=keyword)  #  定义命中的规则      
                                                 #  当它发现带了一个参数keyword,就会完成参数的替换
        return self   #  search要返回个特定的内容，返回搜索页
        '''



