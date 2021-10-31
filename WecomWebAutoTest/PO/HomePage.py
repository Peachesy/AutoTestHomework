from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.AddMembersPage import AddMembersPage
from WecomWebAutoTest.PO.Base import BasePage
from WecomWebAutoTest.PO.ContactsPage import ContactsPage
from selenium import webdriver


class HomePage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def switch_to_add_members(self):

        # 点击添加成员
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        return AddMembersPage(self.driver)

    def switch_to_contacts(self):
        return ContactsPage(self.driver)