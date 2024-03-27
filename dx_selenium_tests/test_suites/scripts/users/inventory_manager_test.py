from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.gui_tests import test_case

class InventoryManagerTest(DXTest):
    def set_inventory_manager_role(self):
        self.setup(DXConstant().user_by_role['inventory_manager'])

    def verify_admin_link(self, admin_page):
        admin_page.close_message_popup()
        admin_page.go_to_link(DXConstant().admin_link)
        admin_page.page_should_contain(admin_page.admin_link_message)

    @test_case()
    def verify_admin_link_for_role(self):
       inventory_manager_page = self.get_page_object()
       self.verify_admin_link(inventory_manager_page)

    @test_case()
    def verify_admin_page(self):
       inventory_manager_page = self.get_page_object()
       for page_content in inventory_manager_page.admin_page_by_role['inventory_manager'].values():
            inventory_manager_page.page_should_contain(page_content)

    @test_case()
    def not_permitted_to_create_campaign(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_create_campaign)

    @test_case()
    def not_permitted_to_create_creative(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_create_creative)

    @test_case()
    def not_permitted_to_create_user(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_create_user)

    @test_case()
    def not_permitted_to_create_reports(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_create_reports)

    @test_case()
    def not_permitted_to_product_feature(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_product_feature)

    @test_case()
    def not_permitted_to_login_slide(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_login_slide)

    @test_case()
    def not_permitted_to_audience(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_audience)
        inventory_manager_page.link_not_exists(inventory_manager_page.audience_tab)

    @test_case()
    def not_permitted_to_activity(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_not_contain(inventory_manager_page.permitted_to_activity)
        inventory_manager_page.link_not_exists(inventory_manager_page.activity_tab)

    @test_case()
    def permitted_to_inventory(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.page_should_contain(inventory_manager_page.permitted_to_inventory)
        inventory_manager_page.link_exists(inventory_manager_page.inventory_tab)

    @test_case()
    def permitted_to_edit_my_account(self):
        inventory_manager_page = self.get_page_object()
        inventory_manager_page.go_to_link(inventory_manager_page.edit_my_account_link)
        inventory_manager_page.page_should_contain(inventory_manager_page.edit_user_page)
        self.set_page_object(inventory_manager_page)