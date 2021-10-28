from WecomWebAutoTest.PO.HomePage import HomePage


class TestAddMembers:

    def test_add_members(self):
        hp = HomePage()
        # 写断言，并在断言中采用链式调用的方式，更加方便的描述业务逻辑
        assert '' in hp.switch_to_add_members().add_members_and_save().get_members_list()