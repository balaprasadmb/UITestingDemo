#coding: utf-8
from advertiser_list import AdvertiserListPage
from advertiser_details import AdvertiserDetailsPage
from edit_advertiser import EditAdvertiser
from configs.dx_constant import DXConstant
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from new_advertiser import NewAdvertiser
from agencies.agencies_list_page import AgenciesListPage
from agencies.agency_details import AgencyDetailsPage
from agencies.agency_edit import AgencyEdit
from agencies.new_agency import NewAgency
from agency_group.agency_group_details import AgencyGroupDetails
from agency_group.agency_group_edit import AgencyGroupEdit
from agency_group.agency_group_list import AgencyGroupList
from agency_group.new_agency_group import NewAgencyGroup
from common_helpers.common_helpers import CommonHelper
from campaigns.new_campaign import NewCampaign
from campaigns.create_campaign import CreateCampaign
from campaigns.edit_campaign import EditCampaign
from campaigns.campaign_show_page import CampaignShowPage
from flights.flight_budget_scheduling import FBSPage
from flights.create_flight import CreateFlight
from flights.flights_show_page import FlightsShowPage
from flights.upload_flights import UploadFlights
from campaign_test_helpers.campaign_test_helper import CampaignTestHelper
from login.login import Login
from lib.dx_date import DXDate
from upload_flight_test import UploadFlightTest
from admin_page import AdminPage
import csv
import os
import time
from selenium.webdriver.common.keys import Keys

