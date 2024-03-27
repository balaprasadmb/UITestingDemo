from base.dx import Dx
from selenium.webdriver.common.action_chains import ActionChains

class EditCreatives(Dx):

    def click_creative_list_link(self):
        self.click_element(self.back_to_creatives_list)

    def click_all_creative_list_link(self):
        self.click_element(self.back_to_all_creatives)

    def input_creative_name(self, value):
        self.send_keys(self.name, value)

    def input_creative_concept(self, value):
        self.send_keys(self.concept, value)

    def select_size(self, value):
        self.select_option(self.size, value)

    def select_ad_type(self, value):
        self.select_option(self.type, value)

    def select_feature(self, value):
        self.select_option(self.feature, value)

    def input_url(self, value):
        self.send_keys(self.url, value)

    def select_offer(self, value):
        self.select_option(self.offer, value)

    def input_additional_urls(self, value):
        self.send_keys(self.additional_urls, value)

    def select_lang_targeting(self, value):
        self.select_option(self.lang_targeting, value)

    def input_start_date(self, value):
        self.send_keys(self.start_date, value)

    def input_end_date(self, value):
        self.send_keys(self.end_date, value)

    def click_add_server(self):
        self.click_element(self.add_server_button)

    def select_server(self, value):
        self.select_option(self.add_servers, value)

    def click_remove_server(self):
        self.click_element(self.remove_server)

    def select_is_flash(self, value):
        self.select_option(self.is_flash, value)

    def select_oba_placement(self, value):
        self.select_option(self.placement, value)

    def input_index(self, value):
        self.send_keys(self.z_index, value)

    def click_add_external_ids(self):
        self.click_element(self.add_external_id)

    def select_source(self, value):
        self.select_option(self.exteranl_id_source, value)

    def input_external_id(self, value):
        self.send_keys(self.exteranl_id, value)

    def click_remove_external_ids(self):
        self.click_element(self.remove_exteranl_id)

    def select_second_source(self, value):
        self.select_option(self.second_source, value)

    def input_second_external_id(self, value):
        self.send_keys(self.second_exteranl_id, value)

    def click_remove_second_external_ids(self):
        self.click_element(self.remove_second_exteranl_id)

    def click_new_add_on(self):
        self.click_element(self.new_add_on_button)

    def input_creative_add_on(self, value):
        self.fill_field(self.creative_add_on, value)

    def select_add_on_type(self, value):
        self.select_option(self.add_on_type, value)

    def click_remove_add_on(self):
        self.click_element(self.remove_add_on)

    def input_landing_url(self, value):
        self.send_keys(self.landing_url, value)

    def click_add_tracker(self):
        self.click_element(self.add_tracker_button)

    def select_tracker(self, value):
        self.select_option(self.tracker, value)

    def input_tracker_value(self, value):
        self.fill_field(self.tracker_value, value)

    def click_remove_tracker(self):
        self.click_element(self.remove_tracker)

    def click_cancel(self):
        self.click_element(self.cancel_button)

    def click_preview(self):
        self.click_element(self.preview_button)

    def click_save_creatives(self):
        self.click_element(self.submit_button)
        self.click_element(self.submit_button)

    def wait_for_update_form(self):
        self.wait_till_visible(self.update_form[0], self.update_form[1])

    def wait_for_errors(self):
        self.wait_till_visible(self.errors[0], self.errors[1])
