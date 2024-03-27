from selenium.webdriver.common.by import By
from base.dx import Dx
from configs.dx_constant import DXConstant
import time

class NewAgencyGroup(Dx):
    def fill_fields(self, agency_group_attribute):
        self.type_organization_name(agency_group_attribute["organization_name"])
        self.type_email(agency_group_attribute["email"])
        self.type_contact_name(agency_group_attribute["contact_name"])
        self.check_select_all_currencies()
        self.type_add_on_cost_name(agency_group_attribute["add_on_cost_name"])
        self.upload_rate_card(agency_group_attribute["rate_card"])
        self.type_add_on_cost_rate(agency_group_attribute["add_on_cost_value"])
        self.click_create_agency_group_button()
        time.sleep(2)
        self.accept_add_on_cost_pop_up()
        return self

    def type_organization_name(self, organization):
        self.clear_and_send_value(organization, self.agency_group_name)

    def type_contact_name(self, contact_name):
        self.clear_and_send_value(contact_name, self.contact_name)

    def select_currency_from_listbox(self, currency='United States Dollar (USD)', method='label'):
        self.select_option(self.currency, currency, method)

    def check_select_all_currencies(self):
        self.click_element(self.select_all_currency)

    def select_currency_using_checkbox(self, currencies):
        currency_code_dict = DXConstant().agency_group_currency_code
        if type(currencies) is list:
            for currency in currencies:
                loc = (By.ID, "agency_group_organization_attributes_currency_ids_{0}".format(currency_code_dict[currency]))
                self.click_element(loc)
        if type(currencies) is str:
            loc = (By.ID, "agency_group_organization_attributes_currency_ids_{0}".format(currency_code_dict[currencies]))
            self.click_element(loc)

    def click_cogs_inherited_value_checkbox(self):
        self.click_element(self.cogs_inherited_value_checkbox)

    def click_margin_inherited_value_checkbox(self):
        self.click_element(self.margin_inherited_value_checkbox)

    def type_cogs_value(self, value):
        self.clear_and_send_value(value, self.cogs_inherited_value_textbox)

    def type_margin_value(self, value):
        self.clear_and_send_value(value, self.margin_inherited_value_textbox)

    def click_new_add_on_cost_button(self):
        self.click_element(self.new_add_on_cost)

    def type_add_on_cost_name(self, name):
        element = self.get_last_element(self.add_on_cost_name)
        self.clear_and_send_value(name, element)

    def type_add_on_cost_rate(self, rate):
        element = self.get_last_element(self.add_on_cost_value)
        self.clear_and_send_value(rate, element)

    def select_add_on_cost_fee_type(self, fee_type, method='label'):
        element = self.get_last_element(self.add_on_cost_fee_type)
        self.select_option(element, fee_type, method)

    def click_add_on_cost_billable_checkbox(self):
        element = self.get_last_element(self.add_on_cost_billable_checkbox)
        element.click()

    def click_marketlace_checkbox(self):
        element = self.get_last_element(self.add_on_cost_marketplace_checkbox)
        element.click()

    def click_dataxu_controlled_checkbox(self):
        element = self.get_last_element(self.add_on_cost_dataxu_controlled_checkbox)
        element.click()

    def click_add_on_cost_channel(self, channel, method='label'):
        element = self.get_last_element(self.add_on_cost_channel)
        self.select_option(element, channel, method)

    def remove_add_on_cost_functionality(self):
        element = self.get_last_element(self.remove_add_on_cost)
        element.click()

    def upload_rate_card(self, file_path):
        self.uplaod_file(file_path, self.rate_card)

    def click_inherit_licenses_checkbox(self):
        self.click_element(self.inherit_licensing_checkbox)

    def click_media_type_checkbox(self, media_type='Mobile'):
        self.click_element(self.online_media_type_checkbox[media_type.lower()].values())

    def select_all_inventory(self):
        self.click_element(self.select_all_inventories)

    def select_inventories(self, inventories):
        if type(inventories) is list:
            for inventory in inventories:
                loc = (By.CSS_SELECTOR, "input[data-inventory_supplier_name='{0}']".format(inventory))
                self.click_element(loc)
        if type(inventories) is str:
            loc = (By.CSS_SELECTOR, "input[data-inventory_supplier_name='{0}']".format(inventories))
            self.click_element(loc)

    def click_targeting_checkbox(self):
        self.click_element(self.geo_targeting_checkbox)

    def click_cost_model_type(self, cost_model):
        if cost_model == 'CPA':
            self.click_element(self.cost_model_type)

    def select_insights(self, insight='Frequency Impact Report'):
        insight_dict = {
            'Frequency Impact Report': 'frequency',
            'Consideration Period Report': 'consideration',
            'Retargeting Effectiveness Report': 'retargeting',
            'Index of Best Metrocodes': 'index'
        }
        self.click_element(self.insights[insight_dict[insight]].values())

    def click_create_agency_group_button(self):
        self.click_element(self.submit_button)

    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def accept_add_on_cost_pop_up(self):
        if self.is_element_present(self.add_on_cost_modified_pop_up['pop_up'].values()):
            self.click_element(self.add_on_cost_modified_pop_up['accept'].values())

    def decline_add_on_cost_pop_up(self):
        if self.is_element_present(self.add_on_cost_modified_pop_up['pop_up'].values()):
            self.click_element(self.add_on_cost_modified_pop_up['cancel'].values())

    def click_seats_edit_icon(self):
        self.click_element(self.edit_configure_seat)

    def click_seats_cancel_button(self):
        self.click_element(self.configure_seats_pop_up['cancel_button'].values())

    def click_seats_ok_button(self):
        self.click_element(self.configure_seats_pop_up['ok_button'].values())

    def type_seat_name(self, value):
        self.clear_and_send_value(value, self.configure_seats_pop_up['seat_name'].values())

    def type_seat_id(self, value):
        self.clear_and_send_value(value, self.configure_seats_pop_up['seat_id'].values())

    def click_seats_billable_checkbox(self):
        self.click_element(self.configure_seats_pop_up['seat_billable'].values())

    def add_seats(self):
        self.click_element(self.configure_seats_pop_up['add_seat'].values())

    def remove_seats(self):
        self.click_element(self.configure_seats_pop_up['remove_seat'].values())

    def click_seats_inherit_radio_button(self):
        self.click_element(self.configure_seats_pop_up['inherit_checkbox'].values())

    def click_seats_override_radio_button(self):
        self.click_element(self.configure_seats_pop_up['override_checkbox'].values())