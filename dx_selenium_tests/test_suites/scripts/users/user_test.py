from dx_test.dx_test import DXTest
from users.new_user import NewUser
from configs.dx_constant import DXConstant
from lib.gui_tests import test_case

class UserTest(DXTest):
    def create_new_user(self, email, user_role = 'Campaign Manager'):
        new_user = NewUser(self.driver.get_browser())
        new_user.open()
        new_user.type_email(email)
        new_user.select_organization(new_user.organization)
        new_user.click_on_add_user_role()
        new_user.select_organization_to_add_role(new_user.organization)
        new_user.add_user_role(user_role)
        new_user.submit()
        return new_user

    @test_case()
    def validate_duplicate_email(self, email):
        self.setup()
        new_user = self.create_new_user(email)
        new_user.check_failure_message(new_user.duplicate_email_error)

    @test_case()
    def create_user_with_role(self):
        self.setup()
        count = 1000
        for user_role in NewUser(self.driver.get_browser()).roles.values():
            email = 'test' + str(count) + '@gmail.com'
            user = self.create_new_user(email, user_role)
            user.check_success_message()
            count = count + 1

    @test_case()
    def verify_admin_link(self):
        login_page = self.setup()
        login_page.close_message_popup()
        login_page.go_to_link(DXConstant().admin_link)
        login_page.page_should_contain(login_page.admin_link_message)