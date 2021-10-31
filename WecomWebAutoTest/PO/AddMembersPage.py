from selenium.webdriver.common.by import By

from WecomWebAutoTest.PO.Base import BasePage


class AddMembersPage(BasePage):
    # 定义页面元素
    username_ele = (By.ID,"username")
    memberID_ele = (By.ID,"memberAdd_acctid")
    memberPhone_ele = (By.ID,"memberAdd_phone")
    click_ele = (By.CSS_SELECTOR,".js_btn_save")

    def add_members_and_save(self):
        # ContactsPage和AddMembersPage两个类互相调用，会产生循环调用的问题，为解决这个问题，把导入操作放在方法内部
        from WecomWebAutoTest.PO.ContactsPage import ContactsPage
        # self.driver.find_element(By.XPATH,"//*[@id='js_contacts234']/div/div[2]/div/div[4]/div/form/div[1]/a[1]")
        # (*self.username_ele)为元组解包，若不解包，则传过去的内容为一个参数，参数内容是个元组
        self.find(*self.username_ele).send_keys("user1")
        self.find(*self.memberID_ele).send_keys("0001")
        self.find(*self.memberPhone_ele).send_keys("15111110000")
        self.find(*self.click_ele).click()

        return ContactsPage(self.driver)