from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.dx import Dx
import time
class CreateFlight(Dx):

    def fill_fields(self , flight_attributes):
        self.expand_lang_targeting()
        self.click_separate_language_targeting()
        self.select_lang_targeting()
        self.click_move_selected_lang()
        self.expand_geo_targeting()
        self.click_separate_geo_targeting()
        self.select_avail_countries()
        self.click_move_selected_country()
        self.expand_blacklist()
        self.select_use_new_blacklist()
        self.enter_blacklist(flight_attributes['blacklist_url'])
        self.expand_whitelist()
        self.select_use_new_whitelist()
        self.enter_whitelist(flight_attributes['whitelist_url'])
        self.click_save_exit()

    def fill_fields_validation(self, flight_attributes_validation):
        self.type_start_date(flight_attributes_validation['start_date'])
        self.type_end_date(flight_attributes_validation['end_date'])
        self.enter_default_bid(flight_attributes_validation['deafault_bid_usd'])
        self.enter_budget_usd(flight_attributes_validation['Budget_usd'])
        self.click_save_exit()

    def edit_flight_description(self, flight_description):
        self.clear_description_filter()
        self.type_in_edit_description_filter(flight_description)
        self.click_save_and_continue()

    def expand_add_on_cost(self):
        self.wait_till_visible('id', 'flight_description')
        element = self.find_element(self.new_add_on_cost)
        if not element.is_displayed():
            self.click_element(self.add_on_cost_expand)

    def type_in_edit_description_filter(self, description):
        self.fill_field(self.edit_flight_name, description)

    def clear_description_filter(self):
        self.clear(self.edit_flight_name)

    def select_tactic(self, value):
        self.select_option(self.flight_tactic, value)

    def type_start_date(self, value):
        self.send_keys(self.start_date, value)

    def type_end_date(self, value):
        self.send_keys(self.end_date, value)

    def enter_default_bid(self, values):
        self.send_keys(self.deafault_bid_usd, values)

    def enter_budget_usd(self, values): 
        self.send_keys(self.budget_usd, values)

    def enter_allocated_percentage(self, values):
        self.send_keys(self.alloc, values)

    def expand_inventory(self):
        self.click_element(self.inventory_targeting)

    def select_creative_type(self, value):
        self.select_option(self.creative_type, value)

    def select_available_inventory(self, value):
        self.select_option(self.avail_inventory, value)

    def select_applied_inventory(self, value):
        self.select_option(self.applied_inventory, value)

    def move_selected_inventory(self):
        self.click_element(self.move_select_inventory)

    def remove_selected_inventory(self):
        self.click_element(self.remove_select_inventory)

    def move_all_selected_inventory(self):
        self.click_element(self.move_all_inventory)

    def remove_all_selected_inventory(self):
        self.click_element(self.remove_all_inventory)

    def expand_deals(self):
        self.click_element(self.deals)

    def filter_deals(self, value):
        self.send_keys(self.deals_filters, value)
        self.fill_field(self.deals_filters, Keys.ENTER)

    def click_master_select(self):
        self.click_element(self.master_select_deals)

    def click_select_first_deal(self):
        self.click_element(self.select_first_deal)

    def click_new_aoc(self):
        self.click_element(self.new_add_on_cost)

    def select_aoc_name(self, value):
        self.select_option(self.add_on_cost_name, value)

    def enter_aoc_rate(self, value):
        self.fill_field(self.add_on_cost_rate, value)

    def select_fee_type(self, value):
        self.select_option(self.add_on_cost_fee_type, value)

    def click_billable(self):
        self.click_element(self.add_on_cost_billable)

    def click_is_marketplace(self):
        self.click_element(self.add_on_cost_marketplace)

    def click_on_aoc_remove_button(self):
        self.click_element(self.aoc_remove_button)

    def expand_private_inventory(self):
        self.click_element(self.private_inventory)

    def select_first_private_inventory(self):
        self.click_element(self.first_private_inventory)

    def expand_lang_targeting(self):
        self.click_element(self.lang_targeting)

    def click_separate_language_targeting(self):
        self.click_element(self.separate_language_targeting)

    def select_lang_targeting(self):
        self.click_element(self.select_first_lang)

    def click_move_selected_lang(self):
        self.click_element(self.move_selected_lang)

    def click_remove_selected_lang(self):
        self.click_element(self.remove_selected_lang)

    def click_move_all_selected_lang(self):
        self.click_element(self.move_all_selected_lang)

    def click_remove_all_selected_lang(self):
        self.click_element(self.remove_all_selected_lang)

    def expand_geo_targeting(self):
        self.click_element(self.geographic_targeting)

    def click_separate_geo_targeting(self):
        self.click_element(self.separate_geo_targeting)

    def select_selected_countries(self, value):
        self.click_element(self.country_selected, value)

    def click_move_selected_country(self):
        self.click_element(self.move_selected_country)

    def click_remove_selected_country(self):
        self.click_element(self.remove_selected_country)

    def click_move_all_selected_countries(self):
        self.click_element(self.move_all_selected_country)

    def click_remove_all_selected_countries(self):
        self.click_element(self.remove_all_selected_country)

    def select_avail_countries(self):
        self.click_element(self.country_first_select)

    def expand_whitelist(self):
        self.click_element(self.whitelist)

    def select_use_new_whitelist(self):
        self.click_element(self.new_whitelist)

    def upload_whitelist(self, value):
        self.fill_field(self.whitelist_file, value)

    def enter_whitelist(self, value):
        self.fill_field(self.whitelist_domains, value)

    def select_do_not_use_whitelist(self):
        self.click_element(self.no_whitelist)

    def expand_blacklist(self):
        self.click_element(self.blacklist)

    def select_use_new_blacklist(self):
        self.click_element(self.new_blacklist)

    def upload_blacklist(self, value):
        self.fill_field(self.blacklist_file, value)

    def enter_blacklist(self, value):
        self.fill_field(self.blacklist_domains, value)

    def select_do_not_use_blacklist(self):
        self.click_element(self.no_blacklist)

    def click_close_popup(self):
        self.click_element(self.close_popup)

    def expand_audience_targeting(self):
        self.click_element(self.audience_targeting)

    def click_save_exit(self):
        self.click_element(self.save_and_exit)

    def click_save_and_continue(self):
        self.click_element(self.save_and_continue)    

    def select_preferred_placement(self , value):
        self.select_option(self.preferred_placement, value)

    def wait_for_flight_details(self):
        self.wait_till_visible(self.flight_details[0], self.flight_details[1], 30)

    def get_filtered_search(self, element):
        element = self.find_element(getattr(self, element))
        search_text = str(element.get_attribute('innerHTML'))
        search_text = search_text.replace('<wbr>', '')
        return search_text

    def do_hover(self):
        element = self.find_element(self.inventory_suppliers)
        ActionChains(self.driver).move_to_element(element)

    def get_inventory(self, element, count = 1):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            if count == 1:
                return option.text
            else:
                selected.append(option.text)
        return selected

    def click_single_device(self):
        self.click_element(self.single_device_enabled)

    def click_high_precision(self):
        self.click_element(self.high_precision_enabled)

    def click_broad_reach(self):
        self.click_element(self.broad_reach_enabled)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)
