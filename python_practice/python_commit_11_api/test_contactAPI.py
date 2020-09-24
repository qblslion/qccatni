
'''
课堂实战： 测试企业微信的联系人接口

1.登录企业微信->管理工具，开启各种API权限
2.注意，要实现添加联系人功能，需要开通通讯录同步的API编辑通讯录权限。在企业微信-管理工具-通讯录同步界面
    ——Celia 2020.9.24
'''
# 获取access token : https://work.weixin.qq.com/api/doc/90000/90135/91039
# 有了corpid和corpsecret才有获取token的资格
#  corpid: 首页->我的企业微信，获取
#  corpsecret怎么获取：比如想对通讯录进行操作，那么点通讯录->管理工具进行通讯录同步的API的管理，这样就有了一个权限，就可以对通讯录进行增删改查

import requests


def get_token():
    corpid="wwbebf98fa66fd7a94"
    corpsecret="ZX7myPtY825h4G1qZeZlmUEVSDtx2ZAiG64CU0oJOvE" # 通讯录的钥匙
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)   # r是个response对象<Response [200]>
    result = r.json()
    #print(type(r))  #  <class 'requests.models.Response'>
    #print(result["access_token"])
    return result["access_token"]


#  读取成员:  https://work.weixin.qq.com/api/doc/90000/90135/90196
#  access_token专门用来传密钥
def test_get():
    token = get_token()# 先获取身份信息
    userid="xiaoying"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"  # 看接口文档传参数
    print(requests.get(url).json())


#  创建成员： https://work.weixin.qq.com/api/doc/90000/90135/90195
#  注意，这里需要开通通讯录同步的API编辑通讯录权限。在企业微信-管理工具-通讯录同步界面
def test_add_contact():
    token=get_token() #先获取身份信息
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data = {
        "userid":"xiaoying",
        "name":"小樱",
        "mobile":"12111111110",
        "department":[1]
    }
    r=requests.post(url,json=data)
    #requests.post(url, json=data) #把数据自动格式化成json格式，为什么转成json?“所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码”在接口文档中已明确
    print(r.json())

# 删除小樱联系人
def test_del_contact():
    token=get_token()
    USERID="xiaoying"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={USERID}"
    r = requests.get(url)
    print(r.json())


#看接口文档，填必填字段 access_token，userid  文档地址 https://work.weixin.qq.com/api/doc/90000/90135/90197
def test_update_contact():
    token=get_token()
    USERID="xiaoying"
    data={
        "userid":USERID,
        "position":"产品经理",
        "department":[2]
    }
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    r = requests.post(url,json=data)
    print(r.json())
