from base.dx import Dx

class DealInventoryEditPage(Dx):
    def click_on_deals_link(self):
        self.click_element(self.deals_link)
    
    def enter_deal_name(self, deal_name):
        self.clear_and_send_value(deal_name, self.deal_name)
    
    def select_deal_inventory_exchange(self, option, method='index'):
        self.select_option(self.exchange_dropdown, option, method)
    
    def enter_deal_id(self, deal_id):
        self.clear_and_send_value(deal_id, self.deal_id)
    
    def select_deal_type(self, option, method='index'):
        self.select_option(self.deal_type_dropdown, option, method)
    
    def select_deal_currency(self, option, method='label'):
        self.select_option(self.deal_currency, option, method)
    
    def enter_cost_cpm_value(self, cost_cpm):
        self.clear_and_send_value(cost_cpm, self.deal_cost_cpm_value)
    
    def enter_start_date(self, start_date):
        self.clear_and_send_value(start_date, self.deal_start_date)
    
    def enter_end_date(self, end_date):
        self.clear_and_send_value(end_date, self.deal_end_date)
    
    def enter_deal_description(self, description):
        self.clear_and_send_value(description, self.deal_description)

    def enter_deal_permissioned_agency_group_name(self, agency_group_name):
        self.send_keys(self.deal_permissioned_agency_group_name, agency_group_name)
    
    def enter_deal_permissioned_agency_name(self, agency_name):
        self.send_keys(self.deal_permissioned_agency_name, agency_name)
        
    def enter_deal_permissioned_advertiser_name(self, advertiser_name):
        self.send_keys(self.deal_permissioned_advertiser_name, advertiser_name)
        
    def click_on_deal_cancel_button(self):
        self.click_element(self.deal_cancel_button)
        
    def click_on_save_deal_button(self):
        self.click_element(self.save_deal_button)
