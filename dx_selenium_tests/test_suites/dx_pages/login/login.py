from base.dx import Dx

class Login(Dx):
    def type_password(self, password):
        self.fill_field(self.password, password)

    def submit(self):
        self.click_element(self.login_submit)