from base.dx import Dx

class LoginSlidesEditPage(Dx):
    def enter_login_slide_name(self, login_slide_name):
        self.clear_and_send_value(login_slide_name, self.name_textbox)

    def enter_login_slide_body(self, login_slide_body):
        self.clear_and_send_value(login_slide_body, self.body_textbox)

    def click_enabled_checkbox(self):
        self.click_element(self.enabled_checkbox)

    def click_create_login_slide_btn(self):
        self.click_element(self.create_login_slide_btn)

    def click_edit_page_back_link(self):
        self.click_element(self.edit_page_back_link)

    def click_new_page_back_link(self):
        self.click_element(self.new_page_back_link)
