from base.dx import Dx

class LoginSlidesListPage(Dx):
    def click_new_login_slides_btn(self):
        self.click_element(self.new_login_slides_btn)

    def click_gear_icon(self):
        self.click_element(self.gear_icon)

    def click_edit_link(self):
        self.click_element(self.edit_link)

    def click_delete_link(self):
        self.click_element(self.delete_link)

    def click_first_login_slide_name(self):
        self.click_element(self.first_login_slide_name)

    def get_first_login_screen_slide_name(self):
        element = self.find_element(self.first_login_slide_name)
        login_slide_name = str(element.get_attribute('innerHTML'))
        return login_slide_name
