
'''
作业：实现部门管理，包括增删改查

'''

import requests


def get_token():
    corpid="wwbebf98fa66fd7a94"
    corpsecret="ZX7myPtY825h4G1qZeZlmUEVSDtx2ZAiG64CU0oJOvE"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)
    result = r.json()
    return result["access_token"]


#  获取部门
#  access_token专门用来传密钥
def test_get_depart():
    token = get_token()  # 先获取身份信息
    departid="3"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={departid}"  # 看接口文档传参数
    r = requests.get(url)
    print(r.json())

#  创建部门
#  把数据自动格式化成json格式，为什么转成json?“所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码”在接口文档中已明确
def test_add_depart():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}"
    data={
        "name": "北京研发中心",
        "parentid": 3,
        "id": 7
    }
    r = requests.post(url, json=data)
    print(r.json())

# 删除部门
def test_del_depart():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id=7"
    r = requests.get(url)
    print(r.json())

#  更新部门
def test_update_depart():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}"
    data={
        "id":7,
        "name":"大数据测试部门"
    }
    r = requests.post(url,json=data)
    print(r.json())

