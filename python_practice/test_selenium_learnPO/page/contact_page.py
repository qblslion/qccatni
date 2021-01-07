from selenium.webdriver.common.by import By

from test_selenium.page.base import Base


class ContactPage(Base):
    _namelist=(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    def go_to_add_member(self):
        from test_selenium.page.add_member_page import AddMember
        return AddMember(self.driver)

    def get_member_list(self):
        # 找到多个元素, 返回的事元素对象，需要用列表推导式把里面的内容放到列表里
        #name_list=self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list=self.finds(*self._namelist)
        list1=[]
        for name in name_list:
            list1.append(name.text)

        return list1
