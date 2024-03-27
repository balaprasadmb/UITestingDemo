# -*- coding: utf-8 -*-
import os
import time
import uuid

from lib.dx_date import DXDate

from selenium.webdriver.common.keys import Keys

from agency_group.agency_group_details import AgencyGroupDetails
from agency_group.new_agency_group import NewAgencyGroup

from agencies.agency_details import AgencyDetailsPage
from agencies.new_agency import NewAgency

from new_advertiser import NewAdvertiser
from advertiser_list import AdvertiserListPage

from creatives.new_creatives import NewCreatives
from creatives.detailed_edit_creatives import DetailedEditCreatives
from creatives.bulk_upload_creatives import BulkUploadCreatives
from creatives.creative_list_page import CreativeList

from audiences_segments.audiences_list_page import AudiencesListPage
from audiences_segments.create_audience import CreateAudience
from audiences_segments.create_segment import CreateSegment

from activity_create_new_page import ActivityCreateNewPage

from configs.dx_constant import DXConstant
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from lib.custom_exception import CustomException
from manage_organizations import ManageOrganizations

from users.user_list_page import UserListPage
from users.user_edit_page import UserEditPage
from users.user_show_page import UserShowPage

from deal_inventory_edit_page import DealInventoryEditPage

from new_system_message import NewSystemMessage

