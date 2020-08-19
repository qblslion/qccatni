#  web企业微信实战（一）
#  作业内容： 使用cookie 登录企业微信，完成导入联系人，加上断言验证

'''
top预警：
   selenium请下载指定3.141.0版本，高版本有bug
   pip install selenium==3.141.0 --trusted-host http://mirrors.aliyun.com/pypi/simple/

1.复用浏览器仅适用于chrome, 启动chrome remote关键语句
  chrome --remote-debugging-port=9222 端口可以改
2.所以引入了cookie
  cookie是记录在客户端的身份验证，根据不同网站的特点cookie的时效不同
3.浏览器复用不会关闭网页，除非手动关闭，如果手动关闭则需要重新启动
4.expired是个时间戳，是系统生成的，在add_coockie时可以删掉，因为一旦出现小数会引发错误
5.定位元素的时候去chrome页面元素验证下元素是否唯一
  两种方式：$('')  css-selector定位     $x('')  xpath定位
6.shelve小写 是python内置的小型数据库
7.给每条测试用例最后添加一句断言验证操作正确性是个良好的编程习惯

   -- by Celia
      2020.08.20

'''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWechat():

    def setup_class(self):
        #  pytest框架复习： 在类中前后运行一次 setup_class, teardown_class
        db = shelve.open("mydb/logincookies")  # 打开了一个数据库

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850284576560'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'kz42vwtll3XNkWXlfnlvhG67zOGDG51uKUpHEJJVY88mccQxWTpZzAbYVL6xqepnTwtKfO2IVgw-HQxVgkJ__deSgOcjMH5dEuR7jY5XMhovH2Wsm9hCY2dP7dGTUqHa-diP5ePx4FvcoIpnG8SV_2XYBCcrrd0GdY7AA6AnJvFOAsRgvI4Mz49vhTaAhIqydf06mGPbHBia0WL97floM0LkZUGp9L2AHBFUk5lLFH7aEGiWKnS50rebXECk-jP-pE9ijy5oWZtNL-k6iWzt4Q'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850284576560'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325037155875'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1930644'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'ur4Du8srTb3k1vmFIDy-GB-om4mGijwrIOF3b8Bjxh8xV_zD0kARTcfsISoM6Zmu'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629387581, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597851582'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597883116, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '76k48k3'},
            {'domain': '.qq.com', 'expiry': 1597938173, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2022965607.1597851585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '33600610532552371'},
            {'domain': '.qq.com', 'expiry': 1597851813, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1660923773, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.72692131.1597851585'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629387580, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600443775, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        #  先存后取之——存
        db['cookie'] = cookies  # 存：通过这句，把cookies数据（就是上面一大批cookie数据）保存的数据库key里，先让数据库有cookies

    def teardown_class(self):
        db = shelve.open("mydb/logincookies")
        db.clear()
        db.close()

    def setup_method(self, method):

        #  关于浏览器复用 self.driver = webdriver.Chrome(options=option)是核心
        option = Options()  # 导入chrome对应的option
        option.debugger_address = "localhost:9222"  # 根据刚才启动的端口名填写
        # self.driver = webdriver.Chrome(options=option)

        #  打开一个新的浏览器，不复用
        self.driver = webdriver.Chrome()

        # 全局隐式等待，注意：高版本selenium这句会引发bug，请下载3.141.0版本
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        #  退出浏览器
        #  用quit()不要用close(), quit不仅关页面而且关闭进程，close仅仅关闭页面
        self.driver.quit()


    def test_import_contact(self):
        db = shelve.open("mydb/logincookies")  # 打开了一个数据库
        cookies = db['cookie']  # 先存后取之——取：获取cookies
        db.close()

        #  打开一个页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        #  拿coockie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')  # 这个值对cookie来说没有意义，没有也会运行成功。而且一旦是小数还会引起错误，所以遍历字典，出现这个key就删掉
            self.driver.add_cookie(cookie)

        #  再次打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, 'menu_contacts').click()

        #  定位页面元素$('.index_service_cnt_itemWrap:nth-child(2)') 完成点击操作 跳转页面
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys(r"E:\3.qccatni\python_practice\python_commit_5_wechat\mydata.xlsx")

        sleep(3)
        #  真正写测试用例的时候，要加断言判断测试结果
        assert "mydata.xlsx" == self.driver.find_element(By.ID,"upload_file_name").text


