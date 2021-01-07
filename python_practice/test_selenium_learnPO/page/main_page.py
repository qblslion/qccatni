# 使用类建立页面对象
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.add_member_page import AddMember
from test_selenium.page.base import Base
from test_selenium.page.contact_page import ContactPage


class MainPage(Base):
    _url="https://work.weixin.qq.com/wework_admin/frame#index"

    def go_to_contact(self):
        return ContactPage(self.driver)


    def go_to_addmember(self):
        self.driver.find_element(By.CSS_SELECTOR,"[node-type=addmember]").click()
        return AddMember(self.driver)