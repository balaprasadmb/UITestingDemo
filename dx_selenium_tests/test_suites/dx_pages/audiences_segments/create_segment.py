from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class CreateSegment(Dx):
            
    def click_back_to_list_link(self):
        self.click_element(self.back_to_list_link)

    def click_show_link(self):
        self.click_element(self.show_link)

    def click_view_all_link(self):
        self.click_element(self.view_all_link)

    def enter_segment_name(self, segment_name):
        self.clear_and_send_value(segment_name, self.segment_name_text_box)

    def enter_segment_expiration_value(self, expiration_value):
        self.clear_and_send_value(expiration_value, self.expiration_text_box)

    def select_segment_expiration_unit(self, unit):
        self.select_option(self.expiration_units_dropdown, unit)

    def check_enable_sharing_checkbox(self):
        self.click_element(self.enable_sharing_checkbox)

    def check_organization_master_checkbox(self):
        self.click_element(self.organization_master_checkbox)
        time.sleep(1)

    def click_on_create_segment_button(self):
        self.click_element(self.create_segment_button)

    def click_on_cancel_button(self):
        self.click_element(self.cancel_button)

    def click_on_add_pixel_activity_button(self):
        self.click_element(self.add_pixel_activity_button)
        time.sleep(4)

    def click_on_see_all_pixels_link(self):
        self.click_element(self.see_all_pixels_link)

    def click_on_pixels_master_checkbox(self):
        self.click_element(self.pixel_popup_master_checkbox)
        time.sleep(2)

    def select_first_pixel_activity_from_popup(self):
        self.click_element(self.pixel_popup_first_activity_checkbox)
        time.sleep(1)

    def click_on_add_selected_pixels_button(self):
        self.click_element(self.pixel_popup_add_selected_button)

    def get_innerhtml_text(self, locator, attribute = 'innerHTML'):
        innerhtml_text = str(self.find_element(getattr(self, locator)).get_attribute(attribute))
        return innerhtml_text.replace('<wbr>', '')

    def search_activity_pixels(self, search_string):
        self.clear_and_send_value(search_string, self.pixel_popup_filter)
        self.fill_field(self.pixel_popup_filter, Keys.TAB)
        time.sleep(3)

    def click_added_pixel_edit_link(self):
        for locator in [self.added_pixel_activity_gear_icon, self.added_pixel_activity_link]:
            self.click_element(locator)
