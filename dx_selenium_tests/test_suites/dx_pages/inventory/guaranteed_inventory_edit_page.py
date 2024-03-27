from base.dx import Dx
from selenium.webdriver.support.ui import Select

class GuaranteedInventoryEditPage(Dx):
    def click_on_guaranteed_inventory_link(self):
        self.click_element(self.guaranteed_inventory_link)
    
    def enter_guaranteed_inventory_publisher_name(self, publisher_name):
        self.clear_and_send_value(publisher_name, self.guaranteed_inventory_publisher_name)
    
    def enter_guaranteed_inventory_placement_name(self, placement_name):
        self.clear_and_send_value(placement_name, self.guaranteed_inventory_placement_name)
    
    def click_on_guaranteed_inventory_available_checkbox(self):
        self.click_element(self.guaranteed_inventory_available_checkbox)
    
    def click_on_guaranteed_inventory_secure_checkbox(self):
        self.click_element(self.guaranteed_inventory_secure_checkbox)
    
    def select_guaranteed_inventory_media_type(self, option, method = 'label'):
        self.select_option(self.guaranteed_inventory_media_type_dropdown, option, method)
        
    def select_guaranteed_inventory_tag_type(self, option, method = 'label'):
        self.select_option(self.guaranteed_inventory_tag_type_dropdown, option, method)
    
    def select_guaranteed_inventory_tag_size(self, option, method = 'label'):
        self.select_option(self.guaranteed_inventory_tag_size_dropdown, option, method)
    
    def click_on_guaranteed_inventory_none_assigned_link(self):
        self.click_element(self.guaranteed_inventory_not_assigned_link01)
    
    def click_on_close_button_from_assign_creative_popup(self):
        self.click_element(self.guaranteed_inventory_creative_popup_close_button)
    
    def click_on_guaranteed_inventory_add_another_size_button(self):
        self.click_element(self.guaranteed_inventory_add_another_size_button)
    
    def click_on_guaranteed_inventory_remove_creative_size_button(self):
        self.click_element(self.guaranteed_inventory_remove_creative_size_button01)
    
    def click_on_guaranteed_inventory_budget_section_header(self):
        self.click_element(self.guaranteed_inventory_budget_section_header)
    
    def select_guaranteed_inventory_currency(self, option, method = 'label'):
        self.select_option(self.guaranteed_inventory_currency_dropdown, option, method)
    
    def enter_guaranteed_inventory_budget(self, guaranteed_inventory_budget):
        self.clear_and_send_value(guaranteed_inventory_budget, self.guaranteed_inventory_budget_textbox)
    
    def enter_guaranteed_inventory_cost(self, guaranteed_inventory_cost):
        self.clear_and_send_value(guaranteed_inventory_cost, self.guaranteed_inventory_cost_textbox)
    
    def click_on_guaranteed_inventory_cancel_button(self):
        self.click_element(self.guaranteed_inventory_cancel_button)
    
    def click_on_guaranteed_inventory_save_button(self):
        self.click_element(self.guaranteed_inventory_save_button)
        
    def check_dropdown_options(self, option_list, loc):
        select = Select(self.find_element(loc))
        options_text = []
        for opt in select.options:
            options_text.append(opt.text.encode())
        opt_string = ','.join(options_text)
        for option in option_list:
            assert option in opt_string, "Actaul/Obtained list :- {0}/{1}".format(option, options_text)
