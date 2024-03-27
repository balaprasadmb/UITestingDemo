from base.dx import Dx
import time

class UserShowPage(Dx):
    def click_on_edit_link(self):
        self.click_element(self.edit_link)
        time.sleep(5)
