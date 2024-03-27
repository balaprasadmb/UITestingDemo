from base.dx import Dx
from selenium.webdriver.common.keys import Keys

class CreateMediaPlan(Dx):
    
    def type_name(self, media_name):
        self.fill_field(self.name, media_name)
    
    def type_start_date(self, date):
        self.send_keys(self.start_date, date)
    
    def type_end_date(self, date):
        self.send_keys(self.end_date, date)
    
    def type_budget(self, budget):
        self.send_keys(self.budget, budget)
    
    def select_currency(self, currency):
        self.select_option(self.currency, currency)
    
    def select_attribution_model(self, value):
        self.select_option(self.attribution_model, value)
    
    def click_add_row(self):
        self.click_element(self.add_row)
    
    def select_activity(self, value):
        self.select_option(self.activity_pixel, value)
    
    def type_activity_filter(self, filter):
        self.fill_field(self.activity_filter, filter)
    
    def select_value_type(self, value):
        self.select_option(self.value_type, value)
    
    def type_value(self, value):
        self.send_keys(self.value, value)
    
    def remote_activity(self):
        self.click_element(self.delete_activity)
    
    def type_campaign_filter(self, filter):
        self.fill_field(self.campaign_filter, filter)
    
    def click_campaign_filter(self):
        self.click_element(self.campaign_filter)
    
    def click_select_all(self):
        self.click_element(self.master_select)
    
    def type_last_click(self, value):
        self.fill_field(self.last_click_input, value)
    
    def select_last_click(self, value):
        self.select_option(self.last_click_select, value)
    
    def type_last_view(self, value):
        self.fill_field(self.last_view_input, value)
    
    def select_last_view(self, value):
        self.select_option(self.last_view_select, value)
    
    def click_cancel(self):
        self.click_element(self.cancel)
    
    def click_submit(self):
        self.click_element(self.submit)
    
    def go_to_campaign_show_page(self):
        self.click_element(self.show_page_link)
