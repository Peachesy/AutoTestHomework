from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.AddMembersPage import AddMembersPage
from WecomWebAutoTest.PO.Base import BasePage
from WecomWebAutoTest.PO.ContactsPage import ContactsPage
from selenium import webdriver


class HomePage(BasePage):

    def switch_to_add_members(self):


        # 点击添加成员
        self.driver.find_element(By.CLASS_NAME, "index_service_cnt_item_title").click()


        return AddMembersPage()

    def switch_to_contacts(self):
        return ContactsPage()