from base.dx import Dx
from selenium.webdriver.common.action_chains import ActionChains

class InventoryListPage(Dx):
    def click_on_organization_dropdown(self):
        self.click_element(self.advertiser_click)

    def fill_organization_text_box(self, advertiser_name):
        self.send_keys(self.advertiser_input, advertiser_name)

    def click_on_new_guaranteed_media_button(self):
        self.click_element(self.new_guaranteed_inventory_button)

    def enter_text_in_guaranteed_inventory_filterbox(self, guaranteed_inventory_name):
        self.type_search_string(self.guaranteed_inventory_filter, guaranteed_inventory_name)

    def click_on_guaranteed_inventory_publisher_name_link(self):
        self.click_element(self.guaranteed_inventory_publisher_name_link)

    def click_on_guaranteed_inventory_placement_name_link(self):
        self.click_element(self.guaranteed_inventory_placement_name_link)

    def click_on_guaranteed_inventory_gear_icon(self):
        self.click_element(self.guaranteed_inventory_gear_icon)

    def click_on_guaranteed_inventory_edit_link(self):
        self.click_element(self.guaranteed_inventory_edit_link)

    def click_on_guaranteed_inventory_export_tags_link(self):
        self.click_element(self.guaranteed_inventory_export_tags_link)

    def clik_on_guaranteed_inventory_publishername_header(self):
        self.click_element(self.guaranteed_inventory_publishername_header)

    def click_on_guaranteed_inventory_placementname_header(self):
        self.click_element(self.guaranteed_inventory_placementname_header)

    def click_on_guaranteed_inventory_media_size_max_duration_header(self):
        self.click_element(self.guaranteed_inventory_media_size_max_duration_header)

    def click_on_guaranteed_inventory_created_header(self):
        self.click_element(self.guaranteed_inventory_created_header)

    def click_on_guaranteed_inventory_pagination_next(self):
        self.click_element(self.guaranteed_inventory_pagination_next)

    def click_on_guaranteed_inventory_pagination_previous(self):
        self.click_element(self.guaranteed_inventory_pagination_previous)

    def select_count_from_guaranteed_inventory_pagination_dropdown(self, option, method='label'):
        self.select_option(self.guaranteed_inventory_pagination_dropdown, option, method)

    def click_on_deals_tab(self):
        self.click_element(self.deal_inventory_tab)

    def enter_text_in_deal_inventory_filterbox(self, deal_inventory_name):
        self.type_search_string(self.deal_inventory_filter, deal_inventory_name)

    def click_on_new_deal_button(self):
        self.click_element(self.new_deal_button)

    def click_on_deal_inventory_dealname_header(self):
        self.click_element(self.deal_inventory_dealname_header)

    def click_on_deal_inventory_dealid_header(self):
        self.click_element(self.deal_inventory_dealid_header)

    def click_on_deal_inventory_exchange_header(self):
        self.click_element(self.deal_inventory_exchange_header)

    def click_on_deal_inventory_cost_header(self):
        self.click_element(self.deal_inventory_cost_header)

    def click_on_deal_inventory_deal_type_header(self):
        self.click_element(self.deal_inventory_deal_type_header)

    def click_on_deal_inventory_dates_header(self):
        self.click_element(self.deal_inventory_dates_header)

    def click_on_deal_inventory_gear_icon(self):
        self.click_element(self.deal_inventory_gear_icon)

    def click_on_deal_inventory_edit_link(self):
        self.click_element(self.deal_inventory_edit_link)

    def select_count_from_deal_inventory_pagination_dropdown(self, option, method='label'):
        self.select_option(self.deal_inventory_pagination_dropdown, option, method)

    def click_on_deal_inventory_pagination_next(self):
        self.click_element(self.deal_inventory_pagination_next)

    def click_on_deal_inventory_pagination_previous(self):
        self.click_element(self.deal_inventory_pagination_previous)

    def click_on_custom_inventory_tab(self):
        self.click_element(self.custom_inventory_tab)

    def enter_text_in_custom_inventory_filterbox(self, custom_inventory_name):
        self.type_search_string(self.custom_inventory_filter, custom_inventory_name)

    def click_on_custom_inventory_publisher_name_link(self):
        self.click_element(self.custom_inventory_publisher_name_link)

    def click_on_custom_inventory_placement_name_link(self):
        self.click_element(self.custom_inventory_placement_name_link)

    def click_on_new_custom_inventory_button(self):
        self.click_element(self.new_custom_inventory_button)

    def click_on_custom_inventory_publishername_header(self):
        self.click_element(self.custom_inventory_publishername_header)

    def click_on_custom_inventory_placementname_header(self):
        self.click_element(self.custom_inventory_placementname_header)

    def click_on_custom_inventory_mediasizes_header(self):
        self.click_element(self.custom_inventory_mediasizes_header)

    def click_on_custom_inventory_created_header(self):
        self.click_element(self.custom_inventory_created_header)

    def click_on_custom_inventory_gear_icon(self):
        self.click_element(self.custom_inventory_gear_icon)

    def click_on_custom_inventory_edit_link(self):
        self.click_element(self.custom_inventory_edit_link)

    def select_count_from_custom_inventory_pagination_dropdown(self, option, method='label'):
        self.select_option(self.custom_inventory_pagination_dropdown, option, method)

    def click_on_custom_inventory_pagination_next(self):
        self.click_element(self.custom_inventory_pagination_next)

    def click_on_custom_inventory_pagination_previous(self):
        self.click_element(self.custom_inventory_pagination_previous)
