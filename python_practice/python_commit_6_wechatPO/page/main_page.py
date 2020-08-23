'''
关于本期作业：
1.实现了添加单个部门测试用例
2.批量添加部门测试用例
3.失败测试用例
4.其中contact_page.py的
goto_add_department_by_link方法加了强制等待，这是源于企业微信的一个bug
即：手工添加子部门和脚本添加子部门UI显示不一致


关于PageObject的个人总结：
PageObject本质就是建模
根据界面封装类和方法（把全部实现暂时设置为占位符）
梳理业务流程，编写测试用例
给每个PageObject根据业务情况添加元素和对应的功能，和业务场景对标
然后与testcase结合，不断调试
用basepage封装公共方法(比如__init__,find,base_quit等)
base类不要与业务产生联系，它是高度抽象化的公共类


细节tips：
1.为了避免多次实例化driver,做了两件事
  a.在base类里加了判断语句，是为了实现driver的复用
  b.还用了类型提示self.driver:WebDriver = driver_base,类型提示是python新版本特性，用来解决动态语言的类型识别问题
 有两个好处：
  一是让它成为一个WebDriver对象，让IDE能够识别它的类型，并且在编写代码的时候能跳出提示
  二是实现driver的复用，只需在第一次进行类的实例化时（在这里指的是MainPage() 创建一次driver即可
    以后就可以把创建好的driver重复传递给新初始化的类
2.为什么要封装findElement方法
  这是因为：
  一、这些都是seleinum的API，如果以后切换技术栈，维护起来会非常繁琐
  二、在每个子类里都导seleinum包太多了，没有必要
3.webdriver对象不可以做断言，可以用列表推导式拿出它的text
4.在测试用例里添加setup_class，这样在别的函数里也可以调用了
5.return PageObject类的时候要加括号
不加括号就是没有实例化，就不能调用里面的方法，也没办法形成链式调用
比如return AddMember()就可以，return AddMember就不行
还有一个原因就是，类不能访问成员方法，成员方法必须用实例对象访问，所以类名.方法是错的（除非是@classmethod类方法
6.不被测试类引用到的变量，都加单下划线,隐藏起来，表示私有变量（不要暴露页面内部的元素给外部）
7.测试用例.py文件里，一定要加断言信息
8.测试用例类不要继承类
9.为了把公共的方法提取出来，所以创建了一个base类，并且让其他的pageObject继承它
10.return PageObject()类其实就是为了实现链式调用
11.如果在代码中出现return self，指的就是返回这个实例对象本身，这样就能实现链式调用
12. 测试类中不能有构造方法，且继承的类中也不能没有__init__  方法

--by Celia, 2020.8.23

'''
from selenium.webdriver.common.by import By
from python_practice.python_commit_6_wechatPO.page.base_page import Base
from python_practice.python_commit_6_wechatPO.page.contact_page import ContactPage


class MainPage(Base):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self.find(By.XPATH,"//*[text()='通讯录']").click()
        return ContactPage(self._driver)


    def goto_add_member(self):
        pass