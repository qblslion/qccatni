### 测试框架改进——数据驱动基础封装2

相对于数据驱动基础封装1，即python_commit_9_framework做了如下改变

####改动1：PO文件的参数化
> 框架层：
- 在BasePage引入了一个初始化的方法，允许外面传一个PO的文件
- 在BasePage的po_run方法里引入了一个self._po_file文件，它会通过一个初始化传递进来并进行使用
本质都是把写死的东西通过一个初始化的方式传递进来
> 用例里面：
- 把需要用到的文件全写到用例里面，引入测试用例文件，并调整了相关的调用代码

####改动2：代理方法等
>- 引入文本定位，修改了find方法和po_run方法
>- 新增了login类，和对应的yaml文件 page_login.yaml
>- 把BasePage start方法做了一次调整；把测试用例类里的setup_class做了一次调整
>- 加了日志log.py类
>>- 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
默认级别顺序logging.WARNING,低于该级别的就不输出了
改变默认级别为DEBUG：logging.basicConfig(level=logging.DEBUG)
>- 在login_page.py文件里，加了__getattr__方法和通用方法 _po_method(self, **kwargs)
实现了方法代理
>- 加了common_page实现通用页面的封装（其实就是把login_page.py更名为common_page.py，
把class LoginPage 改成class CommonPage
>- 新增了test_search_common_page测试用例，用CommonPage替代DemoPage
>>- 之所以把LoginPage和login_page更名为common类和common_page,
是因为实现了重构，它不再与login有关系了，而是一个通用的Page
>>- 小tips:
>1.用Refator可以实现类名的一键更改，无需再去工程里引用到的地方逐个手动改
2.右键某个元素，find usage可以查看代码中哪里会使用到







======================================
Basepage:
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
- 类方法@classmethod:
 不需要实例化类就可以被类本身调用   cls
 >cls : 表示没用被实例化的类本身
- 实例化方法:
 必须实例化类之后才能被调用 self
 >self : 表示实例化类后的地址id