class OneView(DXTest):

    @test_case()
    def login_as_dx_admin(self):
        self.setup()
        self.login_page = Login(self.driver.get_browser())
        self.admin_page = AdminPage(self.driver.get_browser())
        self.new_advertiser_page = NewAdvertiser(self.driver.get_browser())
        self.edit_advertiser_page = EditAdvertiser(self.driver.get_browser())
        self.advertiser_list_page = AdvertiserListPage(self.driver.get_browser())
        self.advertiser_details_page = AdvertiserDetailsPage(self.driver.get_browser())
        self.new_agency_group_page = NewAgencyGroup(self.driver.get_browser())
        self.agency_list_page = AgenciesListPage(self.driver.get_browser())
        self.agency_details_page = AgencyDetailsPage(self.driver.get_browser())
        self.agency_edit_page = AgencyEdit(self.driver.get_browser())
        self.new_agency_page = NewAgency(self.driver.get_browser())
        self.common_helper = CommonHelper()
        self.new_campaign = NewCampaign(self.driver.get_browser())
        self.create_campaign = CreateCampaign(self.driver.get_browser())
        self.edit_campaign = EditCampaign(self.driver.get_browser())
        self.campaign_show_page = CampaignShowPage(self.driver.get_browser())
        self.fbs_page = FBSPage(self.driver.get_browser())
        self.create_flight = CreateFlight(self.driver.get_browser())
        self.flight_show_page = FlightsShowPage(self.driver.get_browser())
        self.flight_upload = UploadFlights(self.driver.get_browser())
        self.upload_flights = UploadFlights(self.driver.get_browser())
        self.message = self.advertiser_list_page.success_message

    @test_case()
    def validate_one_view_for_agency_group_and_agency(self):
        self.new_agency_group_page.open()
        self.common_helper.assert_is_element_present(self.new_agency_group_page, 'one_view_section', criteria=False)
        self.new_agency_page.open()
        self.common_helper.assert_is_element_present(self.new_agency_page, 'one_view_section', criteria=False)

    @test_case()
    def assert_data_in_list(self, page_object, loc, data_list):
        data = page_object.get_content_text(loc)
        assert data in data_list

    @test_case()
    def validate_one_view_for_advertiser(self):
        self.admin_page.go_to_link('Admin')
        self.admin_page.wait_till_visible(self.admin_page.advertiser_link[0],
                                          self.admin_page.advertiser_link[1])
        self.admin_page.go_to_link('Advertisers')
        self.advertiser_list_page.wait_till_visible(self.advertiser_list_page.advertiser_list[0],
                                                    self.advertiser_list_page.advertiser_list[1])
        self.advertiser_list_page.click_on_new_advrtiser_button()
        self.new_advertiser_page.wait_till_visible(self.new_advertiser_page.submit_button[0],
                                                   self.new_advertiser_page.submit_button[1], 30)
        self.common_helper.assert_is_element_present(self.new_advertiser_page, self.new_advertiser_page.one_view_section['policies_table'].values())
        for i in range(3, 6):
            self.assert_data_in_list(self.new_advertiser_page, ['css selector', self.new_advertiser_page.one_view_section['data_policy_text']['value'].format(i)],
                                     ['Single Device', 'High Precision', 'Broad Reach'])

    @test_case()
    def policy_selection_helper(self, element):
        locators = {'single': 3, 'high': 4, 'broad': 5}
        self.new_advertiser_page.click_element([self.new_advertiser_page.one_view_section['policy_radio_buttons']['by'],
                                                self.new_advertiser_page.one_view_section['policy_radio_buttons']['value'].format(locators[element])])
        locators.pop(element)
        for key, value in locators.iteritems():
            self.common_helper.assert_is_selected(self.new_advertiser_page,
                                                  [self.new_advertiser_page.one_view_section['policy_radio_buttons']['by'],
                                                   self.new_advertiser_page.one_view_section['policy_radio_buttons']['value'].format(value)],
                                                  criteria=False)

    @test_case()
    def validate_one_view_policy_selection(self):
        self.new_advertiser_page.open()
        for i in range(1, 7):
            self.assert_data_in_list(self.new_advertiser_page, ['css selector', self.new_advertiser_page.one_view_section['column_headers']['value'].format(i)],
                                     ['Make Available', 'Default Policy', 'Data Policy', 'Aliases Used', 'Links Used', 'Notes'])
        for element in ['lock_policy_checkbox', 'single_policy_default_checked_checkbox']:
            self.common_helper.assert_is_element_present(self.new_advertiser_page,
                                                         self.new_advertiser_page.one_view_section[element].values())
        self.new_advertiser_page.click_high_precision_policy_checkbox()
        time.sleep(2)
        self.new_advertiser_page.click_broad_reach_policy_checkbox()
        for element in ['high_precision_policy_checkbox', 'broad_reach_policy_checkbox']:
            self.common_helper.assert_is_selected(self.new_advertiser_page, self.new_advertiser_page.one_view_section[element].values())
        for element in ['single', 'high', 'broad']:
            self.policy_selection_helper(element)

    @test_case()
    def creation_of_advertiser_with_lock_oneview_policy(self):
        self.agency_list_page.open()
        self.agency_list_page.filter_agency_name_in_filterbox(DXConstant().agency_name)
        time.sleep(3)
        self.agency_list_page.click_first_agency()
        self.agency_details_page.wait_till_visible(self.agency_details_page.add_advertiser_button[0],
                                                   self.agency_details_page.add_advertiser_button[1])
        self.agency_details_page.add_new_advertiser()
        time.sleep(5)
        self.advertiser_high_precision_lock = 'High_Precision_Advertiser_Lock_' + self.new_advertiser_page.get_random_string(10)
        self.new_advertiser_page.type_organization_name(self.advertiser_high_precision_lock)
        self.new_advertiser_page.type_advertiser_domain('www.yahoo.com')
        self.common_helper.validate_add_on_cost(self.new_advertiser_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView', 'value')
        self.new_advertiser_page.click_high_precision_policy_checkbox()
        self.new_advertiser_page.click_broad_reach_policy_checkbox()
        self.policy_selection_helper('high')
        self.new_advertiser_page.click_lock_policy_checkbox()
        time.sleep(2)
        self.new_advertiser_page.click_create_advetiser_button()
        time.sleep(5)
        self.advertiser_list_page.page_should_contain(self.message.format(self.advertiser_high_precision_lock))
        

    @test_case()
    def creation_of_advertiser_with_oneview_policy(self, one_view_advertiser, policy_type):
        self.advertiser_name = ''
        self.agency_list_page.open()
        self.agency_list_page.filter_agency_name_in_filterbox(DXConstant().agency_name)
        time.sleep(3)
        self.agency_list_page.click_first_agency()
        self.agency_details_page.wait_till_visible(self.agency_details_page.add_advertiser_button[0],
                                                   self.agency_details_page.add_advertiser_button[1])
        self.agency_details_page.add_new_advertiser()
        time.sleep(10)
        self.advertiser_name = one_view_advertiser + self.new_advertiser_page.get_random_string(10)
        self.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.new_advertiser_page.type_advertiser_domain('www.yahoo.com')
        self.common_helper.validate_add_on_cost(self.new_advertiser_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView', 'value')
        self.new_advertiser_page.click_high_precision_policy_checkbox()
        self.new_advertiser_page.click_broad_reach_policy_checkbox()
        self.policy_selection_helper(policy_type)
        time.sleep(3)
        self.new_advertiser_page.click_create_advetiser_button()
        time.sleep(5)
        self.advertiser_list_page.page_should_contain(self.message.format(self.advertiser_name))
        return self.advertiser_name

    @test_case()
    def validate_advertiser_with_one_view(self):
        self.advertiser_high_precision = self.creation_of_advertiser_with_oneview_policy('High_Precision_Advertiser_Unlock_', 'high')
        self.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_high_precision)
        time.sleep(3)
        self.advertiser_list_page.click_first_advertiser()
        time.sleep(3)
        self.common_helper.validate_add_on_cost(self.advertiser_details_page, 'add_on_cost_name', 'DXU-ONV-009 - DataXu OneView')
        for i in range(1, 4):
            self.assert_data_in_list(self.advertiser_details_page, ['css selector', self.advertiser_details_page.one_view_section['data_policy_text']['value'].format(i)],
                                     ['Single Device', 'High Precision', 'Broad Reach'])
        self.common_helper.assert_is_element_present(self.advertiser_details_page,self.advertiser_details_page.one_view_section['green_tick'].values())

    @test_case()
    def login_by_user(self, role):
        self.new_advertiser_page.click_element(self.new_advertiser_page.dataxu_logo)
        self.new_advertiser_page.go_to_link('Logout')
        self.login_page.wait_till_visible(self.login_page.login_submit[0],
                                          self.login_page.login_submit[1], 15)
        self.login_page.type_email(DXConstant().user_by_role[role]['user_name'])
        self.login_page.type_password(DXConstant().user_by_role[role]['user_password'])
        self.login_page.submit()
        if self.admin_page.is_element_present(self.admin_page.system_message_popup):
            self.admin_page.close_system_message()

    @test_case()
    def fill_campaigns_required_fields(self, campaign_page):
        campaign_page.type_campaign_name(DXConstant().test_campaign_name + campaign_page.get_random_string())
        campaign_page.enter_start_date(DXDate().date_after_two_days())
        campaign_page.enter_end_date(DXDate().last_date_of_current_month())
        campaign_page.enter_cpa_goal(DXConstant().new_campaign_cpa)
        campaign_page.enter_budget(DXConstant().new_campaign_budget)
        campaign_page.enter_cpm(DXConstant().new_campaign_cpm)
        campaign_page.enter_cogs(DXConstant().new_campaign_cogs)
        campaign_page.click_campaign_objective_distribution()
        time.sleep(3)

    @test_case()
    def create_campaign_popup(self, advertiser_name):
        self.new_campaign.open()
        for element in ['campaign_link', 'search_box']:
            self.new_campaign.click_element(getattr(self.new_campaign, element))
        self.new_campaign.click_new_campaign_link()
        self.new_campaign.type_advertiser(advertiser_name)
        self.new_campaign.submit()
        self.create_campaign.wait_till_visible(self.create_campaign.create_campaign[0],
                                               self.create_campaign.create_campaign[1])

    @test_case()
    def campaign_check_oneview_aoc(self):
        self.create_campaign.expand_add_on_cost()
        self.create_campaign.click_new_aoc()
        self.create_campaign.assert_dropdown_options_not_in(self.create_campaign.add_on_cost_name, 'DXU-ONV-009 - DataXu OneView')
        self.create_campaign.click_on_remove_aoc_button()

    @test_case()
    def fill_fields_fbs_page(self):
        self.fbs_page.wait_till_visible(self.fbs_page.save_continue_button[0],
                                        self.fbs_page.save_continue_button[1])
        flight_name = DXConstant().test_flight_name + self.fbs_page.get_random_string()
        self.fbs_page.fill_description(flight_name)
        self.fbs_page.type_bid_enter(DXConstant().flight_bid)
        self.fbs_page.type_budget_enter(DXConstant().flight_budget)
        time.sleep(2)
        return flight_name

    @test_case()
    def flight_bulk_upload_page(self):
        self.create_flight.go_to_link('Bulk Upload Flights')
        self.flight_upload.wait_till_visible(self.flight_upload.upload_flight_sections[0],
                                             self.flight_upload.upload_flight_sections[1], 60)
        self.flight_upload.select_flight_type(DXConstant().flight_type_standard_exchange)
        time.sleep(2)

    @test_case()
    def sys_admin_oneview_validate_one_view_for_advertiser(self):
        self.login_by_user('sys_admin_one_view')
        self.validate_one_view_for_advertiser()

    @test_case()
    def sys_admin_oneview_creation_of_advertiser_with_oneview(self):
        self.validate_advertiser_with_one_view()
        self.creation_of_advertiser_with_lock_oneview_policy()
        self.advertiser_single_device = self.creation_of_advertiser_with_oneview_policy('Single_Device_Advertiser_Unlock_', 'single')
        self.advertiser_broad_reach = self.creation_of_advertiser_with_oneview_policy('Broad_Reach_Advertiser_Unlock_', 'broad')
    
    @test_case()
    def validate_campaign_flight_with_one_view_permission(self):
        self.login_by_user('campaign_manager_one_view')
        self.create_campaign_popup(self.advertiser_high_precision)
        self.common_helper.assert_is_element_present(self.create_campaign, 'one_view_section_enabled')
        self.campaign_check_oneview_aoc()
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 12)
        self.common_helper.assert_is_element_present(self.create_flight, 'one_view_section_enabled')
        self.create_flight.expand_add_on_cost()
        self.create_flight.click_new_aoc()
        self.create_flight.check_dropdown_options(['DXU-ONV-009 - DataXu OneView'], self.create_flight.add_on_cost_name)
        self.create_flight.click_on_aoc_remove_button()
        self.create_flight.click_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.flight_bulk_upload_page()
        self.common_helper.assert_is_element_present(self.flight_upload, 'one_view_section')

    @test_case()
    def oneview_section_status(self, page_object, flag):
        for policy in page_object.one_view_policies_disabled:
            self.common_helper.assert_is_element_present(page_object, policy, criteria=flag)

    @test_case()
    def oneview_editable_for_campaign_flight(self):
        self.create_campaign_popup(self.advertiser_high_precision)
        self.oneview_section_status(self.create_campaign, False)
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 15)
        self.oneview_section_status(self.create_flight, False)
        self.create_flight.click_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.flight_bulk_upload_page()
        for policy in self.flight_upload.one_view_policies_flight_upload:
            self.common_helper.assert_is_element_present(self.flight_upload, policy)

    @test_case()
    def oneview_not_editable_for_campaign_flight(self):
        self.create_campaign_popup(self.advertiser_high_precision_lock)
        self.oneview_section_status(self.create_campaign, True)
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 12)
        self.oneview_section_status(self.create_flight, True)
        self.create_flight.click_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.flight_bulk_upload_page()
        self.common_helper.assert_is_element_present(self.flight_upload, self.flight_upload.one_view_policies_flight_upload[0])
        for policy in self.flight_upload.one_view_policies_flight_upload[1:]:
            self.common_helper.assert_is_element_present(self.flight_upload, policy, criteria=False)

    @test_case()
    def updating_oneview_aoc_as_per_policy(self):
        self.create_campaign_popup(self.advertiser_high_precision)
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 12)
        for policy in self.create_flight.one_view_policies_enabled[:2]:
            self.create_flight.click_element(getattr(self.create_flight, policy))
            time.sleep(3)
            assert self.create_flight.is_element_present(self.create_flight.oneview_aoc_name)
        self.create_flight.click_single_device()
        time.sleep(3)
        assert not self.create_flight.is_element_present(self.create_flight.oneview_aoc_name)

    @test_case()
    def oneview_policy_warning(self, page_object):
        page_object.click_single_device()
        time.sleep(2)
        assert not page_object.is_element_present(page_object.oneview_warning_popup)
        for policy in page_object.single_device_warning:
            page_object.click_element(getattr(page_object, policy))
            time.sleep(2)
            assert page_object.is_element_present(page_object.oneview_warning_popup)
            page_object.click_oneview_popup_cancel()
        page_object.click_high_precision()
        time.sleep(2)
        page_object.click_oneview_popup_ok()
        time.sleep(2)
        page_object.click_broad_reach()
        time.sleep(2)
        assert not page_object.find_element(page_object.oneview_warning_popup).is_displayed()
        time.sleep(2)
        for policy in page_object.broad_reach_warning:
            page_object.click_element(getattr(page_object, policy))
            time.sleep(2)
            assert not page_object.find_element(page_object.oneview_warning_popup).is_displayed()
            page_object.click_broad_reach()
            time.sleep(2)
            if page_object.find_element(page_object.oneview_warning_popup).is_displayed():
                  page_object.click_oneview_popup_ok()
                  time.sleep(2)
        page_object.click_high_precision()

    @test_case()
    def oneview_policy_confirmation_popup(self):
        self.create_campaign_popup(self.advertiser_high_precision)
        self.oneview_policy_warning(self.create_campaign)
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 12)
        self.oneview_policy_warning(self.create_flight)

    @test_case()
    def updating_policy_for_campaign_flight(self):
        self.create_campaign_popup(self.advertiser_high_precision)
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        flight1 =  self.fill_fields_fbs_page()        
        self.fbs_page.click_on_add_flight()
        flight2 = self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.high_precision_enabled[0],
                                             self.create_flight.high_precision_enabled[1])
        self.common_helper.assert_is_selected(self.create_flight, self.create_flight.high_precision_enabled)
        self.create_flight.click_save_and_continue()
        self.create_flight.wait_till_visible(self.create_flight.broad_reach_enabled[0],
                                             self.create_flight.broad_reach_enabled[1])
        self.create_flight.click_broad_reach()
        self.create_flight.click_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.edit_link[0],
                                                  self.campaign_show_page.edit_link[1], 20)
        self.campaign_show_page.edit()
        self.create_campaign.wait_till_visible(self.create_campaign.single_device_enabled[0],
                                               self.create_campaign.single_device_enabled[1], 20)
        self.create_campaign.click_single_device()
        self.create_campaign.submit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.campaign_show_page.go_to_link(flight1)
        self.flight_show_page.wait_till_visible(self.flight_show_page.oneview_section[0],
                                                self.flight_show_page.oneview_section[1])
        self.flight_show_page.page_should_contain('Single Device')
        self.flight_show_page.click_campaign_link()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.campaign_show_page.go_to_link(flight2)
        self.flight_show_page.wait_till_visible(self.flight_show_page.oneview_section[0],
                                                self.flight_show_page.oneview_section[1])
        self.flight_show_page.page_should_contain('Broad Reach')

    @test_case()
    def oneview_policy_workflow(self, policy_advertiser, policy_name):
        self.create_campaign_popup(policy_advertiser)
        self.common_helper.assert_is_selected(self.create_campaign, getattr(self.create_campaign, policy_name))
        self.campaign_check_oneview_aoc()
        self.create_campaign.page_should_not_contain('DXU-ONV-009 - DataXu OneView')
        self.fill_campaigns_required_fields(self.create_campaign)
        self.create_campaign.submit()
        self.fill_fields_fbs_page()
        self.fbs_page.click_on_save_continue()
        self.create_flight.wait_till_visible(self.create_flight.save_and_continue[0],
                                             self.create_flight.save_and_continue[1], 15)
        self.common_helper.assert_is_selected(self.create_flight, getattr(self.create_flight, policy_name))
        if self.create_flight.find_element(self.create_flight.single_device_enabled).is_selected():
            self.create_flight.expand_add_on_cost()
            self.create_flight.page_should_not_contain('DXU-ONV-009 - DataXu OneView')
        else:
            self.create_flight.page_should_contain('DXU-ONV-009 - DataXu OneView')
        self.create_flight.click_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.flight_bulk_upload_page()
        for policy in self.flight_upload.one_view_policies_flight_upload:
            self.common_helper.assert_is_element_present(self.flight_upload, policy)
            
    @test_case()
    def flight_upload_policy_workflow(self, flight_speadsheet, policy1, policy2):
        self.upload_flight_test = UploadFlightTest()
        self.upload_flight_test.read_csv(flight_speadsheet)
        self.upload_flight_test.process_data()
        self.upload_flight_test.write_to_file(flight_speadsheet)
        self.flight_upload.select_file(os.path.dirname(__file__)+ '/../../../data/flights_upload/'+flight_speadsheet+'.csv')
        self.flight_upload.click_upload_file()
        self.upload_flights.wait_till_visible(self.upload_flights.flight_submit[0],
                                              self.upload_flights.flight_submit[1], 120)
        self.upload_flights.click_flights_submit()
        self.fbs_page.wait_till_visible(self.fbs_page.flights_row[0],
                                        self.fbs_page.flights_row[1], 180)
        self.fbs_page.page_should_contain('All flights have been saved successfully.')
        self.fbs_page.click_on_save_exit()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        oneview_flight_name = []
        with open(os.path.dirname(__file__)+ '/../../../data/flights_upload/'+flight_speadsheet+'.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            first = False
            for reader in csvreader:
                if first:
                    oneview_flight_name.append(reader[0])
                first = True
        self.campaign_show_page.go_to_link(oneview_flight_name[0])
        self.flight_show_page.wait_till_visible(self.flight_show_page.oneview_section[0],
                                                self.flight_show_page.oneview_section[1])
        self.flight_show_page.page_should_contain(policy1)
        self.flight_show_page.click_campaign_link()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.campaign_show_page.go_to_link(oneview_flight_name[1])
        self.flight_show_page.wait_till_visible(self.flight_show_page.oneview_section[0],
                                                self.flight_show_page.oneview_section[1])
        self.flight_show_page.page_should_contain(policy1)
        self.flight_show_page.click_campaign_link()
        self.campaign_show_page.wait_till_visible(self.campaign_show_page.tactic_flight_table[0],
                                                  self.campaign_show_page.tactic_flight_table[1], 20)
        self.campaign_show_page.go_to_link(oneview_flight_name[2])
        self.flight_show_page.wait_till_visible(self.flight_show_page.oneview_section[0],
                                                self.flight_show_page.oneview_section[1])
        self.flight_show_page.page_should_contain(policy2)

    @test_case()
    def single_device_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_single_device, 'single_device_enabled')
        self.flight_upload_policy_workflow('Single_Device_Flights', 'Single Device', 'High Precision')

    @test_case()
    def high_precision_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_high_precision, 'high_precision_enabled')
        self.flight_upload_policy_workflow('High_Precision_Flights', 'High Precision', 'Single Device')

    @test_case()
    def broad_reach_policy_workflow(self):
        self.oneview_policy_workflow(self.advertiser_broad_reach, 'broad_reach_enabled')
        self.flight_upload_policy_workflow('Broad_Reach_Flights', 'Broad Reach', 'High Precision')
