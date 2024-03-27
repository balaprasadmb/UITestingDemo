from selenium.webdriver.common.by import By
from base.dx import Dx
from configs.dx_constant import DXConstant
import time

class AdminPage(Dx):

    def close_system_message(self):
        self.click_element(self.system_message_close)
        time.sleep(2)

    def click_display_message_link(self):
        self.click_element(self.display_message_link)
        time.sleep(1)

    def click_dismiss_all_notices_button(self):
        self.click_element(self.dismiss_all_notices_button)
        time.sleep(1)

    def click_login_screen_slides_link(self):
        self.click_element(self.login_screen_slides_link)
