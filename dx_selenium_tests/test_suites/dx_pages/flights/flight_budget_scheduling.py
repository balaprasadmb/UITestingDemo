from base.dx import Dx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class FBSPage(Dx):
    def select_all_flights(self):
        self.click_element(self.select_all_flights_checkbox)

    def type_in_description_filter(self, description):
        self.fill_field(self.description_filter, description)
        
    def clear_description_filter(self):
        self.clear(self.description_filter)    

    def select_tactic_filter(self, tactic_option= 'Filter by tactic', method='label'):
        self.select_option(self.tactic_filter, tactic_option, method)

    def select_flight_type_filter(self, option, method='label'):
        self.select_option(self.flight_type_filter, option, method)

    def select_algorithm_filter(self, option='Filter by decision algorithm', method='label'):
        self.select_option(self.algorithm_filter, option, method)

    def select_status_filter(self, option='Filter by status', method='label'):
        self.select_option(self.status_filter, option, method)

    def select_single_flight(self, index=1):
        element = self.get_element_by_index(index, self.select_single_flight)
        element.click()

    def fill_description(self, description):
        self.wait_till_visible('css' , 'input.ember-view.ember-text-field.flight_name.text');
        element = self.get_last_element(self.flight_description)
        self.clear_and_send_value(description,element)

    def select_tactic(self, tactic):
        element = self.get_last_element(self.flight_tactic_listbox["link"].values())
        element.click()
        element = self.get_last_element(self.flight_tactic_listbox["textbox"].values())
        element.send_keys(tactic)
        self.press_enter_key(element)

    def select_flight_type(self, flight_type):
        element = self.get_last_element(self.flight_type_listbox["link"].values())
        element.click()
        element = self.get_last_element(self.flight_type_listbox["textbox"].values())
        element.send_keys(flight_type)
        self.press_enter_key(element)

    def select_decision_algorithm(self, algorithm):
        element = self.get_last_element(self.flight_algorithm_listbox["link"].values())
        element.click()
        element = self.get_last_element(self.flight_algorithm_listbox["textbox"].values())
        element.send_keys(algorithm)
        self.press_enter_key(element)

    def type_start_date(self, date):
        element = self.get_last_element(self.start_date.values())
        self.clear_and_send_value(date, element)

    def type_end_date(self, date):
        element = self.get_last_element(self.end_date.values())
        self.clear_and_send_value(date, element)

    def type_frequency_cap(self, value):
        element = self.get_last_element(self.frequency_cap)
        self.clear_and_send_value(value, element)
        
    def type_single_frequency_cap(self, value): 
        self.clear_and_send_value(value, self.single_frequency_cap)

    def type_impressions(self, value):
        element = self.get_last_element(self.impressions)
        self.clear_and_send_value(value, element)
        
    def select_frequency_type_dropdown(self):
        self.click_element(self.select_frequency_type)

    def select_frequency_types(self, type="hour"):
        type_dict = {
                    'hour': 'hours',
                    'day': 'days',
                    'week': 'weeks',
                    'flight_duration': 'flight_duration'
                    }
        element = self.get_last_element(self.frequency_type_listbox[type_dict[type]].values())
        element.click()

    def type_bid(self, bid):
        element = self.get_last_element(self.bid)
        self.clear_and_send_value(bid, element)
        time.sleep(3)
        element.send_keys(Keys.TAB)

    def type_bid_enter(self, bid):
        element = self.get_last_element(self.bid)
        self.clear_and_send_value(bid, element)
        time.sleep(2)
        element.send_keys(Keys.ENTER)

    def type_bid_normal(self , bid):
        self.fill_field(self.bid, bid)
        time.sleep(1)
        self.fill_field(self.bid , Keys.TAB)

    def type_day_cap(self, value):
        element = self.get_last_element(self.day_cap)
        self.clear_and_send_value(value, element)

    def type_budget(self, value):
        element = self.get_last_element(self.budget)
        self.clear_and_send_value(value, element)

    def type_budget_enter(self, value):
        element = self.get_last_element(self.budget)
        self.clear_and_send_value(value, element)
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        
    def clear_budget_field(self):
        element = self.get_last_element(self.budget)
        element.clear()

    def type_allocated_percent(self, value):
        element = self.get_last_element(self.percent_allocated)
        self.clear_and_send_value(value, element)
        element.send_keys(Keys.TAB)
        time.sleep(1)

    def click_on_add_flight(self):
        self.click_element(self.add_flight)

    def click_on_edit_selected(self):
        self.click_element(self.edit_selected)

    def copy_flight(self, index=1):
        element = self.get_element_by_index(index, self.copy_flight)
        element.click()

    def delete_flight(self, index=1):
        element = self.get_element_by_index(index, self.delete_flight)
        element.click()

    def click_on_cancel(self):
        self.click_element(self.cancel_button)

    def click_on_save_exit(self):
        self.click_element(self.save_exit_button)

    def click_on_save_continue(self):
        self.click_element(self.save_continue_button)

    def click_on_tactic_checkbox(self):
        self.click_element(self.edit_flight_popup_tactic_checkbox)

    def select_tactic_on_pop_up(self, option='Default', method='label'):
        self.select_option(self.edit_flight_popup_tactic, option, method)

    def click_on_start_date_checkbox(self):
        self.click_element(self.edit_flight_popup_start_date_checkbox)

    def type_pop_up_start_date(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_start_date)

    def click_on_end_date_checkbox(self):
        self.click_element(self.edit_flight_popup_end_date_checkbox)

    def type_pop_up_end_date(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_end_date)

    def click_on_algorithm_checkbox(self):
        self.click_element(self.edit_flight_popup_algorithm_checkbox)

    def select_algorithm_on_pop_up(self, option='Default', method='label'):
        element = self.get_last_element(self.edit_flight_popup_algorithm["link"].values())
        element.click()
        element = self.get_last_element(self.edit_flight_popup_algorithm["textbox"].values())
        element.send_keys(option)
        self.press_enter_key(element)

    def click_pop_up_bid_checkbox(self):
        self.click_element(self.edit_flight_popup_bid_checkbox)

    def type_pop_up_bid(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_bid)

    def click_pop_up_budget_checkbox(self):
        self.click_element(self.edit_flight_popup_budget_checkbox)

    def type_pop_up_budget(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_budget)

    def click_pop_up_percent_allocated_checkbox(self):
        self.click_element(self.edit_flight_popup_percent_allocated_checkbox)

    def type_pop_up_percent_allocated(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_percent_allocated)

    def click_pop_up_day_cap_checkbox(self):
        self.click_element(self.edit_flight_popup_day_cap_checkbox)

    def type_pop_up_day_cap(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_day_cap)

    def click_pop_up_frequency_cap_checkbox(self):
        self.click_element(self.edit_flight_popup_frequency_cap_checkbox)

    def type_pop_up_frequency_cap(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_frequency_cap)

    def type_pop_up_impressions(self, value):
        self.clear_and_send_value(value, self.edit_flight_popup_impressions)

    def select_frequency_type_on_pop_up(self, option='Hour(s)', method='label'):
        self.select_option(self.edit_flight_popup_frequency_type, option, method)

    def click_on_update_flight_button(self):
        self.click_element(self.update_flights)

    def click_on_cancel_button(self):
        self.click_element(self.cancel_button)

    def select_first_flight(self, index=1):
        self.click_element(self.select_single_flight)

    def wait_for_flights(self):
        self.wait_till_visible(self.flights_row[0], self.flights_row[1], 30)
