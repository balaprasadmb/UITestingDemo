from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.gui_tests import test_case
from users.new_user import NewUser

class OrganizationAdministratorTest(DXTest):
    def set_organization_administrator_role(self):
        self.setup(DXConstant().user_by_role['organization_administrator'])

    @test_case()
    def verify_admin_link(self, admin_page):
        admin_page.close_message_popup()
        admin_page.go_to_link(DXConstant().admin_link)
        admin_page.page_should_contain(admin_page.admin_link_message)

    @test_case()
    def verify_admin_link_for_role(self):
        organization_administrator_page = self.get_page_object()
        self.verify_admin_link(organization_administrator_page)

    @test_case()
    def permitted_to_edit_my_account(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.go_to_link(organization_administrator_page.edit_my_account_link)
        organization_administrator_page.page_should_contain(organization_administrator_page.edit_user_page)
        self.set_page_object(organization_administrator_page)

    def create_new_user(self, user_role = 'campaign_manager'):
        new_user = NewUser(self.driver.get_browser())
        email = 'test_' + new_user.get_random_string(5) + '@dataxu.com'
        new_user.open()
        new_user.type_email(email)
        new_user.select_organization(new_user.organization)
        new_user.click_on_add_user_role()
        new_user.select_organization_to_add_role(new_user.organization)
        new_user.add_user_role(new_user.roles[user_role])
        new_user.submit()
        return new_user

    @test_case()
    def create_user_campaign_manager(self):
        new_user = self.create_new_user()
        new_user.check_success_message()

    @test_case()
    def create_user_inventory_manager(self):
        new_user = self.create_new_user('inventory_manager')
        new_user.check_success_message()

    @test_case()
    def create_user_planner(self):
        new_user = self.create_new_user('planner')
        new_user.check_success_message()

    @test_case()
    def create_user_read_only(self):
        new_user = self.create_new_user('read_only_user')
        new_user.check_success_message()

    @test_case()
    def create_user_report(self):
        new_user = self.create_new_user('report_user')
        new_user.check_success_message()

    @test_case()
    def create_user_support(self):
        new_user = self.create_new_user('support_user')
        new_user.check_success_message()

    @test_case()
    def create_user_user_administrator(self):
        new_user = self.create_new_user('user_administrator')
        new_user.check_success_message()

    @test_case()
    def not_permitted_to_create_campaign(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_not_contain(organization_administrator_page.permitted_to_create_campaign)

    @test_case()
    def not_permitted_to_create_reports(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_not_contain(organization_administrator_page.permitted_to_create_reports)

    @test_case()
    def not_permitted_to_create_creative(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_not_contain(organization_administrator_page.permitted_to_create_creative)

    @test_case()
    def not_permitted_to_activity(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_not_contain(organization_administrator_page.permitted_to_activity)
        organization_administrator_page.link_not_exists(organization_administrator_page.activity_tab)

    @test_case()
    def not_permitted_to_inventory(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_not_contain(organization_administrator_page.permitted_to_inventory)
        organization_administrator_page.link_not_exists(organization_administrator_page.inventory_tab)

    @test_case()
    def permitted_to_product_feature(self):
        organization_administrator_page = self.get_page_object()
        organization_administrator_page.page_should_contain(organization_administrator_page.permitted_to_product_feature)

