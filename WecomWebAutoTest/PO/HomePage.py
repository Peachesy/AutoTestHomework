from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.AddMembersPage import AddMembersPage
from WecomWebAutoTest.PO.Base import BasePage
from WecomWebAutoTest.PO.ContactsPage import ContactsPage
from selenium import webdriver


class HomePage(BasePage):

    def switch_to_add_members(self):


        # 点击添加成员
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()


        return AddMembersPage()

    def switch_to_contacts(self):
        return ContactsPage()