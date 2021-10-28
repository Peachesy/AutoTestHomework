from WecomWebAutoTest.PO.AddMembersPage import AddMembersPage
from WecomWebAutoTest.PO.Base import BasePage


class ContactsPage(BasePage):

    def add_members(self):
        return AddMembersPage()

    def get_members_list(self):

        return []