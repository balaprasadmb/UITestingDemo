from base.dx import Dx
import time

class UserListPage(Dx):
    def click_on_edit_icon(self):
        self.click_element(self.edit_icon)

    def filter_user(self, user_name):
        self.clear_and_send_value(user_name, self.filter)
        self.press_enter_key(self.filter)
        time.sleep(5)

    def click_user_email(self, user_email):
        self.click_element(user_email)
        time.sleep(5)
