from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.AddMembersPage import AddMembersPage
from WecomWebAutoTest.PO.Base import BasePage


class ContactsPage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_members(self):
        return AddMembersPage(self.driver)

    def get_members_list(self):
        ele = self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 通过列表推导式获取列表数据
        name_list = [i.text for i in ele]
        print(name_list)

        return name_list