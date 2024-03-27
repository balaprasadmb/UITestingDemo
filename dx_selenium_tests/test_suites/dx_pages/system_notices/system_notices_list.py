from selenium.webdriver.support import expected_conditions as EC
from base.dx import Dx
import time

class SystemNoticesList(Dx):
    def filter_system_notices(self, search_string):
        self.fill_fields(self.filter_system_notices, search_string)

    def select_all_messages(self):
        self.click_element(self.select_all_messages)

    def click_on_new_system_message(self):
        self.go_to_link(self.new_system_message_link)
        time.sleep(3)
     
    def click_on_admin_link(self):
        self.go_to_link(self.admin_link)    
        
    def close_preview_popup(self):
        self.click_element(self.preview_popup)            
        
    def click_on_first_system_message(self):
        self.click_element(self.select_first_system_message_checkbox)
        
    def click_on_first_system_message_name(self):
        self.click_element(self.select_first_system_message_name)    

    def delete_selected_message(self):
        self.click_element(self.delete_selected_message_button)

    def preview_selected_message(self):
        self.click_element(self.preview_selected_message_button)
        
    def click_on_gear_icon(self):
        self.click_element(self.gear_icon)
        
    def click_on_edit_link(self):
        self.click_element(self.click_edit_link)
        
    def click_on_preview_link(self):
        self.click_element(self.click_preview_link)
        
    def click_on_delete_link(self):
        self.click_element(self.click_delete_link) 
        
    def click_on_clone_link(self):
        self.click_element(self.click_clone_link)   
        