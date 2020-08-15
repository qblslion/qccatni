import os
import sys
import traceback

import yaml
import pytest

from python_practice.pytest_learning.mycalc import myCalc

current_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(current_path, 'calc_data.yaml')

if not os.path.exists(yaml_path):
    raise FileExistsError("文件路径不存在，请检查")


def setup_function():
    print("开始读取数据...")


def teardown_function():
    print("数据读取结束...")


def test_get_data(t='add'):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        value = data[t]["value"]
        ids = data[t]["id"]
    return [value, ids]


#  计算加法
class Test_mycalc_Add:

    def setup_class(self):
        self.calc = myCalc()
        print("I'm setup_class")

    def teardown_class(self):
        print("I'm teardown_class")

    def setup(self):
        print("开始加法计算")

    def teardown(self):
        print("结束加法计算")

    # 参数直接赋值
    @pytest.mark.parametrize(
        'a,b,expect',
        [(1, 2, 3), (0.1, 0.8, 0.9), (0, 8, 8), pytest.param(7, 8, 50, marks=pytest.mark.xfail)],
        ids=['int', 'float', 'zero', 'xfail']
    )
    def test_add(self, a, b, expect):
        calc_result = self.calc.add(a, b)
        if type(a) == float and type(b) == float:
            a = round(a, 3)
            b = round(b, 3)
            calc_result = round(calc_result, 3)
        assert calc_result == expect

    # 参数从yaml中读取
    @pytest.mark.parametrize(
        'a,b,expect',
        test_get_data()[0],
        ids=test_get_data()[1]
    )
    def test_add_yaml(self, a, b, expect):
        calc_result = self.calc.add(a, b)
        assert calc_result == expect

    def test_a(self):
        result = self.calc.add(1, 2)
        assert 3 == result
        print("测试用例test_a")

        t = map(lambda x: x + 1, range(1, 6))
        print(list(t))


#  计算除法
#  用了两种方法捕获异常：1.python自带try except机制 2.pytest.raises机制
class Test_mycalc_Divide:
    def setup_class(self):
        self.calc = myCalc()
        print("I'm setup class from Test_mycalc_Divide")

    def teardown_class(self):
        print("I'm teardown class from Test_mycalc_Divide")

    def setup(self):
        print("开始除法计算")

    def teardown(self):
        print("结束除法计算")

    #  参数直接赋值
    @pytest.mark.parametrize('a,b,expect', [
        (100, 2, 50),
        (0.8, 4, 0.2),
        (7, 0, 7),
        ('test', 'hello', 1)], ids=['int', 'float', 'zero', 'str'])
    def test_divide(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError) as exc_info:
                calc_result = self.calc.divide(a, b)
                raise ZeroDivisionError("division by zero")
            if exc_info.type == ZeroDivisionError:
                assert exc_info.type is ZeroDivisionError
                assert exc_info.value.args[0] == "division by zero"
                print(exc_info.value.args[0])

        elif type(a) == str or type(b) == str:
            with pytest.raises(TypeError) as exc_info:
                calc_result = self.calc.divide(a, b)
                raise TypeError("unsupported operand type(s) for /: 'str' and 'str'")
            if exc_info.type == TypeError:
                assert exc_info.type is TypeError
                assert exc_info.value.args[0] == "unsupported operand type(s) for /: 'str' and 'str'"
                print(exc_info.value.args[0])

        else:
            calc_result = self.calc.divide(a, b)
            assert calc_result == expect

    #  参数从yaml中读取
    @pytest.mark.parametrize('a,b,expect',
                             test_get_data("divide")[0],
                             ids=test_get_data("divide")[1])
    def test_divide_yaml(self, a, b, expect):
        try:
            if b == 0:
                raise ZeroDivisionError
            elif type(a) == str or type(b) == str:
                raise TypeError  # 注意，用python自带的try except机制捕捉异常的时候，如果引发异常，try结构里剩下的代码将不能执行

            calc_result = self.calc.divide(a, b)  # 如果引发ZeroDivisionError,TypeError异常，这两句不会执行，但是后面的except还是会走到
            assert calc_result == expect

        except ZeroDivisionError as e:
            print("引发异常：", repr(e))
        except TypeError as e:
            print("引发异常：", repr(e))
        except Exception as e:
            print("引发异常：", repr(e))
            # print(sys.exc_info())  #  返回一个元组，包含关于error的三个元素：type,value,object
            # print(traceback.print_exc())  #  直接打印出错误信息的value值
