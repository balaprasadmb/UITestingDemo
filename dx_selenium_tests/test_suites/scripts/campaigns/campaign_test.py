import uuid
import random
import os
import time
from selenium.common.exceptions import NoSuchElementException
from dx_test.dx_test import DXTest
from search.search import  SearchPage
from campaigns.new_campaign import NewCampaign
from campaigns.create_campaign import CreateCampaign
from campaigns.edit_campaign import EditCampaign
from campaigns.campaign_show_page import CampaignShowPage
from flights.flight_budget_scheduling import FBSPage
from flights.create_flight import CreateFlight
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from campaign_test_helpers.campaign_test_helper import CampaignTestHelper

class CampaignTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(DXConstant().user_by_role['campaign_manager'])
        self.search_page = SearchPage(self.driver.get_browser())
        self.new_campaign = NewCampaign(self.driver.get_browser())
        self.create_campaign = CreateCampaign(self.driver.get_browser())
        self.edit_campaign = EditCampaign(self.driver.get_browser())
        self.show_campaign = CampaignShowPage(self.driver.get_browser())
        self.fbs = FBSPage(self.driver.get_browser())
        self.create_flight = CreateFlight(self.driver.get_browser())

    def search_page_campaign_click(self):
        self.search_page.wait_for_campaign_link()
        self.search_page.click_campaign_link()

    def fill_advertiser_details(self, channel = None, counter = 0):
        try:
            self.new_campaign.click_new_campaign_link()
            self.new_campaign.type_advertiser(DXConstant().advertiser_name)
            if channel:
                self.new_campaign.select_campaign_channel(channel)
            self.new_campaign.submit()
        except NoSuchElementException:
            if counter < 3:
                counter += 1
                self.new_campaign.page_refresh()
                time.sleep(10)
                self.fill_advertiser_details(channel, counter)

    @test_case()
    def create_campaign_page(self):
        self.search_page_campaign_click()
        self.fill_advertiser_details()
        time.sleep(5)
        self.create_campaign.wait_for_campaign_details()

    @test_case()
    def fill_create_campaign_fields(self, campaign, campaign_attributes):
        campaign = campaign.fill_fields(campaign_attributes)
        return campaign

    @test_case()
    def datepicker_should_visible(self, date_type):
        self.create_campaign_page()
        if date_type == 'start':
            self.create_campaign.click_start_date()
        elif date_type == 'end':
            self.create_campaign.click_end_date()
        assert self.create_campaign.find_element(self.create_campaign.date_picker).is_displayed()

    def fill_fields_with_blank_data(self):
        self.create_campaign_page()
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def blank_message_validation(self, element_name):
        self.create_campaign.page_should_contain(self.create_campaign.blank_msgs[element_name])

    @test_case()
    def blank_campaign_name(self):
        self.blank_message_validation('campaign_name')

    @test_case()
    def blank_start_date(self):
        self.blank_message_validation('start_date')

    @test_case()
    def blank_end_date(self):
        self.blank_message_validation('end_date')

    @test_case()
    def blank_tactics(self):
        self.blank_message_validation('tactic_name')

    @test_case()
    def blank_add_on_costs(self):
        self.blank_message_validation('add_on_cost_name')

    @test_case()
    def blank_cpa(self):
        self.blank_message_validation('cpa')

    @test_case()
    def blank_cogs(self):
        self.blank_message_validation('cogs')

    @test_case()
    def blank_io_budget(self):
        self.blank_message_validation('budget')

    @test_case()
    def blank_io_margin(self):
        self.blank_message_validation('margin')

    @test_case()
    def blank_activity_type(self):
        self.blank_message_validation('activity_type')

    @test_case()
    def blank_third_party_tag_id(self):
        self.blank_message_validation('third_party_tag_id')

    @test_case()
    def blank_cpm(self):
        self.blank_message_validation('cpm')

    def fill_fields_with_special_character_data(self):
        self.create_campaign_page()
        for field  in ['cpa', 'cpm', 'cogs', 'budget', 'insertion_order' 'tag_id']:
            self.create_campaign.campaign_attributes[field] = DXConstant().special_char
            self.create_campaign.campaign_attributes['activity_pixel'] = 1
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def special_character_validation(self, element):
        self.create_campaign.page_should_contain(self.create_campaign.special_character_msgs[element])

    @test_case()
    def special_char_cpa(self):
        self.special_character_validation('cpa')

    @test_case()
    def special_char_cpm(self):
        self.special_character_validation('cpm')

    @test_case()
    def special_char_value(self):
        self.special_character_validation('value')

    @test_case()
    def special_char_io_budget(self):
        self.special_character_validation('budget')

    @test_case()
    def special_char_insertion_order(self):
        self.special_character_validation('order') 

    @test_case()
    def special_char_cog(self):
        self.special_character_validation('cogs')

    @test_case()
    def special_char_third_party_tag_id(self):
        self.special_character_validation('third_party_tag_id')

    def fill_fields_with_string_data(self):
        self.create_campaign_page()
        for field  in ['cpa', 'cpm', 'cogs', 'budget', 'tactics_budget', 'icaps' ]:
            self.create_campaign.campaign_attributes[field] = DXConstant().strings
            self.create_campaign.campaign_attributes['tactics'] = DXConstant().tactics
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def string_validation(self, element):
        self.create_campaign.page_should_contain(self.create_campaign.string_msgs[element])

    @test_case()
    def string_cpa(self):
        self.string_validation('cpa')

    @test_case()
    def string_io_budget(self):
        self.string_validation('budget')

    @test_case()
    def string_cpm(self):
        self.string_validation('cpm')

    @test_case()
    def string_cog(self):
        self.string_validation('cogs')

    @test_case()
    def string_budget(self):
        self.string_validation('tactic_budget')

    @test_case()
    def string_impression(self):
        self.string_validation('tactic_impression_cap')

    def fill_fields_with_max_range_data(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['cpa'] = DXConstant().limit_ten_thousand
        self.create_campaign.campaign_attributes['budget'] = DXConstant().limit_ninty_lacs
        self.create_campaign.campaign_attributes['cogs'] = DXConstant().limit_ten
        self.create_campaign.campaign_attributes['objective'] = 'ctr'
        for field  in ['cpm', 'goal_ctr' ]:
            self.create_campaign.campaign_attributes[ field ] = DXConstant().limit_hundread
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def range_message(self, element):
        self.create_campaign.page_should_contain(self.create_campaign.range_msgs[element])

    @test_case()
    def range_cpa(self):
        self.range_message('cpa')

    @test_case()
    def range_io_budget(self):
        self.range_message('budget')

    @test_case()
    def range_cpm(self):
        self.range_message('cpm')

    @test_case()
    def range_cogs(self):
        self.range_message('cogs')

    @test_case()
    def range_margin(self):
        self.range_message('margin')

    @test_case()
    def range_goal_ctr(self):
        self.range_message('ctr')

    @test_case()
    def geo_target_section(self):
        self.create_campaign_page()
        self.create_campaign.select_geo_targeting_type(2)
        for element in ['geo_target_country_id', 'geo_target_area_type']:
            self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def select_specify_region_within(self):
        self.create_campaign.select_geo_targeting_type(2)

    @test_case()
    def select_avail_regions(self, country, regions_list):
        self.create_campaign.select_geo_target_country(country)
        for region in regions_list:
            self.create_campaign.select_avail_countries_dual(region)

    @test_case()
    def select_region_us(self):
        self.select_avail_regions('United States', ['Colorado' , 'Connecticut' ,'Delaware'])

    @test_case()
    def select_region_brazil(self):
        self.select_avail_regions('Brazil', ['Mato Grosso' , 'Minas Gerais'])

    @test_case()
    def select_region_canada(self):
        self.select_avail_regions('Canada', ['New Brunswick' , 'Nova Scotia' , 'Nunavut'])

    @test_case()
    def select_region_france(self):
        self.select_avail_regions('France', ['Corse' , 'Franche-Comte' , 'Franche-Comte'])

    @test_case()
    def select_region_germany(self):
        self.select_avail_regions('Germany', ['Bremen' , 'Hamburg', 'Hessen'])

    @test_case()
    def select_region_gb(self):
        self.select_avail_regions('Great Britain', ['Ards' , 'Armagh' , 'Ballymena'])

    @test_case()
    def select_region_ireland(self):
        self.select_avail_regions('Ireland', ['Clare' , 'Dublin' , 'Galway'])

    @test_case()
    def select_region_italy(self):
        self.select_avail_regions('Italy', ['Liguria' , 'Lombardia' ,'Lombardia'])

    @test_case()
    def select_region_poland(self):
        self.select_avail_regions('Poland', ['Pomorskie' , 'Opolskie' ,'Malopolskie'])

    @test_case()
    def select_region_spain(self):
        self.select_avail_regions('Spain', ['Catalonia' , 'Extremadura' ,'Madrid'])

    @test_case()
    def geo_target_section_metrocodes(self):
        self.create_campaign_page()
        self.create_campaign.select_geo_targeting_type(2)
        for element in ['geo_target_country_id', 'geo_target_area_type']:
            self.create_campaign.click_element(getattr(self.create_campaign, element))
        self.create_campaign.select_geo_target_country('United States')
        self.create_campaign.select_area_type(1)

    @test_case()
    def metrocodes_shown_for_us(self):
        self.select_specify_region_within()
        self.create_campaign.select_geo_target_country('United States')
        self.create_campaign.select_area_type(1)
        self.create_campaign.wait_till_visible('id', 'campaign_dmas_input')
        for metro_country in ['500 Portland-Auburn ME', '506 Boston MA-Manchester NH', '519 Charleston SC']:
            self.create_campaign.select_avail_countries_metro(metro_country)

    @test_case()
    def metrocodes_not_shown_for_others(self, country):
        self.select_specify_region_within()
        self.create_campaign.select_geo_target_country(country)
        self.create_campaign.assert_options()

    def fill_fields_with_negative_values(self):
        self.create_campaign_page()
        for field in ['cpm', 'tag_id', 'filters_value']:
            self.create_campaign.campaign_attributes[field] = DXConstant().negative_value
        self.create_campaign.campaign_attributes['objective'] = 'performance'
        self.create_campaign.campaign_attributes['activity_pixel'] = 1
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def negative_value_validation(self, element):
        self.create_campaign.page_should_contain(self.create_campaign.negative_value_message[element])

    @test_case()
    def negative_value_cpm(self):
        self.negative_value_validation('cpm')

    @test_case()    
    def negative_value_third_party_tag_id(self):
        self.negative_value_validation('third_party_tag_id')

    @test_case()
    def negative_value_filter_values(self):
        self.negative_value_validation('activity_value')

    @test_case()
    def negative_value_ctr_goal(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['goal_ctr'] =  DXConstant().negative_value
        self.create_campaign.campaign_attributes['objective'] = 'ctr'
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.page_should_contain(self.create_campaign.negative_value_message['ctr_goal'])

    def fill_fields_with_alphanumeric_values(self):
        self.create_campaign_page()
        for field in ['tag_id','filters_value']:
            self.create_campaign.campaign_attributes[field] = DXConstant().alphanumeric_value
        self.create_campaign.campaign_attributes['objective'] = 'performance'
        self.create_campaign.campaign_attributes['activity_pixel'] = 1    
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    @test_case()
    def alphanumeric_value_third_party_tag_id(self):
        self.negative_value_validation('third_party_tag_id')

    @test_case()
    def alphanumeric_value_filter_values(self):
        self.negative_value_validation('activity_value')

    @test_case()
    def language_targeting_test_cases(self):
        self.create_campaign_page()
        self.create_campaign.expand_lang_targeting()

    @test_case()
    def language_targeting_page_content(self):
        self.create_campaign.check_dropdown_options(self.create_campaign.lang_targeting_dropdown_option, self.create_campaign.base_lang_targeting)
        for element in ['move_selected_lang', 'remove_selected_lang', 'move_all_selected_lang', 'remove_all_selected_lang']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def select_button_functionality(self):
        self.create_campaign.select_lang_targeting("Dutch")
        self.create_campaign.click_move_all_selected_lang()
        self.create_campaign.click_remove_all_selected_lang()

    @test_case()
    def complete_flow_with_distribution(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_distribution(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def go_to_campaign_show_page(self):
        self.fbs.wait_for_flights()
        time.sleep(5)
        self.fbs.go_to_link(self.campaign_attributes['campaign_name'])
        self.show_campaign.wait_for_loading()

    @test_case()
    def go_to_campaign_edit(self):
        if self.show_campaign.is_element_present(self.show_campaign.reports_link):
            time.sleep(5)
            self.show_campaign.go_to_link('Edit')
            self.edit_campaign.wait_for_details()

    def assert_attributes(self, element):
        self.create_campaign.page_should_contain(self.campaign_attributes[element])

    @test_case()
    def assert_start_date(self):
        self.assert_attributes('start_date')

    @test_case()
    def assert_end_date(self):
        self.assert_attributes('end_date')

    @test_case()
    def assert_cpa(self):
        self.assert_attributes('value')

    @test_case()
    def assert_budget(self):
        self.assert_attributes('budget')

    @test_case()
    def assert_cpm(self):
        self.assert_attributes('value')

    @test_case()
    def assert_margin(self):
        self.assert_attributes('margin')

    @test_case()
    def assert_objective(self):
        objective_dict = {
            'performance' : 'Maximize Performance and Distribution',
            'ctr' : 'Maximize CTR',
            'distribution': 'Maximize Distribution',
            'views': 'Maximize Completed Ad Views'
        }
        self.create_campaign.page_should_contain(objective_dict[self.campaign_attributes['objective']])

    @test_case()
    def assert_tactics(self):
        for content in ['Default', self.campaign_attributes['tactics_value']]:
            self.create_campaign.page_should_contain(content)

    @test_case()
    def assert_tactics_budget(self):
        self.assert_attributes('tactics_budget')

    @test_case()
    def assert_tactics_impression_cap(self):
        self.assert_attributes('value')

    @test_case()
    def assert_external_id_source(self):
        self.assert_attributes('source')

    @test_case()
    def assert_external_id_value(self):
        self.assert_attributes('source_value')

    @test_case()
    def assert_brand_safety(self):
        try:
            brand_safety_dict = {
            '1': 'Level One',
            '2': 'Level Two',
            '3': 'Level Three',
            '4': 'Level Four'
            }
            self.create_campaign.page_should_contain(brand_safety_dict[self.campaign_attributes['brand_safety_level']])
        except KeyError:
            self.create_campaign.page_should_contain('Level Two')

    @test_case()
    def assert_whitelist(self):
        self.create_campaign.open_whitelist()
        self.create_campaign.assert_list(self.campaign_attributes['whitelist'])

    @test_case()
    def assert_blacklist(self):
        self.create_campaign.open_blacklist()
        self.create_campaign.assert_list(self.campaign_attributes['blacklist'])

    @test_case()
    def assert_aoc_name(self):
        time.sleep(5)
        self.assert_attributes('aoc_custom')

    @test_case()
    def assert_aoc_cpm_value(self):
        self.assert_attributes('value')

    @test_case()
    def assert_uploaded_whitelist(self):
        self.create_campaign.open_whitelist()
        self.create_campaign.verify_uploads(self.campaign_attributes['whitelist_file'])

    @test_case()
    def assert_uploaded_blacklist(self):
        self.create_campaign.open_blacklist()
        self.create_campaign.verify_uploads(self.campaign_attributes['blacklist_file'])

    @test_case()
    def complete_flow_with_ctr(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_ctr(self.create_campaign.campaign_values)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign.campaign_attributes['goal_ctr'] = self.create_campaign.campaign_values['ctr_goal']
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)

    def complete_flow_helper(self):
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.fbs.wait_for_flights()

    @test_case()
    def complete_flow_with_future_dates(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_future_date(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_retargeting_xls(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_retargeting(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_optimized_xlsx(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_optimized(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def complete_flow_with_channel_xlsx(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_channel(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def date_ahead(self):
        self.create_campaign_page()
        self.create_campaign.enter_start_date(DXDate().date_after_two_days())
        self.create_campaign.enter_end_date(DXDate().todays_date())
        self.create_campaign.submit()

    def date_helper(self):
        self.create_campaign.page_should_contain(self.create_campaign.date_ahead_msgs)

    @test_case()
    def start_date_exceeds(self):
        self.date_helper()

    @test_case()
    def end_date_before(self):
        self.date_helper()

    @test_case()
    def create_campaign_with_completed_ad_views(self):
        self.search_page_campaign_click()
        self.fill_advertiser_details('Mobile')
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_ad_views(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def assert_aoc_number_name(self):
        self.assert_attributes('aoc_custom')

    @test_case()
    def assert_aoc_rate(self):
        self.assert_attributes('aoc_rate')

    @test_case()
    def verify_max_performance_distribution(self):
        contents = ['model', 'activity', 'pixel', 'tag_server', 'filter', 'tag_id']
        for element in contents:
            self.create_campaign.click_element(getattr(self.create_campaign, element))

    @test_case()
    def verify_max_ctr(self):
        self.create_campaign.click_campaign_objective_ctr()
        self.create_campaign.click_element(self.create_campaign.campaign_goal_ctr)

    def campaign_objective_helper(self, page_object):
        page_object.click_campaign_objective_ctr()
        page_object.click_campaign_objective_distribution()
        page_object.click_campaign_objective_performance()

    @test_case()
    def verify_campaign_objective(self):
        self.campaign_objective_helper(self.create_campaign)

    @test_case()
    def verify_campaign_objective_under_mobile(self):
        self.search_page_campaign_click()
        self.fill_advertiser_details('Mobile')
        self.campaign_objective_helper(self.create_campaign)
        self.create_campaign.click_campaign_objective_ad_views()

    @test_case()
    def verify_campaign_objective_under_video(self):
        self.search_page_campaign_click()
        self.fill_advertiser_details('Video')
        self.campaign_objective_helper(self.create_campaign)
        self.create_campaign.click_campaign_objective_ad_views()

    @test_case()
    def verify_add_on_cost_contents(self):
        self.create_campaign.expand_add_on_cost()
        contents = ['View Change History', 'Name', 'Rate', 'Fee Type', 'Billable', 'DataXu Marketplace']
        for content in contents:
            self.create_campaign.page_should_contain(content)
        assert self.create_campaign.is_element_present(self.create_campaign.new_add_on_cost)
        self.create_campaign.click_new_aoc()
        for element in ['add_on_cost_name', 'add_on_cost_rate', 'add_on_cost_billable', 'remove_add_on_cost']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_budget_spending(self):
        for element in ['cost_model', 'cpa_goal', 'order_budget', 'campaign_cpm', 'campaign_cogs', 'campaign_margin']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_cost_model(self):
        for option in ['CPA', 'CPM']:
            self.create_campaign.select_cost_model(option)

    @test_case()
    def verify_tactics(self):
        self.create_campaign.page_should_contain('Default')

    @test_case()
    def verify_tactics_contents(self):
        contents = ['Tactic name', 'Budget', 'Impression Cap']
        for content in contents:
            self.create_campaign.page_should_contain(content)
        assert self.create_campaign.is_element_present(self.create_campaign.new_tactics)
        self.create_campaign.click_add_new_tactic()
        for element in ['tactic_name', 'tactics_budget', 'tactics_impression', 'remove_tactics']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_tactics_name_contents(self):
        contents = ['Retargeting', 'Optimized', 'GeoTargeting', 'Channel', 'Custom...']
        for content in contents:
            self.create_campaign.page_should_contain(content)

    @test_case()
    def verify_external_ids_contents(self):
        self.create_campaign.expand_external_ids()
        assert self.create_campaign.is_element_present(self.create_campaign.new_external_ids)
        self.create_campaign.click_new_external_id()
        for element in ['external_id_source', 'external_id_value', 'remove_external_id']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))
        contents = [
                    'RMX', 'DFA', 'Atlas', 'BlueKai', 'WURFL', 'MediaMind',
                    'Facebook', 'Facebook Campaign', 'Facebook Page Post Ad'
                    ]
        for content in contents:
            self.create_campaign.page_should_contain(content)

    @test_case()
    def verify_geographic_targeting_section(self):
        for element in ['geo_target_type', 'country_available_search', 'country_available', 'country_selected']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))
        countries = [
                     'United States', 'Brazil', 'Canada', 'France', 'Germany',
                     'Great Britain', 'Ireland', 'Italy', 'Poland', 'Spain'
                    ]
        for content in countries:
            self.create_campaign.page_should_contain(content)

    @test_case()
    def verify_buttons_in_geographic_targeting(self):
        self.create_campaign.select_avail_countries('Brazil')
        self.create_campaign.click_move_selected_country()
        self.create_campaign.assert_geographic_selected_country(self.create_campaign.country_selected, 'Brazil')
        self.create_campaign.select_selected_countries('Brazil')
        self.create_campaign.click_remove_selected_country()
        self.create_campaign.assert_geographic_selected_country(self.create_campaign.country_available, 'Brazil')
        self.create_campaign.click_remove_selected_country()
        countries = [
                     'United States', 'Brazil', 'Canada', 'France', 'Germany',
                      'Great Britain', 'Ireland', 'Italy', 'Poland', 'Spain'
                    ]
        self.create_campaign.click_move_all_selected_countries()
        self.create_campaign.assert_geographic_selected_country(self.create_campaign.country_selected, None, countries)
        self.create_campaign.click_remove_all_selected_countries()
        self.create_campaign.assert_geographic_selected_country(self.create_campaign.country_available, None, countries)

    @test_case()
    def verify_search_in_geographic_targeting(self):
        self.create_campaign.search_avail_countries('India')
        self.create_campaign.assert_geographic_selected_country(self.create_campaign.country_available, 'India')

    @test_case()
    def verify_postal_codes_in_geo_target(self):
        self.select_specify_region_within()
        self.create_campaign.select_area_type(2)
        contents = [
                    'geo_target_type', 'geo_target_country_id', 'geo_target_area_type',
                     'postal_code_group_name', 'postal_code_group_submit'
                     ]
        for element in contents:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_geofenced_in_geo_target(self):
        self.create_campaign.select_geo_targeting_type(0)
        elements = [
                    'geo_target_type', 'geofenced_search', 'geofenced_available',
                    'geofenced_applied', 'geofenced_file', 'geofenced_name', 'geofenced_submit'
                    ]
        for element in elements:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_blacklist_section(self):
        self.create_campaign.expand_blacklist()
        for element in ['use_blacklist', 'blacklist_domains', 'blacklist_domains_file']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_whitelist_section(self):
        self.create_campaign.expand_brand_safety()
        self.create_campaign.click_brand_safety_level_four()
        self.create_campaign.expand_whitelist()
        for element in ['whitelist_domains', 'whitelist_domains_file']:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_brandsafety_section(self):
        self.create_campaign.expand_brand_safety()
        self.create_campaign.page_should_contain('Defaults to Level 2')
        self.create_campaign.expand_brand_safety()
        for content in range(1, 18):
            self.create_campaign.page_should_contain(self.create_campaign.contents[content])
        elements = [
                    'brand_safety_level_one', 'brand_safety_level_two',
                    'brand_safety_level_three', 'brand_safety_level_four'
                    ]
        for element in elements:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def fill_fields_with_limit_data(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['objective'] = 'performance'
        self.create_campaign.campaign_attributes['activity_pixel'] = 1
        self.create_campaign.campaign_attributes['tag_id'] = DXConstant().four_len_value
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        time.sleep(5)
        self.create_campaign.page_should_contain(self.create_campaign.limit_msgs['activity'])

    @test_case()
    def blank_ctr_goal(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['objective'] = 'ctr'
        self.create_campaign.campaign_attributes['goal_ctr'] = ''
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        time.sleep(5)
        self.create_campaign.page_should_contain(self.create_campaign.blank_msgs['ctr_goal'])

    @test_case()
    def special_chars_ctr_goal(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['goal_ctr'] =  DXConstant().special_char
        self.create_campaign.campaign_attributes['objective'] = 'ctr'
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.page_should_contain(self.create_campaign.special_character_msgs['ctr_goal'])

    @test_case()
    def fill_activity_with_max_limit(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_max_limit(self.create_campaign.campaign_values)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.create_campaign.page_should_contain(self.create_campaign.campaign_attributes['aoc_custom'])

    @test_case()
    def aoc_name_exceeding_limit(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['objective'] = 'distribution'
        self.create_campaign.campaign_attributes['aoc_name'] = 'Custom...'
        activity = DXConstant().activity_name + self.create_campaign.get_random_digits(248)
        self.create_campaign.campaign_attributes['aoc_custom'] = activity
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.page_should_contain(self.create_campaign.limit_msgs['aoc'])

    @test_case()
    def fill_cpm_with_max_limit(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_cpm_max_limit(self.create_campaign.campaign_values)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.create_campaign.page_should_contain(self.create_campaign.campaign_attributes['aoc_custom'])

    @test_case()
    def fill_cpm_alphanumeric_value(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['objective'] = 'distribution'
        self.create_campaign.campaign_attributes['aoc_rate'] = DXConstant().alphanumeric_value
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.page_should_contain(self.create_campaign.alphanumeric_value_msgs['aoc_rate'])

    @test_case()
    def fill_tactics_name_with_limit(self):
        self.create_campaign_page()
        self.create_campaign.campaign_attributes['objective'] = 'distribution'
        self.create_campaign.campaign_attributes['tactics'] = 'Custom...'
        tactics = DXConstant().tactics_name + self.create_campaign.get_random_digits(249)
        self.create_campaign.campaign_attributes['tactics_value'] = tactics
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.page_should_contain(self.create_campaign.limit_msgs['tactics'])

    @test_case()
    def fill_tactics_name_with_limit_data(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_tactics(self.create_campaign.campaign_values)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.go_to_campaign_show_page()
        self.create_campaign.page_should_contain(self.create_campaign.campaign_attributes['tactics_value'])

    @test_case()
    def fill_fields_with_facebook_campaign(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_facebook_campaign(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def fill_fields_with_brand_safety_one(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().fill_fields_with_brand_safety_one(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def verify_bulk_assign_pixels(self):
        assert self.create_campaign.is_element_present(self.create_campaign.bulk_assign_pixel)

    @test_case()
    def verify_bulk_assign_pixels_contents(self):
        self.create_campaign.click_bulk_assign_click()
        self.create_campaign.wait_for_bulk_assign_pixel()
        self.create_campaign.page_should_contain('Bulk Assign Pixels')
        contents = ['bulk_available_search', 'bulk_available_activities', 'pixel_type_value', 'pixel_type_filter', 'add_pixel']
        for element in contents:
            assert self.create_campaign.is_element_present(getattr(self.create_campaign, element))

    @test_case()
    def verify_bulk_pixel_type(self):
        for option in ['Conversion Pixel', 'Learning Pixel']:
            self.create_campaign.select_bulk_pixel_type(option)

    @test_case()
    def verify_no_new_textbox_appear(self):
        self.create_campaign.select_bulk_pixel_type('Learning Pixel')
        assert not self.create_campaign.find_element(self.create_campaign.pixel_type_value).is_selected()

    @test_case()
    def verify_new_textbox_appear(self):
        self.create_campaign.select_bulk_pixel_type('Conversion Pixel')
        assert self.create_campaign.is_element_present(self.create_campaign.pixel_type_learning)

    @test_case()
    def verify_search_activities(self):
        self.create_campaign.search_available_bulk_pixel('activity')
        activity = str(self.create_campaign.get_first_activity())
        assert activity.find('activity') != -1, 'Searching activity not present'

    @test_case()
    def verify_conversion_value_char_data(self):
        self.create_campaign.search_available_bulk_pixel('')
        activity=self.create_campaign.get_first_activity()
        self.create_campaign.select_one_available_activity(activity)
        self.create_campaign.select_bulk_pixel_type('Conversion Pixel')
        self.create_campaign.enter_bulk_conversion_pixel_value('abcde')
        self.create_campaign.click_add_pixel()
        element = self.create_campaign.find_element(self.create_campaign.first_value_field)
        assert str(element.get_attribute('placeholder')) == '0.0', 'Conversion value error'

    def conversion_helper(self, pixel):
        self.create_campaign.click_bulk_assign_click()
        self.create_campaign.wait_for_bulk_assign_pixel()
        self.create_campaign.search_available_bulk_pixel('test-activity')
        time.sleep(5)
        activity = self.create_campaign.get_first_activity()
        self.create_campaign.search_available_bulk_pixel('')
        self.create_campaign.select_one_available_activity(activity)
        self.create_campaign.select_bulk_pixel_type(pixel)
        return activity

    @test_case()
    def verify_conversion_value_special_chars(self):
        self.create_campaign.click_remove_activity()
        self.conversion_helper('Conversion Pixel')
        self.create_campaign.enter_bulk_conversion_pixel_value('!@#$%^&')
        self.create_campaign.click_add_pixel()
        element = self.create_campaign.find_element(self.create_campaign.second_value_field)
        assert str(element.get_attribute('placeholder')) == '0.0', 'Conversion value error'

    @test_case()
    def popup_should_close(self):
        self.create_campaign.click_bulk_assign_click()
        self.create_campaign.wait_for_bulk_assign_pixel()
        self.create_campaign.close_popup()

    @test_case()
    def assign_learning_pixel_type(self, pixel_type = 'Learning Pixel'):
        if self.create_campaign.is_element_present(self.create_campaign.campaign_name):
            activity =self.conversion_helper(pixel_type)
            if pixel_type == 'Conversion Pixel':
                self.create_campaign.enter_bulk_conversion_pixel_value('19')
            self.create_campaign.click_add_pixel()
            self.campaign_attributes = CampaignTestHelper().get_campaign_with_objective_performance(self.create_campaign.campaign_values)
            self.campaign_attributes['activity_pixel'] = None
            self.complete_flow_helper()
        self.go_to_campaign_show_page()
        self.go_to_campaign_edit()
        self.create_campaign.page_should_contain(activity)
        assert str(self.create_campaign.get_first_pixel_type()) == pixel_type, '%s not present'%(pixel_type)

    @test_case()
    def assign_conversion_pixel_type(self):
        self.assign_learning_pixel_type('Conversion Pixel')

    @test_case()
    def external_id_value_blank(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_blank_external_value(self.create_campaign.campaign_values)
        self.complete_flow_helper()
        self.go_to_campaign_show_page()
        self.create_campaign.page_should_contain(self.create_campaign.campaign_attributes['source'])

    @test_case()
    def edit_external_id_value(self):
        self.go_to_campaign_edit()
        self.edit_campaign.select_external_id_source('DFA')
        self.edit_campaign.enter_external_id_value('19')
        self.edit_campaign.submit()
        self.edit_campaign.page_should_contain('DFA')
        self.edit_campaign.page_should_contain('19')

    def split_messages(self, message):
        msg = (str(message)).split(',')
        return msg

    @test_case()
    def geofenced_region_valid_file(self):
        self.create_campaign.select_geo_targeting_type(0)
        self.create_campaign.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/domains_list/valid_geohash_upload.csv')
        geofence_name = DXConstant().geofenced_group_name + str(uuid.uuid4()) + '193'
        for i in range(1,42):
            geofence_name += '13579'
        self.create_campaign.enter_geofenced_group_name(geofence_name)
        self.create_campaign.click_geofenced_submit()
        time.sleep(10)
        self.create_campaign.page_should_contain(self.create_campaign.geofenced_msgs['valid'])

    @test_case()
    def geofenced_invalid_name(self):
        geofence_name = DXConstant().geofenced_group_name + str(uuid.uuid4())
        for i in range(1,43):
            geofence_name += '13579'
        self.create_campaign.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/domains_list/valid_geohash_upload.csv')
        self.create_campaign.enter_geofenced_group_name(geofence_name)
        self.create_campaign.click_geofenced_submit()
        self.create_campaign.wait_for_upload_error_message()
        messages = self.split_messages(self.create_campaign.geofenced_msgs['invalid_name'])
        for message in messages:
            self.create_campaign.page_should_contain(message)

    @test_case()
    def geofenced_region_invalid_file(self):
        self.create_campaign.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/domains_list/Cute_XU.xls')
        self.create_campaign.click_geofenced_submit()
        self.create_campaign.wait_for_upload_error_message()
        time.sleep(10)
        messages = self.split_messages(self.create_campaign.geofenced_msgs['invalid_csv'])
        for message in messages:
            self.create_campaign.page_should_contain(message)

    @test_case()
    def geofenced_region_alphanumeric_name(self):
        self.create_campaign.upload_geofenced_file(os.path.dirname(__file__)+ '/../../../data/domains_list/valid_geohash_upload.csv')   
        geofence_name = DXConstant().geofenced_group_name + str(uuid.uuid4())
        self.create_campaign.enter_geofenced_group_name(geofence_name)
        self.create_campaign.click_geofenced_submit()
        time.sleep(5)
        self.create_campaign.page_should_contain(self.create_campaign.geofenced_msgs['valid'])

    @test_case()
    def blacklist_info_icon(self):
        assert self.create_campaign.hover_and_visible('blacklist_info_icon', 'blacklist_popover')

    @test_case()
    def whitelist_info_icon(self):
        self.create_campaign.expand_brand_safety()
        self.create_campaign.click_brand_safety_level_four()
        assert self.create_campaign.hover_and_visible('whitelist_info_icon', 'whitelist_popover')

    @test_case()
    def campaign_with_brand_safety_three(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_brand_safety_three(self.create_campaign.campaign_values)
        self.complete_flow_helper()

    @test_case()
    def verify_blank_csv_present(self):
        self.create_campaign.page_should_contain(self.create_campaign.campaign_success_msg)
        time.sleep(10)
        self.create_campaign.go_to_link(self.create_campaign.campaign_attributes['campaign_name'])

    def assert_lists(self):
        self.assert_uploaded_blacklist()
        self.assert_uploaded_whitelist()

    def edit_blacklist_whitelist(self, campaign, file):
        campaign = CampaignTestHelper().set_campaign_attributes(campaign, self.campaign_attributes)
        campaign = self.fill_create_campaign_fields(campaign, campaign.campaign_attributes)
        self.go_to_campaign_show_page()
        self.assert_lists()
        self.go_to_campaign_edit()
        self.campaign_attributes['whitelist_file'] = campaign.campaign_values[file]
        self.campaign_attributes['blacklist_file'] = campaign.campaign_values[file]
        self.edit_campaign.upload_whitelist(os.path.dirname(__file__)+ '/../../../data/domains_list/' + self.campaign_attributes['whitelist_file'])
        self.edit_campaign.upload_blacklist(os.path.dirname(__file__)+ '/../../../data/domains_list/' + self.campaign_attributes['blacklist_file'])
        self.edit_campaign.submit()
        self.show_campaign.wait_for_loading()
        self.assert_lists()

    @test_case()
    def updated_blacklist_whitelist(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_updated_xls(self.create_campaign.campaign_values)
        self.edit_blacklist_whitelist(self.create_campaign, 'new_xls_file')

    @test_case()
    def deleted_blacklist_whitelist(self):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_deleted_xls(self.create_campaign.campaign_values)
        self.edit_blacklist_whitelist(self.create_campaign, 'xls_file')

    @test_case()
    def override_blacklist_whitelist(self):
        self.assert_lists()

    @test_case()
    def fill_fbs_details(self):
        self.fbs.wait_for_flights()
        flight_name = DXConstant().test_flight_name + str(uuid.uuid4())
        self.fbs.fill_description(flight_name)
        self.fbs.type_bid(DXConstant().flight_bid)
        self.fbs.click_on_save_continue()
        self.create_flight.wait_for_flight_details()
        self.create_flight.expand_lang_targeting()
        time.sleep(5)
        assert self.create_flight.find_element(self.create_flight.inherit_lang_targeting).is_selected()
        return flight_name

    @test_case()
    def lang_target_base_settings(self ,base_type):
        self.create_campaign_page()
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_lang_targeting(self.create_campaign.campaign_values, base_type)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        flight = self.fill_fbs_details()
        if base_type == 1:
            self.create_flight.page_should_contain('Browser Setting')
        elif base_type == 2:
            self.create_flight.page_should_contain('Content Language')
        elif base_type == 3:
            self.create_flight.page_should_contain('Either Browser or Content')
        self.create_flight.page_should_contain('English')

    @test_case()
    def edit_lang_target_base_settings(self):
        self.create_campaign_page()
        base_type = 1
        self.campaign_attributes = CampaignTestHelper().get_campaign_with_lang_targeting(self.create_campaign.campaign_values, base_type)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        flight = self.fill_fbs_details()
        self.create_flight.page_should_contain('Browser Setting')
        self.create_flight.page_should_contain('English')
        self.create_flight.click_save_exit()
        self.show_campaign.wait_for_loading()
        self.go_to_campaign_edit()
        self.edit_campaign.select_lang_targeting_selected('English')
        self.edit_campaign.click_remove_selected_lang()
        self.edit_campaign.select_lang_targeting('Spanish')
        self.edit_campaign.click_move_selected_lang()
        self.edit_campaign.submit()
        self.create_flight.go_to_link(flight)
        self.create_flight.go_to_link('Edit')
        self.create_flight.wait_for_flight_details()
        for content in ['Browser Setting', 'Spanish']:
            self.create_flight.page_should_contain(content)

    @test_case()
    def verify_applied_country(self):
        self.create_campaign_page()
        self.create_campaign.wait_for_campaign_details()
        countries = ['Brazil', 'Canada', 'France', 'Germany', 'Great Britain',
                     'Ireland', 'Italy', 'Poland', 'Spain']
        for country in countries:
            self.create_campaign.select_avail_countries(country)
        self.create_campaign.click_move_selected_country()
        self.campaign_attributes = CampaignTestHelper().get_campaign_without_geo_target(self.create_campaign.campaign_values)
        self.create_campaign = CampaignTestHelper().set_campaign_attributes(self.create_campaign, self.campaign_attributes)
        self.create_campaign = self.fill_create_campaign_fields(self.create_campaign, self.create_campaign.campaign_attributes)
        self.create_campaign.go_to_link(self.create_campaign.campaign_attributes['campaign_name'])
        self.go_to_campaign_edit()

    @test_case()
    def verify_applied_country_on_edit_page(self, country):
        self.edit_campaign.assert_geographic_selected_country(self.edit_campaign.country_selected, country)        
