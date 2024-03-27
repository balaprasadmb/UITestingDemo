from custom_inventory_edit_page import CustomInventoryEditPage
from custom_inventory_show_page import CustomInventoryShowPage
from deal_inventory_edit_page import DealInventoryEditPage
from deal_inventory_show_page import DealInventoryShowPage
from inventory_list_page import InventoryListPage
from guaranteed_inventory_edit_page import GuaranteedInventoryEditPage
from guaranteed_inventory_show_page import GuaranteedInventoryShowPage
from dx_test.dx_test import DXTest
from search.search import SearchPage
from lib.gui_tests import test_case
from configs.dx_constant import DXConstant
import time
from lib.dx_date import DXDate
from selenium.webdriver.common.keys import Keys

class InventoryTest(DXTest):

    def login_as_campaign_manager(self):
        self.setup(DXConstant().user_by_role['campaign_manager'])
        self.inventory_list_page = InventoryListPage(self.driver.get_browser())
        self.guaranteed_inventory_edit_page = GuaranteedInventoryEditPage(self.driver.get_browser())
        self.guaranteed_inventory_show_page = GuaranteedInventoryShowPage(self.driver.get_browser())
        self.deal_inventory_edit_page = DealInventoryEditPage(self.driver.get_browser())
        self.custom_inventory_edit_page = CustomInventoryEditPage(self.driver.get_browser())
        self.custom_inventory_show_page = CustomInventoryShowPage(self.driver.get_browser())
    
    def click_inventory_tab(self):
        search_page = SearchPage(self.driver.get_browser())
        search_page.click_inventory_link()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-1')
    
    @test_case()
    def guaranteed_inventory_list_page_contents(self):
        self.click_inventory_tab()
        for page_contents in self.inventory_list_page.guaranteed_inventory_list_page_contents:
            self.inventory_list_page.page_should_contain(page_contents)
        for elements in self.inventory_list_page.guaranteed_inventory_list_page_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def functionality_of_advertiser_dropdown(self):
        self.inventory_list_page.click_on_organization_dropdown()
        self.inventory_list_page.fill_organization_text_box(DXConstant().advertiser_name)
        self.inventory_list_page.fill_field(self.inventory_list_page.advertiser_input, Keys.ENTER)
        time.sleep(5)

    @test_case()
    def creation_of_guaranteed_inventory(self, media_type = 'Online'):
        inventory_media_type =  DXConstant().inventory_names_with_media_type
        self.click_inventory_tab()
        self.inventory_list_page.click_on_new_guaranteed_media_button()
        self.inventory_name = inventory_media_type[media_type] + self.guaranteed_inventory_edit_page.get_random_string()
        self.guaranteed_inventory_edit_page.wait_till_visible('id', self.guaranteed_inventory_edit_page.guaranteed_inventory_form[1])
        functions_dict = {'enter_guaranteed_inventory_publisher_name': self.inventory_name, 'enter_guaranteed_inventory_placement_name': self.inventory_name,
                            'click_on_guaranteed_inventory_available_checkbox': '', 'click_on_guaranteed_inventory_secure_checkbox': '',
                            'select_guaranteed_inventory_media_type': media_type}
        for key, value in functions_dict.iteritems():
            if value:
                getattr(self.guaranteed_inventory_edit_page, key)(value)
            else:
                getattr(self.guaranteed_inventory_edit_page, key)()
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-1')
        self.inventory_list_page.page_should_contain('{0} was created successfully'.format(self.inventory_name))

    @test_case()
    def creation_of_mobile_guaranteed_inventory(self):
        self.creation_of_guaranteed_inventory('Mobile')

    @test_case()
    def creation_of_video_guaranteed_inventory(self):
        self.creation_of_guaranteed_inventory('Linear Video')

    @test_case()
    def guaranteed_inventory_gear_icon_contents(self):
        self.inventory_list_page.click_on_guaranteed_inventory_gear_icon()
        for elements in self.inventory_list_page.guaranteed_inventory_gear_icon_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def guaranteed_inventory_functionality_of_edit_link(self):
        self.inventory_list_page.click_on_guaranteed_inventory_edit_link()
        self.guaranteed_inventory_edit_page.wait_till_visible('class', 'inventory_source_form')
        self.inventory_list_page.page_should_contain('Edit Guaranteed Media')

    @test_case()
    def guaranteed_inventory_publisher_name_textbox_max_limit(self):
        assert self.guaranteed_inventory_edit_page.get_attribute_value(self.guaranteed_inventory_edit_page.guaranteed_inventory_publisher_name, 'size') == '255'

    @test_case()
    def guaranteed_inventory_placement_name_textbox_max_limit(self):
        assert self.guaranteed_inventory_edit_page.get_attribute_value(self.guaranteed_inventory_edit_page.guaranteed_inventory_placement_name, 'size') == '255'

    @test_case()
    def guaranteed_inventory_update_functionality(self):
        self.updated_inventory_name = DXConstant().updated_gm_inventory_name + self.guaranteed_inventory_edit_page.get_random_string()
        update_dict = {'enter_guaranteed_inventory_publisher_name':self.updated_inventory_name, 'enter_guaranteed_inventory_placement_name':self.updated_inventory_name,
                       'click_on_guaranteed_inventory_available_checkbox':'', 'click_on_guaranteed_inventory_secure_checkbox':'', 'select_guaranteed_inventory_media_type': 'Mobile'}
        for key, value in update_dict.iteritems():
            if value:
                getattr(self.guaranteed_inventory_edit_page, key)(value)
            else:
                getattr(self.guaranteed_inventory_edit_page, key)()                
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-1')
        self.inventory_list_page.page_should_contain('{0} was updated successfully'.format(self.updated_inventory_name))

    @test_case()
    def guaranteed_inventory_functionality_of_publisher_or_placement_name_link(self):
        self.click_inventory_tab()
        self.inventory_list_page.click_on_guaranteed_inventory_publisher_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()
        self.click_inventory_tab()
        self.inventory_list_page.click_on_guaranteed_inventory_placement_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()

    def guaranteed_inventory_functionality_of_placement_name_link_helper(self):
        self.guaranteed_inventory_show_page.wait_till_visible('id', 'details')
        for page_contents in self.guaranteed_inventory_show_page.guaranteed_inventory_show_page_contents:
            self.guaranteed_inventory_show_page.page_should_contain(page_contents)
        self.guaranteed_inventory_show_page.page_should_not_contain("Price")
        for elements in self.guaranteed_inventory_show_page.guaranteed_inventory_show_page_elements:
            assert self.guaranteed_inventory_show_page.is_element_present(getattr(self.guaranteed_inventory_show_page, elements))

    @test_case()
    def functionality_of_new_guaranteed_media_button(self):
        self.click_inventory_tab()
        self.inventory_list_page.click_on_new_guaranteed_media_button()
        self.guaranteed_inventory_edit_page.wait_till_visible('id', self.guaranteed_inventory_edit_page.guaranteed_inventory_form[1])
        self.guaranteed_inventory_edit_page.page_should_contain('Create Guaranteed Media')

    @test_case()
    def guaranteed_inventory_click_on_budget_section(self):
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_budget_section_header()
        for elements in self.guaranteed_inventory_edit_page.guaranteed_inventory_budget_section_elements:
            assert self.guaranteed_inventory_edit_page.is_element_present(getattr(self.guaranteed_inventory_edit_page, elements))
        
    @test_case()
    def guaranteed_inventory_edit_page_contents(self):
        for page_contents in self.guaranteed_inventory_edit_page.guaranteed_inventory_edit_page_contents:
            self.guaranteed_inventory_edit_page.page_should_contain(page_contents)
        self.guaranteed_inventory_edit_page.page_should_not_contain("Price")
        for elements in self.guaranteed_inventory_edit_page.guaranteed_inventory_edit_page_elements:
            assert self.guaranteed_inventory_edit_page.is_element_present(getattr(self.guaranteed_inventory_edit_page, elements))

    @test_case()
    def guaranteed_inventory_tag_section_for_linear_video_media_type(self):
        self.guaranteed_inventory_edit_page.select_guaranteed_inventory_media_type('Linear Video')
        self.guaranteed_inventory_edit_page.page_should_contain('Maximum Duration')
        self.guaranteed_inventory_edit_page.check_dropdown_options(self.guaranteed_inventory_edit_page.maximum_duration_dropdown, self.guaranteed_inventory_edit_page.guaranteed_inventory_tag_size_dropdown01)

    @test_case()
    def guaranteed_inventory_add_another_size_button_functionality(self):
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_add_another_size_button()
        for elements in self.guaranteed_inventory_edit_page.guaranteed_inventory_another_size_element:
            assert self.guaranteed_inventory_edit_page.is_element_present(getattr(self.guaranteed_inventory_edit_page, elements))
        
    @test_case()
    def guaranteed_inventory_functionality_of_none_assigned_link(self):
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_none_assigned_link()
        self.guaranteed_inventory_edit_page.wait_till_visible('class', 'assign_creative_modal')
        self.guaranteed_inventory_edit_page.page_should_contain('Assign Creative')

    @test_case()
    def guaranteed_inventory_assign_creative_popup_contents(self):
        for elements in self.guaranteed_inventory_edit_page.guaranteed_inventory_assign_creative_popup_elements:
            assert self.guaranteed_inventory_edit_page.is_element_present(getattr(self.guaranteed_inventory_edit_page, elements))

    @test_case()
    def guaranteed_inventory_functionality_of_assign_creative_popup_close_button(self):
        self.guaranteed_inventory_edit_page.click_on_close_button_from_assign_creative_popup()
        time.sleep(3)

    @test_case()
    def guaranteed_inventory_functionality_of_creative_size_remove_button(self):
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_remove_creative_size_button()
        assert not self.guaranteed_inventory_edit_page.is_element_present(self.guaranteed_inventory_edit_page.guaranteed_inventory_not_assigned_link01)

    @test_case()
    def guaranteed_inventory_functionality_of_cancel_button(self):
        self.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_cancel_button()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-1')
        for page_contents in self.inventory_list_page.guaranteed_inventory_list_page_contents:
            self.inventory_list_page.page_should_contain(page_contents)
        for elements in self.inventory_list_page.guaranteed_inventory_list_page_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def deal_tab_access_to_permission_user(self):
        self.inventory_list_page.is_element_present(self.inventory_list_page.deal_inventory_tab)

    @test_case()
    def deal_inventory_list_page_contents(self):
        self.inventory_list_page.click_on_deals_tab()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-2', 15)
        for page_contents in self.inventory_list_page.deals_inventory_list_page_contents:
            self.inventory_list_page.page_should_contain(page_contents)
        for elements in self.inventory_list_page.deals_inventory_list_page_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def creation_of_deal_inventory(self):
        self.inventory_list_page.click_on_new_deal_button()
        self.deal_inventory_edit_page.wait_till_visible('id', self.deal_inventory_edit_page.deal_inventory_form[1])
        self.deal_inventory_name = DXConstant().deal_name + self.deal_inventory_edit_page.get_random_string()
        self.deal_inventory_edit_page.enter_deal_name(self.deal_inventory_name)
        self.deal_inventory_edit_page.select_deal_inventory_exchange(1)
        self.deal_inventory_edit_page.enter_deal_id(self.deal_inventory_edit_page.get_random_string())
        self.deal_inventory_edit_page.select_deal_type(1)
        self.deal_inventory_edit_page.enter_cost_cpm_value(DXConstant().deal_cpm)
        self.deal_inventory_edit_page.enter_start_date(DXDate().todays_date())
        self.deal_inventory_edit_page.enter_end_date(DXDate().last_date_of_current_month())
        self.deal_inventory_edit_page.enter_deal_description(DXConstant().deal_description)
        self.deal_inventory_edit_page.enter_deal_permissioned_advertiser_name(DXConstant().advertiser_name)
        self.deal_inventory_edit_page.fill_field(self.deal_inventory_edit_page.deal_permissioned_advertiser_name, Keys.ENTER)
        self.deal_inventory_edit_page.click_on_save_deal_button()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-2', 15)
        self.inventory_list_page.page_should_contain('Deal {0} was created successfully'.format(self.deal_inventory_name))

    @test_case()
    def deal_inventory_gear_icon_contents(self):
        self.inventory_list_page.click_on_deal_inventory_gear_icon()
        assert self.inventory_list_page.is_element_present(self.inventory_list_page.deal_inventory_edit_link)

    @test_case()
    def functionality_of_new_deal_button(self):
        self.inventory_list_page.click_on_new_deal_button()
        self.deal_inventory_edit_page.wait_till_visible('id', self.deal_inventory_edit_page.deal_inventory_form[1])
        self.deal_inventory_edit_page.page_should_contain('Create Deal')

    @test_case()
    def deal_inventory_edit_page_contents(self):
        for page_contents in self.deal_inventory_edit_page.deal_inventory_edit_page_contents:
            self.deal_inventory_edit_page.page_should_contain(page_contents)
        for elements in self.deal_inventory_edit_page.deal_inventory_edit_page_elements:
            assert self.deal_inventory_edit_page.is_element_present(getattr(self.deal_inventory_edit_page, elements))

    @test_case()
    def deal_inventory_functionality_of_cancel_button(self):
        self.deal_inventory_edit_page.click_on_deal_cancel_button()
        self.inventory_list_page.wait_till_visible('id', 'ui-tabs-2', 20)
        for page_contents in self.inventory_list_page.deals_inventory_list_page_contents:
            self.inventory_list_page.page_should_contain(page_contents)
        for elements in self.inventory_list_page.deals_inventory_list_page_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def custom_inventory_tab_access_to_permission_user(self):
        self.inventory_list_page.is_element_present(self.inventory_list_page.custom_inventory_tab)

    @test_case()
    def custom_inventory_list_page_contents(self):
        self.inventory_list_page.click_on_custom_inventory_tab()
        self.inventory_list_page.wait_till_visible('id', 'custom_inventory_table_wrapper')
        for page_contents in self.inventory_list_page.custom_inventory_list_page_contents:
            self.inventory_list_page.page_should_contain(page_contents)
        for elements in self.inventory_list_page.custom_inventory_list_page_elements:
            assert self.inventory_list_page.is_element_present(getattr(self.inventory_list_page, elements))

    @test_case()
    def custom_inventory_gear_icon_contents(self):
        self.inventory_list_page.click_on_custom_inventory_gear_icon()
        assert self.inventory_list_page.is_element_present(self.inventory_list_page.custom_inventory_edit_link)

    @test_case()
    def custom_inventory_export_tag_link_not_available(self):
        assert not self.inventory_list_page.is_element_present(self.inventory_list_page.custom_inventory_export_tag_link)

    @test_case()
    def custom_inventory_functionality_of_edit_link(self):
        self.inventory_list_page.click_on_custom_inventory_edit_link()
        self.inventory_list_page.page_should_contain('Edit Custom Inventory')

    @test_case()
    def custom_inventory_functionality_of_publisher_or_placement_name_link(self):
        self.click_inventory_tab()
        self.inventory_list_page.click_on_custom_inventory_tab()
        self.inventory_list_page.wait_till_visible('id', 'custom_inventory_table_wrapper')
        self.inventory_list_page.click_on_custom_inventory_publisher_name_link()
        self.custom_inventory_functionality_of_placement_name_link_helper()
        self.inventory_list_page.click_on_custom_inventory_placement_name_link()
        self.custom_inventory_functionality_of_placement_name_link_helper()

    def custom_inventory_functionality_of_placement_name_link_helper(self):
        self.custom_inventory_show_page.wait_till_visible('id', 'details')
        for page_contents in self.custom_inventory_show_page.custom_inventory_show_page_contents:
            self.custom_inventory_show_page.page_should_contain(page_contents)
        for elements in self.custom_inventory_show_page.custom_inventory_show_page_elements:
            assert self.custom_inventory_show_page.is_element_present(getattr(self.custom_inventory_show_page, elements))
        self.custom_inventory_show_page.click_on_custom_inventory_link()

    @test_case()
    def functionality_of_new_custom_inventory_button(self):
        self.inventory_list_page.click_on_new_custom_inventory_button()
        self.custom_inventory_edit_page.wait_till_visible('id', self.custom_inventory_edit_page.custom_inventory_form[1])
        self.custom_inventory_edit_page.page_should_contain('Create Custom Inventory')
