from appium.webdriver.common.mobileby import MobileBy

from python_practice.python_commit_8_appPO.page.base_page import BasePage

'''

AddContactPage类：
添加联系人page
1.如果方法执行完成后还停留在当前页面，返回self, return self
2.alt+回车\command+回车导locally包，避免循环导入，python不支持循环导入

'''
class AddContactPage(BasePage):
    name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_elementM= (MobileBy.XPATH, "//*[@text='男']")  #  default choice
    gender_elementF = (MobileBy.XPATH, "//*[@text='女']")
    phone_element = (MobileBy.ID, "com.tencent.wework:id/f9s")
    save_element = (MobileBy.ID, "com.tencent.wework:id/hk6")

    def add_contact_basicinfo(self, name, gender, phone):
        self.find(*self.name_element).send_keys(name)
        self.find(*self.gender_elementM).click()

        # print(gender)
        #  根据传入的参数选择性别
        if gender == '男':
            self.find(*self.gender_elementM).click()
        else:
            self.find(*self.gender_elementF).click()

        #  传入电话号码
        self.find(*self.phone_element).send_keys(phone)

        return self

    def click_save(self):
        self.find(*self.save_element).click()
        from python_practice.python_commit_8_appPO.page.memberInvite_page import MemberInvitePage  # 避免循环导入
        return MemberInvitePage(self.driver)
