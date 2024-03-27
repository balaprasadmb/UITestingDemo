from base.dx import Dx

class NewUser(Dx):
    def select_organization(self, organization, method = 'label'):
        self.select_option(self.organization_loc, organization, method)

    def click_on_add_user_role(self):
        self.click_element(self.add_user_role_button)

    def select_organization_to_add_role(self, organization, method= 'label'):
        self.select_option(self.organization_loc_role, organization, method)

    def add_user_role(self, role, method = 'label'):
        self.select_option(self.organization_role, role, method)

    def submit(self):
        self.click_element(self.user_submit)