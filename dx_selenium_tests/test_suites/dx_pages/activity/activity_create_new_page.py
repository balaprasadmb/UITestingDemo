from base.dx import Dx
import time
from selenium.webdriver.common.keys import Keys

class ActivityCreateNewPage(Dx):

    def click_activities_link(self):
        self.click_element(self.activities_link)

    def enter_activity_name_first(self, activity_name):
        self.clear_and_send_value(activity_name, self.activity_name_first)

    def enter_activity_name_second(self, activity_name):
        self.clear_and_send_value(activity_name, self.activity_name_second)

    def enter_tag_id_first(self, tag_id):
        self.fill_field(self.tag_id_first, tag_id)

    def click_secure_checkbox_first(self):
        self.click_element(self.secure_checkbox_first)

    def click_rmx_checkbox_first(self):
        self.click_element(self.rmx_checkbox_first)

    def select_activity_type(self, activity_type):
        self.click_element(self.activity_type_dropdown_first)
        self.clear_and_send_value(activity_type, self.activity_type_textbox)
        self.fill_field(self.activity_type_textbox, Keys.TAB)

    def select_tag_server(self, tag_server_name):
        self.click_element(self.tag_server_dropdown_first)
        self.clear_and_send_value(tag_server_name, self.tag_server_textbox)
        self.fill_field(self.tag_server_textbox, Keys.TAB)

    def click_add_pixel_button(self):
        self.click_element(self.add_pixel_button)
        time.sleep(1)

    def click_remove_button(self):
        self.click_element(self.remove_button_second)
        time.sleep(1)

    def click_create_activity_button(self):
        self.click_element(self.create_activity_button)
        
    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def check_enable_sharing_checkbox(self):
        self.click_element(self.enable_sharing_checkbox)

    def check_create_segment_checkbox(self):
        self.click_element(self.create_segment_checkbox)

    def enter_activity_segment_name(self, activity_segment_name):
        self.fill_field(self.activity_segment_name, activity_segment_name)

    def enter_segment_expiration_value(self, segment_expiration_value):
        self.fill_field(self.expiration_text_box, segment_expiration_value)

    def select_expiration_unit(self, option, method='label'):
        self.select_option(self.expiration_unit_dropdown, option, method)

    def enter_segment_frequency(self, segment_frequency):
        self.fill_field(self.frequency_textbox, segment_frequency)

    def check_create_audience_checkbox(self):
        self.click_element(self.create_audience_checkbox)

    def enter_audience_name(self, activity_audience_name):
        self.fill_field(self.audience_name_textbox, activity_audience_name)
