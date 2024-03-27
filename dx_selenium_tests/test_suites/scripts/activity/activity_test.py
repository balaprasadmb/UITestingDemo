#coding: utf-8
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from configs.dx_constant import DXConstant
from selenium.webdriver.common.keys import Keys
from common_helpers.common_helpers import CommonHelper
from login.login import Login
from search.search import SearchPage
from admin_page import AdminPage
from activity_list_page import ActivityListPage
from activity_create_new_page import ActivityCreateNewPage
from activity_edit_page import ActivityEditPage
from activity_show_page import ActivityShowPage

class ActivityTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(DXConstant().user_by_role['campaign_manager'])
        self.activity_list_page = ActivityListPage(self.driver.get_browser())
        self.activity_create_new_page = ActivityCreateNewPage(self.driver.get_browser())
        self.activity_edit_page = ActivityEditPage(self.driver.get_browser())
        self.activity_show_page = ActivityShowPage(self.driver.get_browser())
        self.search_page = SearchPage(self.driver.get_browser())
        self.common_helper = CommonHelper()
        self.login_page = Login(self.driver.get_browser())
        self.admin_page = AdminPage(self.driver.get_browser())

    @test_case()
    def click_on_activity_tab(self):
        self.search_page.click_activity_tab()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])

    @test_case()
    def functionality_of_advertiser_dropdown(self):
        self.click_on_activity_tab()
        actual_advertiser_name = DXConstant().advertiser_name
        self.activity_list_page.select_organization(actual_advertiser_name)
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        expected_advertiser_name = self.activity_list_page.get_innerhtml_text("seleceted_organization_name")
        assert actual_advertiser_name in expected_advertiser_name

    @test_case()
    def activity_list_page_contents(self):
        for page_content in self.activity_list_page.activity_list_page_contents:
            self.activity_list_page.page_should_contain(page_content)
        for element in self.activity_list_page.activity_list_page_elements:
            assert self.activity_list_page.is_element_present(getattr(self.activity_list_page, element))

    @test_case()
    def check_all_checkboxes_are_checked(self, criteria=True):
        elements = [self.activity_list_page.header_master_checkbox, self.activity_list_page.first_activity_checkbox,
                    self.activity_list_page.footer_master_checkbox]
        for element in elements:
            self.common_helper.assert_is_selected(self.activity_list_page, element, criteria)

    @test_case()
    def functionality_of_master_checkbox(self):
        for checkbox in ['click_activity_header_master_checkbox', 'click_activity_footer_master_checkbox']:
            getattr(self.activity_list_page, checkbox)()
            self.check_all_checkboxes_are_checked()
            getattr(self.activity_list_page, checkbox)()
            self.check_all_checkboxes_are_checked(criteria=False)

    @test_case()
    def gear_icon_contents(self):
        self.activity_list_page.click_gear_icon()
        for elements in self.activity_list_page.activity_gear_icon_elements:
            assert self.activity_list_page.is_element_present(getattr(self.activity_list_page, elements))

    @test_case()
    def functionality_of_activity_name(self):
        expected_activity_name = self.activity_list_page.get_innerhtml_text("first_activity_name")
        self.activity_list_page.click_activity_name()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        actual_activity_name = self.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name

    @test_case()
    def activity_show_page_contents(self):
        for page_contents in self.activity_show_page.activity_show_page_contents:
            self.activity_show_page.page_should_contain(page_contents)
        for element in self.activity_show_page.activity_show_page_elements:
            assert self.activity_show_page.is_element_present(getattr(self.activity_show_page, element))

    @test_case()
    def functionality_of_edit_link_from_show_page(self):
        self.activity_show_page.click_edit_link()
        self.activity_edit_page.wait_till_visible(self.activity_edit_page.create_activity_button[0],
                                                  self.activity_edit_page.create_activity_button[1])
        self.activity_edit_page.page_should_contain("Edit activity")

    @test_case()
    def existing_activity_edit_page_contents(self):
        for element in self.activity_edit_page.activity_edit_page_elements:
            assert self.activity_edit_page.is_element_present(getattr(self.activity_edit_page, element))
        for element in self.activity_edit_page.unavailable_elements:
            assert not self.activity_edit_page.is_element_present(getattr(self.activity_edit_page, element))

    @test_case()
    def functionality_of_cancel_button_from_edit_page(self):
        self.activity_edit_page.click_cancel_button()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        self.activity_show_page_contents()

    @test_case()
    def functionality_of_activities_link_from_show_page(self):
        self.activity_show_page.click_activities_link()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_view_activity_link_from_gear_icon(self):
        expected_activity_name = self.activity_list_page.get_innerhtml_text("first_activity_name")
        self.activity_list_page.click_gear_icon()
        self.activity_list_page.click_view_activity_link()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        actual_activity_name = self.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name
        self.functionality_of_activities_link_from_show_page()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_edit_link_from_gear_icon(self):
        self.activity_list_page.click_gear_icon()
        self.activity_list_page.click_edit_activity_link()
        self.activity_edit_page.wait_till_visible(self.activity_edit_page.create_activity_button[0],
                                                  self.activity_edit_page.create_activity_button[1])
        assert self.activity_edit_page.is_element_present(self.activity_edit_page.create_activity_button)
        self.activity_edit_page.click_activities_link()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page_contents()

    @test_case()
    def functionality_of_new_activity_button(self):
        self.activity_list_page.click_on_create_new_activity_button()
        self.activity_create_new_page.wait_till_visible(self.activity_create_new_page.create_activity_button[0],
                                                        self.activity_create_new_page.create_activity_button[1])
        self.activity_create_new_page.page_should_contain("Create activity")

    @test_case()
    def new_activity_edit_page_contents_for_permission_user(self):
        for element in self.activity_create_new_page.activity_create_new_page_elements:
            assert self.activity_create_new_page.is_element_present(getattr(self.activity_create_new_page, element))

    @test_case()
    def activity_type_dropdown_options(self):
        elements = self.activity_create_new_page.find_elements(self.activity_create_new_page.activity_type_dropdown_option)
        actual_option_text = []
        for element in elements:
            actual_option_text.append(element.get_attribute('innerHTML'))
        for option in actual_option_text:
            assert option in self.activity_create_new_page.expected_activity_type_options

    @test_case()
    def functionality_of_add_pixel_button(self):
        self.activity_create_new_page.click_add_pixel_button()
        for element in self.activity_create_new_page.activity_second_row_elements:
            assert self.activity_create_new_page.is_element_present(getattr(self.activity_create_new_page, element))

    @test_case()
    def functionality_of_remove_button(self):
        self.activity_create_new_page.click_remove_button()
        for element in self.activity_create_new_page.activity_second_row_elements:
            assert not self.activity_create_new_page.is_element_present(getattr(self.activity_create_new_page, element))

    @test_case()
    def set_activity_name_and_save(self, activity_name):
        self.activity_create_new_page.enter_activity_name_first(activity_name)
        self.activity_create_new_page.click_create_activity_button()
        self.activity_create_new_page.wait_till_visible(self.activity_create_new_page.create_activity_button[0],
                                                        self.activity_create_new_page.create_activity_button[1])

    @test_case()
    def activity_with_blank_name(self):
        self.set_activity_name_and_save('')
        self.activity_create_new_page.page_should_contain("Activity name can't be blank")

    @test_case()
    def activity_name_with_script_tag(self):
        self.set_activity_name_and_save(DXConstant().html_tag)
        self.activity_create_new_page.page_should_contain("Activity name is invalid")

    @test_case()
    def activity_name_with_more_than_255_char(self):
        self.set_activity_name_and_save(self.activity_create_new_page.get_random_string(256))
        self.activity_create_new_page.page_should_contain("Activity name is too long (maximum is 255 characters)")

    @test_case()
    def functionality_of_cancel_button_from_create_activity_page(self):
        self.activity_create_new_page.click_cancel_button()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page_contents()

    @test_case()
    def valid_activity_name(self, activity_name):
        self.activity_list_page.click_on_create_new_activity_button()
        self.activity_create_new_page.enter_activity_name_first(activity_name)
        self.activity_create_new_page.click_create_activity_button()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page.page_should_contain("Activity successfully created:")

    @test_case()
    def activity_name_with_255_chars_and_search_functionality(self):
        activity_name = self.activity_list_page.get_random_string(255)
        self.valid_activity_name(activity_name)
        self.activity_search_functionality(activity_name)


    @test_case()
    def update_activity_with_name(self, activity_name):
        self.functionality_of_edit_link_from_show_page()
        self.activity_edit_page.enter_activity_name(activity_name)
        self.activity_edit_page.click_create_activity_button()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        self.activity_show_page.page_should_contain(self.activity_show_page.update_success_message.format(activity_name))

    @test_case()
    def activity_name_with_special_chars(self):
        self.update_activity_with_name("!@#$%" + self.activity_create_new_page.get_random_string(10))

    @test_case()
    def activity_name_with_alphanumeric_chars(self):
        self.update_activity_with_name(self.activity_list_page.get_random_string())

    @test_case()
    def activity_search_functionality(self, activity_name):
        expected_activity_name = activity_name
        self.activity_list_page.search_activity(activity_name)
        self.activity_list_page.click_activity_name()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        actual_activity_name = self.activity_show_page.get_activity_name()
        assert actual_activity_name in expected_activity_name
        
    @test_case()
    def fill_up_activity_fields(self, activity_type, is_secure=False):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        activity_name = self.activity_create_new_page.get_random_string()
        self.activity_create_new_page.enter_activity_name_first(activity_name)
        self.activity_create_new_page.select_activity_type(activity_type)
        self.activity_create_new_page.select_tag_server("DFA")
        self.activity_create_new_page.enter_tag_id_first(self.activity_create_new_page.get_random_digits(8))
        if is_secure:
            self.activity_create_new_page.click_secure_checkbox_first()
        self.activity_create_new_page.click_rmx_checkbox_first()
        self.activity_create_new_page.click_create_activity_button()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page.page_should_contain("Activity successfully created:")
        return activity_name

    @test_case()
    def creation_of_new_activity_with_secure(self):
        activity_name = self.fill_up_activity_fields("Marketing", True)
        self.activity_search_functionality(activity_name)
        pixel_tag_value = self.activity_show_page.get_pixel_tag_value()
        for content in ['img', 'https']:
            assert content in pixel_tag_value

    @test_case()
    def creation_of_new_activity_with_non_secure(self):
        activity_name = self.fill_up_activity_fields("Product")
        self.activity_search_functionality(activity_name)
        pixel_tag_value = self.activity_show_page.get_pixel_tag_value()
        for content in ['img', 'http']:
            assert content in pixel_tag_value
        for content in ['https']:
            assert not content in pixel_tag_value

    @test_case()
    def creation_of_activity_with_segment_and_audience(self):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        self.activity_create_new_page.enter_activity_name_first(self.activity_create_new_page.get_random_string())
        self.activity_create_new_page.select_activity_type("Homepage")
        self.activity_create_new_page.select_tag_server("DFA")
        self.activity_create_new_page.enter_tag_id_first(self.activity_create_new_page.get_random_digits(8))
        self.activity_create_new_page.click_secure_checkbox_first()
        self.activity_create_new_page.click_rmx_checkbox_first()
        segment_audience_name = "segment_audience-"+self.activity_create_new_page.get_random_string()
        self.activity_create_new_page.check_create_segment_checkbox()
        self.activity_create_new_page.enter_activity_segment_name(segment_audience_name)
        self.activity_create_new_page.check_create_audience_checkbox()
        self.activity_create_new_page.enter_audience_name(segment_audience_name)
        self.activity_create_new_page.click_create_activity_button()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page.page_should_contain("Activity successfully created:")

    @test_case()
    def functionality_of_share_button(self):
        expected_shared_staus = "With Others"
        self.activity_list_page.select_first_activity_checkbox()
        self.activity_list_page.click_share_activities_button()
        for element in self.activity_list_page.activity_share_popup_element:
            assert self.activity_list_page.is_element_present(getattr(self.activity_list_page, element))
        self.activity_list_page.select_sharing_organization()
        self.activity_list_page.click_share_button_from_popup()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        actual_shared_status = self.activity_list_page.get_innerhtml_text("shared_status")
        assert expected_shared_staus in actual_shared_status

    @test_case()
    def functionality_of_display_check_activities_button(self):
        self.activity_list_page.select_first_activity_checkbox()
        self.activity_list_page.click_display_checked_activities_button()
        assert self.activity_list_page.find_element(self.activity_list_page.display_activities_popup).is_displayed()
        self.activity_list_page.click_display_activities_close_btn()
        assert not self.activity_list_page.find_element(self.activity_list_page.display_activities_popup).is_displayed()

    @test_case()
    def updating_existing_activity(self):
        self.activity_list_page.click_gear_icon()
        self.activity_list_page.click_edit_activity_link()
        activity_name = self.activity_edit_page.get_random_string()
        self.activity_edit_page.enter_activity_name(activity_name)
        self.activity_edit_page.select_activity_type("Expand")
        self.activity_edit_page.select_tag_server("DFA")
        self.activity_edit_page.enter_tag_id(self.activity_create_new_page.get_random_digits(8))
        self.activity_edit_page.click_secure_checkbox()
        self.activity_edit_page.click_rmx_checkbox()
        self.activity_edit_page.click_create_activity_button()
        self.activity_show_page.wait_till_visible(self.activity_show_page.activity_show_page_locator[0],
                                                  self.activity_show_page.activity_show_page_locator[1])
        self.activity_show_page.page_should_contain(self.activity_show_page.update_success_message.format(activity_name))
        
    @test_case()
    def creation_of_multiple_activities(self):
        self.click_on_activity_tab()
        self.functionality_of_advertiser_dropdown()
        self.functionality_of_new_activity_button()
        self.activity_create_new_page.enter_activity_name_first(self.activity_create_new_page.get_random_string())
        self.activity_create_new_page.click_add_pixel_button()
        self.activity_create_new_page.enter_activity_name_second(self.activity_create_new_page.get_random_string())
        self.activity_create_new_page.click_create_activity_button()
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        self.activity_list_page.page_should_contain("2 Activities successfully created:")

    @test_case()
    def login_by_user(self, role):
        self.activity_list_page.click_element(self.activity_list_page.dataxu_logo)
        self.activity_list_page.go_to_link('Logout')
        self.login_page.wait_till_visible(self.login_page.login_submit[0],
                                          self.login_page.login_submit[1], 15)
        self.login_page.type_email(DXConstant().user_by_role[role]['user_name'])
        self.login_page.type_password(DXConstant().user_by_role[role]['user_password'])
        self.login_page.submit()
        if self.admin_page.is_element_present(self.admin_page.system_message_popup):
            self.admin_page.close_system_message()

    @test_case()
    def activity_list_page_contents_without_permissions(self):
        self.login_by_user('campaign_manager_one_view')
        self.click_on_activity_tab()
        self.activity_list_page.select_organization(DXConstant().advertiser_name)
        self.activity_list_page.wait_till_visible(self.activity_list_page.activity_table[0],
                                                  self.activity_list_page.activity_table[1])
        for page_content in self.activity_list_page.activity_list_page_contents:
            self.activity_list_page.page_should_contain(page_content)
        for element in self.activity_list_page.activity_list_page_elements_without_permission:
            assert self.activity_list_page.is_element_present(getattr(self.activity_list_page, element))
        assert not self.activity_list_page.is_element_present(self.activity_list_page.share_activities_button)

    @test_case()
    def new_activity_edit_page_contents_without_permissions(self):
        self.activity_list_page.click_on_create_new_activity_button()
        for element in self.activity_create_new_page.create_new_page_elements_without_permissions:
            assert self.activity_create_new_page.is_element_present(getattr(self.activity_create_new_page, element))
        for element in self.activity_create_new_page.unavilable_create_new_page_elements_without_permissions:
            assert not self.activity_create_new_page.is_element_present(getattr(self.activity_create_new_page, element))
