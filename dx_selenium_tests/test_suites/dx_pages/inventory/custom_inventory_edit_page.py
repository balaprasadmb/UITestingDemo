from base.dx import Dx

class CustomInventoryEditPage(Dx):
    def click_on_custom_inventory_link(self):
        self.click_element(self.custom_inventory_link)
    
    def enter_custom_inventory_publisher_name(self, publisher_name):
        self.clear_and_send_value(publisher_name, self.custom_inventory_publisher_name)
    
    def enter_custom_inventory_placement_name(self, placement_name):
        self.clear_and_send_value(placement_name, self.custom_inventory_placement_name)
    
    def click_on_custom_inventory_available_checkbox(self):
        self.click_element(self.custom_inventory_available_checkbox)
    
    def click_on_custom_inventory_secure_checkbox(self):
        self.click_element(self.custom_inventory_secure_checkbox)
    
    def select_custom_inventory_media_type(self, option, method = 'label'):
        self.select_option(self.custom_inventory_media_type_dropdown, option, method)
    
    def select_custom_inventory_tag_type(self, option, method = 'label'):
        self.select_option(self.custom_inventory_tag_type, option, method)
    
    def select_custom_inventory_size(self, option, method = 'label'):
        self.select_option(self.custom_inventory_size, option, method)
    
    def click_on_custom_inventory_not_assigned_link(self):
        self.click_element(self.custom_inventory_not_assigned_link)
    
    def click_on_custom_inventory_remove_creative_size_button(self):
        self.click_element(self.custom_inventory_remove_creative_size_button)
    
    def click_on_custom_inventory_add_another_size_button(self):
        self.click_element(self.custom_inventory_add_another_size_button)
    
    def click_on_custom_inventory_budget_section_header(self):
        self.click_element(self.custom_inventory_budget_section_header)
    
    def select_custom_inventory_currency(self, option, method = 'label'):
        self.select_option(self.custom_inventory_currency_dropdown, option, method)
    
    def enter_custom_inventory_budget(self, custom_inventory_budget):
        self.clear_and_send_value(custom_inventory_budget, self.custom_inventory_budget_textbox)
        
    def enter_custom_inventory_cost(self, custom_inventory_cost):
        self.clear_and_send_value(custom_inventory_cost, self.custom_inventory_cost_textbox)
        
    def click_on_custom_inventory_cancel_button(self):
        click_element(self.custom_inventory_cancel_button)
    
    def click_on_save_custom_inventory_button(self):
        click_element(self.save_custom_inventory_button)
