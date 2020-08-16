from typing import List

import pytest

# from python_practice.pytest_learning.mycalc import myCalc
from python_practice.python_commit_3.mycalc import myCalc

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

#
# @pytest.fixture(scope="class")
# def get_cal():
#     print("开始计算")
#     calc =  myCalc()
#     yield calc
#     print("结束计算")

# #  读取测试数据
# def test_get_data(t='add'):
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         data = yaml.safe_load(f)
#         value = data[t]["value"]
#         ids = data[t]["id"]
#     return [value, ids]