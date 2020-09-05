import os
import sys
from typing import List

import pytest
import yaml

#  必须添加当前路径的父路径到系统路径
#  因为虽然不加这三行，IDE可以执行，但是在命令行执行pytest会提示找不到python_practice模块
#  pytest test_mycalc.py -vs
curPath = os.path.abspath(os.path.dirname(__file__))  # E:\3.qccatni\python_practice\python_commit_4
rootPath = os.path.split(curPath)[0]          # E:\3.qccatni\python_practice
sys.path.append(os.path.split(rootPath)[0])   # sys.path.append   E:\3.qccatni

from python_practice.python_commit_4.mycalc import myCalc


'''
hook函数：
pytest内置定义好的
使用技术手段在运行时动态的将额外代码依附现进程，从而实现替换现有处理逻辑或插入额外功能的目的。
它的技术实现要点有两个：
1）如何注入代码（如何将额外代码依附于现有代码中）。
2）如何确定目标函数的地址及替换。

fixture相当于我们自定义的公共的方法，可以放在conftest.py里
放在conftest里面的所有测试函数都不需要导入，可以直接使用
'''
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]  #  items就是收集上来的用例列表
) -> None:
    #  修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

'''
@pytest.fixture()函数
'''

# fixture里面有个参数scope，用来控制fixture的作用范围
# 根据作用范围大小划分：session > module > class > function
# scope = session 整个session域只执行一次，即在所有测试.py文件前后分别只执行一次
# scope = module  整个module里只会执行一次，即在每一个测试.py文件前后都执行一次
# scope = class，作用域设成类级，那会在测试用例里面每个类的前后都执行一次fixture方法
@pytest.fixture(scope='session')   # 加上@pytest.fixture()装饰器才会变成一个fixture方法. scope这里设置为module级
def get_calc():
    calc = myCalc()
    print("fixture 开始计算")
    yield calc  # 加上yield生成器，它可以激活它后面的测试步骤的执行。相当于激活一个teardown操作
                # 这里的yield还相当于一个return操作
                # 返回一个calc的实例，在测试方法里会用到这个实例
                #  需要在测试用例方法里传入fixture的名字
    print("fixture 结束计算")



def get_data(t='add'):
    yaml_path = os.path.dirname(__file__) + "\calc_data.yaml" #  拼接出当前模块下的yaml文件所在的路径

    # 也可以这么写
    # current_path = os.path.dirname(__file__) # 获取当前文件所在的路径
    # yaml_path = os.path.join(current_path, 'calc_data.yaml')
    # print(current_path)
    # print(yaml_path)

    if not os.path.exists(yaml_path):
        raise FileExistsError("文件路径不存在，请检查")

    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        value = data[t]["value"]
        ids = data[t]["id"]
    return [value, ids]


@pytest.fixture(params=get_data()[0], ids=get_data()[1])  # ids其实就是起个名字而已
def get_data(request):
    # print("request.param is", request.param)
    return request.param