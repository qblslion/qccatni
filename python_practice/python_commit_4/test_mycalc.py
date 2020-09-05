''''''
''' 

    作业1：
        1、补全计算器（加减乘除）的测试用例
        2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
        3、将 Fixture 方法存放在conftest.py ，设置scope=module
    作业2：
        1、编写用例顺序：加- 除-减-乘
        2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
        3、本地生成测试报告

 --------------------------------------------notes
                                        -- by celia
                                        -- 2020.9.4

1.  pytest --help|findstr collect 查询collect相关help指令（mac用grep替代findstr)
    pytest xxxx.py --setup-show   可以追溯执行过程
    pytest xxxx.py --collect-show 可以看到pytest收集测试用例的顺序
   

2. 不需要导入conftest.py模块，pytest会自动识别conftest这个神奇的文件
   在conftest.py里所有的@pytest.fixture()方法都可以直接使用

3. 如果一个方法里使用了yield,它就不再是一个普通的函数了，它就是个生成器

4. param参数可以传递参数， return request.param

5.@pytest.fixture()不能装饰类，不会对类生效
fixture要装饰在类的成员方法上或者类外的方法上，但是不可以装饰在类上


6. './data/clc.yaml'  .代表相对路径，其中 . 的意思随着执行路径的改变而改变
                    执行的路径换了  .的意思就变了
                    .代表当前路径，不是当前文件的路径，而是执行文件的当前路径
'''

import os
import sys
import pytest


# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(os.path.split(rootPath)[0])

def get_root_dir():
    curPath = os.path.dirname(os.path.dirname(__file__))
    return curPath
# 其中的__file__表示当前文件的存储路径
# os.path.dirname表示获取参数中路径的目录部分
# 利用两次dirname方法，可以获取当前文件目录的上级目录绝对路径，因为当前文件相对于项目根目录的位置为两层，所以这样获取到的绝对路径结果就是项目根目录的绝对路径


sys.path.append(get_root_dir())  # 加这句是为了避免在命令行执行的时候报找不到模块的错误


@pytest.mark.first #等价于@pytest.mark.run(order=0)
def test_1():  # pytest test_mycalc.py::test_1 -vs
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(os.path.split(rootPath)[0])
    # print(sys.path)


#  计算加法
class Test_mycalc_Add:

    # def setup_class(self):   被替换成@pytest.fixture(scope='class')
    #     self.calc = myCalc()
    #     print("I'm setup_class")
    #
    # def teardown_class(self):
    #     print("I'm teardown_class")

    def setup(self):
        print("开始加法计算")

    def teardown(self):
        print("结束加法计算")

    # f1: 直接传值
    @pytest.mark.run(order=6)
    def test_a(self, get_calc):
        # result = self.calc.add(1, 2)
        result = get_calc.add(1, 2)
        assert 3 == result
        print("测试用例test_a")

        t = map(lambda x: x + 1, range(1, 6))
        print(list(t))

    # f2: 参数赋值
    @pytest.mark.add1
    @pytest.mark.parametrize(
        'a,b,expect',
        [(1, 2, 3), (0.1, 0.8, 0.9), (0, 8, 8), pytest.param(7, 8, 50, marks=pytest.mark.xfail)],
        ids=['int', 'float', 'zero', 'xfail']
    )
    @pytest.mark.run(order=5)
    def test_add(self, get_calc, a, b, expect):
        # calc_result = self.calc.add(a, b)
        calc_result = get_calc.add(a, b)
        if type(a) == float and type(b) == float:
            a = round(a, 3)
            b = round(b, 3)
            calc_result = round(calc_result, 3)
        assert calc_result == expect

    # f3: 参数从yaml中读取，并用fixture实现参数化
    @pytest.mark.add2
    # @pytest.mark.parametrize('a,b,expect',get_data()[0],ids=get_data()[1])
    # def test_add_yaml(self, get_calc, a, b, expect):
    @pytest.mark.run(order=4)
    def test_add_yaml(self, get_calc, get_data):  # 传入fixtured的名字
        # 通过get_calc这个fixture方法能够拿到返回的calc实例
        # 如果需要返回值，一定要传入fixture方法的名字
        # 如果不需要返回值，可以不传
        # 这里测试用例需要用到calc实例，所以记得传入fixture方法的名字（get_calc）才可以拿到fixture的return
        # calc_result = self.calc.add(a, b)
        calc_result = get_calc.add(get_data[0], get_data[1])
        assert calc_result == get_data[2]


#  计算除法
#  用了两种方法捕获异常：1.python自带try except机制 2.pytest.raises机制
class Test_mycalc_Divide:
    # def setup_class(self):
    #     # self.calc = myCalc()
    #     print("I'm setup class from Test_mycalc_Divide")
    #
    # def teardown_class(self):
    #     print("I'm teardown class from Test_mycalc_Divide")

    # def setup(self):
    #     print("开始除法计算")
    #
    # def teardown(self):
    #     print("结束除法计算")

    #  f1:参数赋值
    @pytest.mark.div1
    @pytest.mark.parametrize('a,b,expect', [
        (100, 2, 50),
        (0.8, 4, 0.2),
        (7, 0, 7),
        ('test', 'hello', 1)], ids=['int', 'float', 'zero', 'str'])
    @pytest.mark.run(order=3)
    def test_divide(self, get_calc, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError) as exc_info:  # pytest.raise是报错才通过。不抛异常， 它就会报错了
                calc_result = get_calc.divide(a, b)

        elif type(a) == str or type(b) == str:
            with pytest.raises(TypeError) as exc_info:
                calc_result = get_calc.divide(a, b)

        else:
            calc_result = get_calc.divide(a, b)
            assert calc_result == expect

    #  f2:参数从yaml中读取
    @pytest.mark.div2
    # @pytest.mark.parametrize('a,b,expect',get_data("divide")[0],ids=get_data("divide")[1])
    # def test_divide_yaml(self, get_calc,a, b, expect):
    @pytest.mark.run(order=2)
    def test_divide_yaml(self, get_calc, get_data):
        try:
            if get_data[1] == 0:
                raise ZeroDivisionError
            elif type(get_data[0]) == str or type(get_data[1]) == str:
                raise TypeError

            calc_result = get_calc.divide(get_data[0], get_data[1])
            assert calc_result == get_data[2]

        except ZeroDivisionError as e:
            print("引发异常：", repr(e))
        except TypeError as e:
            print("引发异常：", repr(e))
        except Exception as e:
            print("引发异常：", repr(e))
            # print(sys.exc_info())  #  返回一个元组，包含关于error的三个元素：type,value,object
            # print(traceback.print_exc())  #  直接打印出错误信息的value值
