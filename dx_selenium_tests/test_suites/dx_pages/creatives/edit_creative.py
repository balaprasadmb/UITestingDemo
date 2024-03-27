from base.dx import Dx
from selenium.webdriver.common.keys import Keys

class EditCreative(Dx):
    
    def click_back_to_advertiser_creatives(self):
        self.click_element(self.list_of_advertiser_creative)

    def click_back_to_all_creatives(self):
        self.click_element(self.list_of_advertiser_creative)

    def input_name(self, value):
        self.send_keys(self.name, value)

    def input_concept(self, value):
        self.send_keys(self.concept, value)

    def select_size(self, value):
        self.select_option(self.size, value)

    def input_url(self, value):
        self.send_keys(self.url, value)

    def select_offer_type(self, value):
        self.select_option(self.offer_type, value)

    def input_add_url(self, value):
        self.send_keys(self.additional, value)

    def update_add_url(self, value):
        for text in [Keys.ENTER, value]:
            self.fill_field(self.additional, text)

    def select_lang_targeting(self, value):
        self.select_option(self.lang_targeting, value)

    def input_start_date(self, value):
        self.send_keys(self.start_date, value)

    def input_end_date(self, value):
        self.send_keys(self.end_date, value)

    def click_add_vendor(self):
        self.click_element(self.add_vendor)

    def select_vendor(self, value):
        self.select_option(self.vendor, value)

    def select_is_flash(self, value):
        self.select_option(self.is_flash, value)

    def select_placement(self, value):
        self.select_option(self.placement, value)

    def input_z_index(self, value):
        self.send_keys(self.z_index, value)

    def click_add_external_id(self):
        self.click_element(self.add_external_id)

    def select_source(self, value):
        self.select_option(self.source, value)

    def input_external_id(self, value):
        self.send_keys(self.value, value)

    def select_second_source(self, value):
        self.select_option(self.second_source, value)

    def input_second_external_id(self, value):
        self.send_keys(self.second_value, value)

    def click_add_crative_add_on(self):
        self.click_element(self.new_creative_add_on)

    def input_creative_add_on(self, value):
        self.send_keys(self.add_on, value)

    def select_source(self, value):
        self.select_option(self.add_on_type, value)

    def click_click_tracking(self):
        self.click_element(self.click_tracking)

    def click_cancel(self):
        self.click_element(self.cancel)

    def click_preview(self):
        self.click_element(self.preview)

    def click_update(self):
        self.click_element(self.update)
        self.click_element(self.update)

    def wait_for_edit(self):
        self.wait_till_visible(self.edit_form[0], self.edit_form[1])

    def wait_for_errors(self):
        self.wait_till_visible(self.error[0], self.error[1])
