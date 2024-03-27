from base.dx import Dx
import time

class UserEditPage(Dx):
    def click_on_add_user_role(self):
        self.click_element(self.add_user_role_button)

    def add_user_role(self, role, method = 'label'):
        self.select_option(self.organization_role, role, method)

    def click_on_update_user_button(self):
        self.click_element(self.update_user_button)

    def select_organization_1(self, organization, method='label'):
        self.select_option(self.organization_dropdown_1, organization, method)
        time.sleep(5)

    def select_role_1(self, role, method='label'):
        self.select_option(self.role_dropdown_1, role, method)
        time.sleep(5)

    def select_organization_2(self, organization, method='label'):
        self.select_option(self.organization_dropdown_2, organization, method)
        time.sleep(5)

    def select_role_2(self, role, method='label'):
        self.select_option(self.role_dropdown_2, role, method)
        time.sleep(5)
