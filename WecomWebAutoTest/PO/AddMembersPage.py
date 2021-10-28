from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.Base import BasePage


class AddMembersPage(BasePage):

    def add_members_and_save(self):
        # ContactsPage和AddMembersPage两个类互相调用，会产生循环调用的问题，为解决这个问题，把导入操作放在方法内部
        from WecomWebAutoTest.PO.ContactsPage import ContactsPage
        # self.driver.find_element(By.XPATH,"//*[@id='js_contacts234']/div/div[2]/div/div[4]/div/form/div[1]/a[1]")
        self.driver.find_element(By.ID,"username").send_keys("user1")
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("0001")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("15111110000")
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()


        return ContactsPage()