from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from system_notices.system_notices_list import SystemNoticesList
from system_notices.edit_system_notices import EditSystemNotices
from system_notices.new_system_message import NewSystemMessage
from admin_page import AdminPage
import time

class SystemNoticesTest(DXTest):
    @test_case()
    def goto_system_notices_list(self):
        self.system_notices_list_page = SystemNoticesList(self.driver.get_browser())
        self.edit_system_notices = EditSystemNotices(self.driver.get_browser())
        self.new_system_notices_page = NewSystemMessage(self.driver.get_browser())
        self.admin_page = AdminPage(self.driver.get_browser())

    @test_case()
    def validate_system_notices_page_content(self):
        for content in self.system_notices_list_page.system_message_list_contents.values():
            self.system_notices_list_page.page_should_contain(content)
     
    @test_case()
    def functionality_of_new_system_message(self):
        self.system_notices_list_page.click_on_new_system_message()
        self.system_notices_list_page.page_should_contain("Create System Message")
        self.system_notices_list_page.go_back()
        time.sleep(2)
    
    @test_case()
    def check_gear_icon_list(self):
        self.system_notices_list_page.click_on_gear_icon()
        element_list = self.system_notices_list_page.gear_icon_system_message
        for element in element_list:
            assert self.system_notices_list_page.is_element_present(["link text", element])
            
    @test_case()
    def check_functionality_name_link(self):
        self.system_notices_list_page.click_on_first_system_message_name()
        self.edit_system_notices.wait_till_visible(self.edit_system_notices.cancel_button[0],
                                                   self.edit_system_notices.cancel_button[1])
        self.edit_system_notices.page_should_contain("View System Message")
        self.system_notices_list_page.go_back()
    
    @test_case()
    def check_functionality_of_edit_link(self):
        self.system_notices_list_page.click_on_edit_link()
        self.system_notices_list_page.page_should_contain("Edit System Message")
        self.system_notices_list_page.go_back()
    
    @test_case()
    def check_functionality_of_preview_link(self):
        self.system_notices_list_page.click_on_gear_icon()
        self.system_notices_list_page.click_on_preview_link()
        self.system_notices_list_page.is_element_present(self.system_notices_list_page.preview_popup_content)
        self.system_notices_list_page.close_preview_popup()
    
    @test_case()
    def check_functionality_of_delete_link(self):
        self.system_notices_list_page.click_on_delete_link()
        self.system_notices_list_page.dismiss_alert()
        self.system_notices_list_page.page_should_contain("Administration")
        self.system_notices_list_page.click_on_gear_icon()
        self.system_notices_list_page.click_on_delete_link()
        self.system_notices_list_page.accept_alert()
        self.system_notices_list_page.page_should_contain("Successfully Destroyed System Message")
    
    @test_case()
    def check_functionality_of_clone_link(self):
        self.system_notices_list_page.click_on_gear_icon()
        self.system_notices_list_page.click_on_clone_link()
        self.edit_system_notices.wait_till_visible(self.edit_system_notices.save_message_button[0],
                                                   self.edit_system_notices.save_message_button[1])
        self.edit_system_notices.page_should_contain("Create System Message")
        self.system_notices_list_page.click_on_admin_link()
        self.admin_page.wait_till_visible(self.admin_page.system_message_table[0],
                                          self.admin_page.system_message_table[1])
    
    @test_case()
    def check_functionality_of_delete_button(self):
        self.system_notices_list_page.click_on_first_system_message()
        self.system_notices_list_page.delete_selected_message_button()
        self.system_notices_list_page.dismiss_alert()
        self.system_notices_list_page.page_should_contain("Administration")
        self.system_notices_list_page.accept_alert()
        self.system_notices_list_page.page_should_contain("Successfully Destroyed System Message")
    
    @test_case()
    def check_functionality_of_edit_button_from_show_page(self):
        self.system_notices_list_page.click_on_first_system_message_name()
        self.edit_system_notices.wait_till_visible(self.edit_system_notices.cancel_button[0],
                                                   self.edit_system_notices.cancel_button[1])
        self.edit_system_notices.click_on_edit_button()
        self.edit_system_notices.wait_till_visible(self.edit_system_notices.save_message_button[0],
                                                   self.edit_system_notices.save_message_button[1])
        self.edit_system_notices.page_should_contain("Edit System Message")
        self.system_notices_list_page.click_on_admin_link()
        self.admin_page.wait_till_visible(self.admin_page.system_message_table[0],
                                          self.admin_page.system_message_table[1])
    
    @test_case()
    def check_functionality_of_cancel_button_from_show_page(self):
        self.system_notices_list_page.click_on_first_system_message_name()
        self.edit_system_notices.wait_till_visible(self.edit_system_notices.cancel_button[0],
                                                   self.edit_system_notices.cancel_button[1])
        self.edit_system_notices.click_on_cancel_button()
        self.admin_page.wait_till_visible(self.admin_page.system_message_table[0],
                                          self.admin_page.system_message_table[1])
        self.system_notices_list_page.page_should_contain("Administration")
    
    @test_case()
    def check_content_of_new_message_page(self):
        self.system_notices_list_page.click_on_new_system_message()
        for content in self.system_notices_list_page.create_system_message_content:
            self.system_notices_list_page.page_should_contain(content)
        new_system_message_content = ["cancel", "save_message", "add_external_link"]
        for button_name in new_system_message_content:
            assert self.new_system_notices_page.is_element_present(getattr(self.new_system_notices_page, button_name))
        self.system_notices_list_page.click_on_admin_link()
        self.admin_page.wait_till_visible(self.admin_page.system_message_table[0],
                                          self.admin_page.system_message_table[1])

    @test_case()
    def check_functionality_of_message_type_dropdown(self):
        self.system_notices_list_page.click_on_new_system_message()
        self.new_system_notices_page.click_on_message_type_dropdown()
        for message_type in new_system_notices_page.message_type:
            self.new_system_notices_page.page_should_contain(message_type)
        for message_type_option in ['Planned Outage', 'Reporting Delays', 'Reporting Delays Resolved', 'Other']:
            self.new_system_notices_page.select_message_type_dropdown(message_type_option)
            expected_result = ["draft", "1", "all_users"]
            if message_type_option == "Planned Outage":
                expected_result = expected_result
            elif message_type_option == "Other":
                expected_result[1] = "0"
                expected_result[2] = "agency_groups"
            else:
                expected_result[2] = "agency_groups"
            for element in ["status", "importance", "display_to_users"]:            
                assert self.new_system_notices_page.get_content_value(getattr(self.new_system_notices_page, element)) in expected_result 
            dx_date_object = DXDate()
            date_value = [dx_date_object.todays_date(), dx_date_object.date_after_one_month()]
            for date_control in ["start_date", "end_date"]:
                assert self.new_system_notices_page.get_content_value(getattr(self.new_system_notices_page, date_control)) in date_value
        self.system_notices_list_page.click_on_admin_link()
        self.admin_page.wait_till_visible(self.admin_page.system_message_table[0],
                                          self.admin_page.system_message_table[1])
        
    @test_case()
    def check_functionality_of_message_box(self):
        self.system_notices_list_page.click_on_new_system_message()
        obj_dx_constant = DXConstant()
        for element in ['alphanumeric_value', 'special_char', 'strings', 'html_tag']:
            self.new_system_notices_page.fill_title_textbox(getattr(obj_dx_constant, element))
            data = self.new_system_notices_page.get_content_value(self.new_system_notices_page.title)
            assert data == getattr(obj_dx_constant, element), data
            
    @test_case()
    def check_functionality_of_status_on_new_message_page(self):   
        self.system_notices_list_page.click_on_admin_link()
        self.system_notices_list_page.click_on_new_system_message()
        self.new_system_notices_page.fill_title_textbox("test")
        importance='High'
        for option in ['Draft', 'Paused', 'Running']:                       
            self.new_system_notices_page.select_status_from_dropdown(option)
            self.new_system_notices_page.click_on_save_message_button()
            self.system_notices_list_page.click_on_new_system_message()
            
    @test_case()
    def check_functionality_of_message_text_box(self):
        self.system_notices_list_page.click_on_admin_link()
        self.system_notices_list_page.click_on_new_system_message()
        obj_dx_constant = DXConstant()
        for message in ['alphanumeric_value', 'special_char', 'strings']:
            self.new_system_notices_page.type_message_in_message_body(getattr(obj_dx_constant, message))
        self.new_system_notices_page.click_on_save_message_button()       
     
    @test_case()
    def check_functionality_of_importance_drop_down(self):
        self.system_notices_list_page.click_on_admin_link()        
        status='Draft'
        for importance in ['High', 'Normal']:
            self.new_system_notices_page.fill_system_message_page("test1", status, importance)
        self.system_notices_list_page.click_on_new_system_message() 
             
    @test_case()
    def check_functionality_of_ui_content(self):
        self.system_notices_list_page.click_on_admin_link()
        self.new_system_notices_page.fill_system_message_page("check external url")
    
    @test_case()
    def check_functionality_of_cancel_button(self):
        self.system_notices_list_page.click_on_admin_link()
        self.system_notices_list_page.click_on_new_system_message()
        self.new_system_notices_page.fill_title_textbox("check cancel button")
        self.new_system_notices_page.click_on_cancel_button()
        self.system_notices_list_page.page_should_contain('Administration')
        
    @test_case()
    def check_functionality_of_admin_link(self):
        self.system_notices_list_page.click_on_admin_link()
        self.system_notices_list_page.page_should_contain('Administration')

    @test_case()
    def check_functionality_of_dismiss_all_button(self):
        self.admin_page.click_display_message_link()
        self.admin_page.click_dismiss_all_notices_button()
        assert not self.admin_page.is_element_present(self.admin_page.dismiss_all_notices_button)