class EnvironmentSetup(DXTest):

    @test_case()
    def login_as_dx_manager(self):
        self.login_as_user()
        self.new_agency_group_page = NewAgencyGroup(self.driver.get_browser())
        self.agency_group_details_page = AgencyGroupDetails(self.driver.get_browser())
        self.agency_details_page = AgencyDetailsPage(self.driver.get_browser())
        self.new_agency_page = NewAgency(self.driver.get_browser())
        self.new_advertiser_page = NewAdvertiser(self.driver.get_browser())
        self.advertiser_list_page = AdvertiserListPage(self.driver.get_browser())
        self.agency_group_success_message = self.new_agency_group_page.success_message['organization_name']
        self.agency_success_message = self.new_agency_page.success_message['organization_name']
        self.new_creative_page = NewCreatives(self.driver.get_browser())
        self.detailed_edit_creatives = DetailedEditCreatives(self.driver.get_browser())
        self.bulk_upload_new_creative = BulkUploadCreatives(self.driver.get_browser())
        self.creative_list_page = CreativeList(self.driver.get_browser())
        self.audience_segment_list_page = AudiencesListPage(self.driver.get_browser())
        self.audience_create_page = CreateAudience(self.driver.get_browser())
        self.segment_create_page = CreateSegment(self.driver.get_browser())
        self.activity_create_new_page = ActivityCreateNewPage(self.driver.get_browser())
        self.user_list_page = UserListPage(self.driver.get_browser())
        self.user_edit_page = UserEditPage(self.driver.get_browser())
        self.user_show_page = UserShowPage(self.driver.get_browser())
        self.deal_inventory_edit_page = DealInventoryEditPage(self.driver.get_browser())
        self.new_system_message_page = NewSystemMessage(self.driver.get_browser())
        self.manage_organization = ManageOrganizations()
        self.advertiser_id_map = {}

    @test_case()
    def setup_organizations(self):
        print 'Started adding agency group'
        self.new_agency_group_page.open()
        self.new_agency_group_page.wait_till_visible('id', self.new_agency_group_page.agency_group_name[1])
        self.agency_group_name = "regression_agency_group_" + self.new_agency_group_page.get_random_string(15)
        self.new_agency_group_page.type_organization_name(self.agency_group_name)
        self.new_agency_group_page.type_email("regression@dataxu.com")
        self.new_agency_group_page.type_contact_name("DataXu")
        self.new_agency_group_page.check_select_all_currencies()
        self.new_agency_group_page.upload_rate_card(os.getcwd() + '/data/rate_cards/rate_card_USD.xls')
        for media in ["Online", "Mobile", "Video"]:
            self.new_agency_group_page.click_media_type_checkbox(media)
        self.new_agency_group_page.select_all_inventory()
        insight_list = self.new_agency_group_page.insight_list
        for insight in insight_list:
            self.new_agency_group_page.select_insights(insight)
        self.new_agency_group_page.click_targeting_checkbox()
        self.new_agency_group_page.click_cost_model_type('CPA')
        self.new_agency_group_page.click_create_agency_group_button()
        self.new_agency_group_page.check_success_message(
        	self.agency_group_success_message['create_new_agency_group'].format(self.agency_group_name))
        self.manage_organization.override_agency_group(self.agency_group_name)
        self.agency_group_details_page.wait_till_visible('link text', self.agency_group_details_page.add_agency[1])
        self.agency_group_details_page.click_add_agency()
        self.new_agency_page.wait_till_visible('id', self.new_agency_page.submit_button[1])
        self.agency_name = "regression_agency_" + self.new_agency_page.get_random_string(15)
        self.new_agency_page.type_organization_name(self.agency_name)
        self.new_agency_page.click_create_agency_button()
        self.new_agency_page.check_success_message(
        	self.agency_success_message['create_new_agency'].format(self.agency_name))
        self.manage_organization.override_agency(self.agency_name)
        self.agency_details_page.wait_till_visible('css', self.agency_details_page.add_advertiser_button[1])
        self.agency_details_page.add_new_advertiser()
        self.new_advertiser_page.wait_till_visible('id', self.new_advertiser_page.organization_name[1])
        self.advertiser_name = "regression_advertiser_" + self.new_advertiser_page.get_random_string(15)
        self.new_advertiser_page.type_organization_name(self.advertiser_name)
        self.new_advertiser_page.type_advertiser_domain('www.dataxu.com')
        self.new_advertiser_page.check_limit_one_impression_per_page_view()
        self.new_advertiser_page.click_oba_compliance_checkbox()
        self.new_advertiser_page.click_create_advetiser_button()
        message = self.advertiser_list_page.success_message
        self.advertiser_list_page.page_should_contain(message.format(self.advertiser_name))
        self.manage_organization.override_advertiser(self.advertiser_name)
        self.advertiser_list_page.type_advertiser_name_in_filterbox(self.advertiser_name)
        time.sleep(2)
        url = self.advertiser_list_page.find_element(self.advertiser_list_page.advertiser_name_link).get_attribute('href')
        self.advertiser_id_map[self.advertiser_name] = url.split('?')[0].split('/')[-1]

    @test_case()
    def setup_creative(self):
        self.advertiser_list_page._open('/advertisers/%s/creatives' % self.advertiser_id_map[self.advertiser_name])
        self.bulk_upload_new_creative.wait_till_visible('id', self.bulk_upload_new_creative.creative_attributes_section[1])
        self.bulk_upload_new_creative.select_is_flash(DXConstant().select_value_false)
        self.bulk_upload_new_creative.input_concept('Creative_Concept')
        time.sleep(1)
        mock_creative_data_filepath = '/../../data/bulk_upload_creative_files/mock_creative_data.xls'
        self.bulk_upload_new_creative.click_upload(os.path.abspath(os.path.dirname(__file__) + mock_creative_data_filepath))
        self.bulk_upload_new_creative.click_submit()
        self.detailed_edit_creatives.wait_till_visible('id', self.detailed_edit_creatives.creative_form[1])
        self.detailed_edit_creatives.click_detailed_edit()
        time.sleep(2)
        self.detailed_edit_creatives.click_validate_first()
        self.detailed_edit_creatives.save_creative()
        self.creative_list_page.wait_till_visible(self.creative_list_page.creative_table[0], self.creative_list_page.creative_table[1])
        self.detailed_edit_creatives.page_should_contain('Creatives successfully saved. Creative Registration status may take up to 48 hours to update.')
        
    @test_case()
    def setup_segment(self):
        self.advertiser_list_page._open('/advertisers/%s/first_party_segments/new' % self.advertiser_id_map[self.advertiser_name])
        self.segment_create_page.wait_till_visible(self.segment_create_page.create_segment_button[0],
                                                   self.segment_create_page.create_segment_button[1], 15)
        segment_name = DXConstant().segment_name + str(uuid.uuid4())
        self.segment_create_page.enter_segment_name(segment_name)
        self.segment_create_page.click_on_create_segment_button()
        self.segment_create_page.page_should_contain("Successfully created segment '{0}'.".format(segment_name))
 
    @test_case()
    def setup_audience(self):
        self.advertiser_list_page._open('/advertisers/%s/composite_segments/new' % self.advertiser_id_map[self.advertiser_name])
        time.sleep(2)
        self.audience_create_page.select_first_segment_from_segment_table()
        self.audience_create_page.click_use_advance_mode_checkbox()
        self.audience_create_page.click_and_button()
        audience_name = DXConstant().audience_name + str(uuid.uuid4())
        self.audience_create_page.enter_audience_name(audience_name)
        self.audience_create_page.click_create_audience_button()
        self.audience_segment_list_page.page_should_contain("Successfully created segment '{0}'.".format(audience_name))

    @test_case()
    def setup_activity(self):
        self.advertiser_list_page._open('/advertisers/%s/activities/new' % self.advertiser_id_map[self.advertiser_name])
        self.activity_create_new_page.wait_till_visible(self.activity_create_new_page.create_activity_button[0],
                                                        self.activity_create_new_page.create_activity_button[1], 15)
        activity_name = DXConstant().activity_name + self.activity_create_new_page.get_random_string(10)
        self.activity_create_new_page.enter_activity_name_first(activity_name)
        self.activity_create_new_page.click_create_activity_button()
        self.activity_create_new_page.page_should_contain("Activity successfully created:")

    @test_case()
    def setup_deal(self):
        self.advertiser_list_page._open('/deal_inventories/new?locale=en')
        deal_name = DXConstant().deal_name + str(uuid.uuid4())
        self.deal_inventory_edit_page.enter_deal_name(deal_name)
        self.deal_inventory_edit_page.select_deal_inventory_exchange(1)
        self.deal_inventory_edit_page.enter_deal_id(self.deal_inventory_edit_page.get_random_string())
        self.deal_inventory_edit_page.select_deal_type(1)
        self.deal_inventory_edit_page.enter_cost_cpm_value('8')
        self.deal_inventory_edit_page.enter_start_date(DXDate().todays_date())
        self.deal_inventory_edit_page.enter_end_date(DXDate().last_date_of_current_month())
        self.deal_inventory_edit_page.enter_deal_description('test deal description')
        self.deal_inventory_edit_page.enter_deal_permissioned_advertiser_name(DXConstant().advertiser_name)
        self.deal_inventory_edit_page.fill_field(self.deal_inventory_edit_page.deal_permissioned_advertiser_name, Keys.ENTER)
        self.deal_inventory_edit_page.click_on_save_deal_button()
        time.sleep(10)
        self.deal_inventory_edit_page.page_should_contain('Deal {0} was created successfully'.format(deal_name))

    @test_case()
    def setup_system_message(self):
        self.advertiser_list_page._open('/system_notices/new?locale=en')
        self.new_system_message_page.click_on_save_message_button()
        self.new_system_message_page.page_should_contain('Successfully Created System Message')

    @test_case()
    def update_user(self, user, user_email, user_organization, user_role):
        self.user_list_page.open()
        self.user_list_page.filter_user(user)
        self.user_list_page.click_user_email(user_email)
        self.user_show_page.click_on_edit_link()
        self.user_edit_page.select_organization_1(user_organization)
        self.user_edit_page.select_role_1(user_role)
        self.user_edit_page.click_on_update_user_button()
        
    @test_case()
    def update_inventory_manager(self):
        self.update_user(self.user_list_page.inventory_manager, self.user_list_page.inventory_manager_email, self.agency_group_name, 'Inventory Manager')

    @test_case()
    def update_campaign_manager_with_oneview(self):
        self.update_user(self.user_list_page.campaign_manager_with_one_view, self.user_list_page.campaign_manager_with_one_view_email, self.agency_group_name, 'Campaign Manager')
        
    def update_campaign_manager(self):
        self.user_list_page.open()
        self.user_list_page.filter_user(self.user_list_page.campaign_manager)
        self.user_list_page.click_user_email(self.user_list_page.campaign_manager_email)
        self.user_show_page.click_on_edit_link()
        for i in range(1,3):
            roles = {1: 'Campaign Manager', 2: 'Inventory Manager'}
            getattr(self.user_edit_page, 'select_organization_{0}'.format(i))(self.agency_group_name)
            getattr(self.user_edit_page, 'select_role_{0}'.format(i))(roles[i])
        self.user_edit_page.click_on_update_user_button()
