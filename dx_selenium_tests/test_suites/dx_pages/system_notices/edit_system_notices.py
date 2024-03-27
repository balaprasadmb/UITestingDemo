from base.dx import Dx

class EditSystemNotices(Dx):
    def click_on_cancel_button(self):
        self.click_element(self.cancel_button)
        
    def click_on_edit_button(self):
        self.click_element(self.edit_button)