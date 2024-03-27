from base.dx import Dx
from selenium.webdriver.common.keys import Keys
import time

class ActivityListPage(Dx):
    def click_on_create_new_activity_button(self):
        self.click_element(self.create_activity_button)

    def select_organization(self, advertiser_name):
        self.click_element(self.organization_dropdown)
        self.send_keys(self.organization_dropdown_input, advertiser_name)
        self.fill_field(self.organization_dropdown_input, Keys.ENTER)

    def click_gear_icon(self):
        self.click_element(self.gear_icon)

    def click_edit_activity_link(self):
        self.click_element(self.edit_activity_link)

    def click_view_activity_link(self):
        self.click_element(self.view_activity_link)

    def select_first_activity_checkbox(self):
        self.click_element(self.first_activity_checkbox)

    def click_activity_header_master_checkbox(self):
        self.click_element(self.header_master_checkbox)

    def click_activity_footer_master_checkbox(self):
        self.click_element(self.footer_master_checkbox)

    def click_display_checked_activities_button(self):
        self.click_element(self.display_checked_activities_button)
        time.sleep(2)

    def click_share_activities_button(self):
        self.click_element(self.share_activities_button)
        time.sleep(3)

    def click_activity_name(self):
        self.click_element(self.first_activity_name)

    def search_activity(self, search_string):
        self.fill_field(self.activity_filter_box, search_string)
        self.fill_field(self.activity_filter_box, Keys.ENTER)
        time.sleep(3)

    def click_display_activities_close_btn(self):
        self.click_element(self.display_activities_popup_close_btn)
        
    def select_sharing_organization(self):
        self.click_element(self.organization_checkbox)

    def click_share_button_from_popup(self):
        self.click_element(self.share_button)
        time.sleep(3)

    def get_innerhtml_text(self, locator, attribute = 'innerHTML'):
        innerhtml_text = str(self.find_element(getattr(self, locator)).get_attribute(attribute))
        return innerhtml_text.replace('<wbr>', '')
