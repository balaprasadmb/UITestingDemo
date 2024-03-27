from login.login import Login
from configs.dx_constant import DXConstant
from configs.dx_web_driver import DXWebDriver

class DXTest(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.driver = DXWebDriver()
        self._page_object = None
        self._page = None

    def get_page_object(self):
        return self._page_object

    def set_page_object(self, new_page_object):
        self._page_object = new_page_object

    def get_page(self):
        return self.page

    def set_page(self, new_page):
        self._page = new_page

    def setup(self,  user_credentials = {}):
        if not user_credentials:
            user_credentials = { 'user_name': '', 'user_password': '' }
        self.set_page_object(self.login_as_user(user_credentials['user_name'], user_credentials['user_password']))
        return self.get_page_object()

    def login_as_user(self, user_name = '', password = ''):
        if not user_name:
            user_name = DXConstant().username
        if not password:
            password = DXConstant().password
        login_page = Login(self.driver.get_browser())
        login_page.open()
        login_page.type_email(user_name)
        login_page.type_password(password)
        login_page.submit()
        login_page.close_message_popup()
        login_page.switch_to_view()
        return login_page

    def __del__(self):
        if self.driver != None:
            self.driver.close_driver()
