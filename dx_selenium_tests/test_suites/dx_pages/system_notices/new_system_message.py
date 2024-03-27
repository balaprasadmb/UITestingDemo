import uuid
import random
from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from system_notices.system_notices_list import SystemNoticesList
from base.dx import Dx

class NewSystemMessage(Dx):
    def fill_system_message_page(self, title, status='Draft', importance='High'):
        SystemNoticesList(self.driver).click_on_new_system_message()
        self.fill_title_textbox(title)
        self.select_status_from_dropdown(status)
        self.type_message_in_message_body('text test')
        self.select_importance_dropdown(importance)
        self.fill_external_link_text('yahoo')
        self.fill_external_link_url('www.yahoo.com')
        self.click_on_save_message_button()
        self.page_should_contain('Administration')
    
    def select_message_type_dropdown(self, option = 'Planned Outtage', method = 'label'):
        self.select_option(self.message_type, option, method)
        
    def click_on_message_type_dropdown(self):
        self.click_element(self.message_type)
    
    def select_display_to_users_dropdown(self, user = 'Agencies', method = 'label'):
        self.select_option(self.display_to_users, user, method)
        
    def click_on_start_date(self):
        self.click_element(self.start_date)
    
    def click_on_end_date(self):
        self.click_element(self.end_date)
        
    def fill_title_textbox(self, value):
        self.clear_and_send_value(value, self.title)
        
    def select_status_from_dropdown(self,  method):
        self.select_option(self.status, method)
        
    def type_message_in_message_body(self, message):
        self.clear_and_send_value(message, self.message_body)
        
    def select_importance_dropdown(self, method = 'label'):
        self.select_option(self.importance, method)
        
    def fill_external_link_text(self, value):
        self.clear_and_send_value(value, self.external_link_text)
        
    def fill_external_link_url(self, value):
        self.clear_and_send_value(value, self.external_link_url)
        
    def click_on_add_on_external_link(self):
        self.click_element(self.add_external_link)
        
    def click_on_save_message_button(self):
        self.click_element(self.save_message)
                   
    def click_on_cancel_button(self):
        self.click_element(self.cancel)
        
    def click_on_delete_icon(self):
        self.click_element(self.delete_icon)

        