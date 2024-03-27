from base.dx import Dx

class LoginSlidesShowPage(Dx):
    def click_edit_link(self):
        self.click_element(self.edit_link)

    def click_back_link(self):
        self.click_element(self.back_link)
