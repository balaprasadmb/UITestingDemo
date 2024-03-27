from base.dx import Dx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class DetailedEditCreatives(Dx):
    
    def click_add_creative(self):
        self.click_element(self.add_detailed_creative)

    def click_first_creative(self):
        self.click_element(self.first_creative_link)

    def input_first_creative_name(self, value):
        self.send_keys(self.first_creative_name, value)

    def input_first_concept(self, value):
        self.send_keys(self.first_concept, value)

    def select_first_size(self, value):
        self.select_option(self.first_size, value)

    def input_first_width(self, value):
        self.send_keys(self.first_size_width, value)

    def input_first_height(self, value):
        self.send_keys(self.first_size_height, value)

    def select_first_ad_type(self, value):
        self.select_option(self.first_ad_type, value)

    def select_first_ad_features(self, value):
        self.select_option(self.first_ad_feature, value)

    def select_first_tag_type(self, value):
        self.select_option(self.first_tag_type, value)

    def input_first_url(self, value):
        self.send_keys(self.first_url, value)

    def select_first_offer_type(self, value):
        self.select_option(self.first_offer_type, value)

    def input_first_add_url(self, value):
        self.send_keys(self.first_additional, value)

    def update_first_add_url(self, value):
        for text in [Keys.ENTER, value]:
            self.fill_field(self.first_additional, text)

    def input_first_start_date(self, value):
        self.fill_field(self.first_start_date, value)

    def input_first_end_date(self, value):
        self.fill_field(self.first_end_date, value)

    def select_first_lang_targeting(self, value):
        self.select_option(self.first_lang_targeting, value)

    def select_first_is_flash(self, value):
        self.select_option(self.first_is_flash, value)

    def select_first_vendor(self, value):
        self.select_option(self.first_select_vendor, value)

    def click_remove_first_vendor(self):
        self.click_element(self.first_remove_vendor)

    def click_add_first_vendor(self):
        self.click_element(self.first_new_vendor)

    def select_first_placement(self, value):
        self.select_option(self.first_placement, value)

    def input_first_z_index(self, value):
        self.send_keys(self.first_z_index, value)

    def click_first_external_id(self):
        self.click_element(self.first_new_external_id)

    def select_first_external_id_source(self, value):
        self.select_option(self.first_external_id_source, value)

    def input_first_external_id_value(self, value):
        self.fill_field(self.first_external_id_value, value)

    def click_remove_first_external_id(self):
        self.click_element(self.first_remove_external_id)

    def select_second_source(self, value):
        self.select_option(self.second_source, value)

    def input_second_value(self, value):
        self.fill_field(self.second_value, value)

    def click_remove_second_external_id(self):
        self.click_element(self.remove_second_external_id)

    def click_first_add_on(self):
        self.click_element(self.first_new_add_on)

    def input_first_add_on(self, value):
        self.fill_field(self.first_add_on_input, value)

    def select_first_add_on(self, value):
        self.select_option(self.first_add_on_select, value)

    def click_remove_first_add_on(self):
        self.click_element(self.first_add_on_remove)

    def click_first_click_tracking(self):
        self.click_element(self.first_click_tracking)

    def click_first_original_link(self):
        self.click_element(self.first_original_link)

    def click_first_processed_link(self):
        self.click_element(self.first_processed_link)
        self.click_element(self.first_processed_link)

    def click_first_secure_link(self):
        self.click_element(self.first_secure_link)

    def click_first_secure_processed_link(self):
        self.click_element(self.first_secure_processed_link)

    def input_first_tags(self, value):
        self.send_keys(self.first_edit_tags, value)

    def input_first_processed_tags(self, value):
        self.send_keys(self.first_processed_tags, value)

    def input_first_secure_tags(self, value):
        self.send_keys(self.first_secure_tags, value)

    def input_first_secure_processed_tags(self, value):
        self.send_keys(self.first_secure_processed_tags, value)

    def click_save_first(self):
        self.click_element(self.first_save)
        self.click_element(self.first_save)

    def save_creative(self):
        self.click_element(self.first_save)

    def click_preview_first(self):
        self.click_element(self.first_preview)

    def click_validate_first(self):
        self.click_element(self.first_validate)
        time.sleep(2)

    def click_cancel_first(self):
        self.click_element(self.first_cancel)

    def click_detailed_edit(self):
        self.click_element(self.detailed_edit)

    def wait_for_detailed_form(self):
        self.wait_till_visible(self.detailed_form[0], self.detailed_form[1])

    def wait_for_external_id_source(self):
        self.wait_till_visible(self.source[0], self.source[1])

    def wait_for_errors(self):
        self.wait_till_visible(self.errors[0], self.errors[1])

    def wait_for_details_view(self):
        self.wait_till_visible(self.details_view[0], self.details_view[1])
