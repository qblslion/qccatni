import os
import sys
from time import sleep

import pytest
import yaml


'''
# 获取当前文件所在的绝对路径（不包括文件名）
写法1：os.path.dirname(os.path.realpath(__file__)) 
写法2：os.path.dirname(__file__)
二者等价

# 获取当前文件所在的路径（包括文件名）
os.path.abspath(__file__)

# 获取当前文件所在的路径的上一级路径 (上上一级等 详见#https://www.jianshu.com/p/1bb207a6f1e9
os.path.dirname(os.path.dirname(__file__))

# 按照路径将文件名和路径分割开 os.path.split方法
应用：
os.path.split(os.path.dirname(__file__))

'''



def test_get_data(t='add'):
    yaml_path = os.path.dirname(__file__)+"\calc_data.yaml"

    # 测试1：比较os.path.dirname() 不包含文件名  和os.path.abspath() 包含文件名   的区别
    # q1=os.path.dirname(__file__)
    # q2=os.path.abspath(__file__)
    # x1=os.path.split(os.path.dirname(__file__))
    # x2=os.path.split(os.path.abspath(__file__))
    #
    # #os.path.dirname(os.path.abspath(__file__))等价于os.path.dirname(__file__)
    # print(q1)
    # print(q2)
    # print(x1)
    # print(x2)

    # 测试2 获取当前文件路径与获取父路径
    # p1 = os.path.abspath(os.path.dirname(__file__)) # 获取当前文件的路径
    # p2= os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的路径的上一级路径
    # print(p1)
    # print(p2)

    # 测试3 等价于本函数第一句的yaml_path
    # path1 = os.path.dirname(__file__) #  获取当前文件所在的绝对路径
    # current_path = os.path.dirname(os.path.realpath(__file__)) #  获取当前文件所在的绝对路径
    # yaml_path = os.path.join(current_path, 'calc_data.yaml')
    # print(path1)
    # print(current_path)
    # print(yaml_path)

    # 测试4：测试os.path.split方法
    #
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = os.path.split(curPath)[0]
    # sys.path.append(os.path.split(rootPath)[0])
    #
    # curPath = os.path.abspath(os.path.dirname(__file__)) # E:\3.qccatni\python_practice\python_commit_4
    # testpath =  os.path.split(curPath) #('E:\\3.qccatni\\python_practice', 'python_commit_4')
    # rootPath = os.path.split(curPath)[0] # E:\3.qccatni\python_practice
    # d = os.path.split(rootPath)[0] # E:\3.qccatni
    # c = sys.path.append(os.path.split(rootPath)[0])
    # print("sys path", sys.path)
    # print("curPath: ", curPath)
    # print("testpath:", testpath)
    # print("rootPath: ", rootPath)
    # print("after sys.path.append:", c)
    # print(d)

    # if not os.path.exists(yaml_path):
    #     raise FileExistsError("文件路径不存在，请检查")
    #
    # with open(yaml_path, 'r', encoding='utf-8') as f:
    #     data = yaml.safe_load(f)
    #     value = data[t]["value"]
    #     ids = data[t]["id"]
    # return [value, ids]

@pytest.mark.run(order=2)
def test_a():
    pytest.assume(1==5)
    # pytest.assume(2==5)
    # pytest.assume(3==5)
    pytest.assume(5==5)
    # pytest.assume(4==5)

    # assert 1==1
    # assert 2==3
    # print("aaa")


# @pytest.mark.flaky(reruns=5, reruns_delay=2)
# def test_b():
#     assert False

@pytest.mark.run(order=1)
def test_C():
    assert True

@pytest.mark.parametrize('a',[1,2,3,4])
def test_xdist(a):
    sleep(1)
    print(a)
