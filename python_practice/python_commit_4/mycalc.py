#  计算器类
import os


class myCalc:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

# print(os.path.realpath(__file__))
# print(os.getcwd())

# for item in range(1,6):
#     print(item)
#
# y = [1]*5
# print(y)
# print(list(range(1,6)))
# print(list(zip(list(range(1,6)),y)))
#
# a='a'
# print(type(a))
# print(type(a)==str)


# import os
# import yaml
#
# current_path = os.path.dirname(os.path.realpath(__file__))
# yaml_path = os.path.join(current_path, 'calc_data.yaml')
#
# if not os.path.exists(yaml_path):
#     raise FileExistsError("文件路径不存在，请检查")
#
#
# def setup_function():
#     print("开始读取数据...")
#
#
# def teardown_function():
#     print("数据读取结束...")
#
#
# def test_get_data():
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         data = yaml.safe_load(f)
#         mydata = data['add']['value']
#         myids = data['add']['id']
#     # return [mydata], [myids]
#     return [mydata,myids]    #  正确

    # data = yaml.safe_load(f)
    #     add_id = data['add']['id']
    #     add_value = data['add']['value']
    #     print(data)
    #     print(add_id)
    #     print(add_value)
    # return add_id,add_value    # 错误
    # return data