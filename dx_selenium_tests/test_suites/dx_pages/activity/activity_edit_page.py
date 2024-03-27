from selenium.webdriver.common.keys import Keys
from base.dx import Dx

class ActivityEditPage(Dx):
    
    def enter_activity_name(self, activity_name):
        self.clear_and_send_value(activity_name, self.activity_name)

    def select_activity_type(self, activity_type):
        self.click_element(self.activity_type_dropdown)
        self.clear_and_send_value(activity_type, self.activity_type_textbox)
        self.fill_field(self.activity_type_textbox, Keys.TAB)

    def select_tag_server(self, tag_server_name):
        self.click_element(self.tag_server_dropdown)
        self.clear_and_send_value(tag_server_name, self.tag_server_textbox)
        self.fill_field(self.tag_server_textbox, Keys.TAB)

    def enter_tag_id(self, tag_id):
        self.fill_field(self.tag_id, tag_id)

    def click_secure_checkbox(self):
        self.click_element(self.secure_checkbox)

    def click_rmx_checkbox(self):
        self.click_element(self.rmx_checkbox)

    def click_create_activity_button(self):
        self.click_element(self.create_activity_button)
        
    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def check_enable_sharing_checkbox(self):
        self.click_element(self.enable_sharing_checkbox)

    def click_activities_link(self):
        self.click_element(self.activities_link)

    def get_activity_name(self):
        element = self.find_element(self.activity_name)
        activity_name = str(element.get_attribute('value'))
        return activity_name
