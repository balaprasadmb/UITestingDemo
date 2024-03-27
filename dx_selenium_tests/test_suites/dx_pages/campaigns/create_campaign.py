import csv
import xlrd
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from base.dx import Dx

class CreateCampaign(Dx):
    def fill_fields(self, campaign_attributes):
        self.type_campaign_name(campaign_attributes['campaign_name'])
        self.enter_start_date(campaign_attributes['start_date'])
        self.enter_end_date(campaign_attributes['end_date'])
        self.enter_cpa_goal(campaign_attributes['cpa'])
        self.enter_budget(campaign_attributes['budget'])
        self.enter_cpm(campaign_attributes['cpm'])
        self.enter_cogs(campaign_attributes['cogs'])
        self.enter_margin(campaign_attributes['margin'])
        self.enter_insertion_order(campaign_attributes['order'])

        if campaign_attributes['objective'] == 'performance':
            self.click_campaign_objective_performance()

            if campaign_attributes['model']:
                self.select_attribution_model(campaign_attributes['model'])
            
            self.click_end_date()

            if campaign_attributes['activity_pixel']:
                self.select_activity_pixel(campaign_attributes['activity_pixel'])
                
                if campaign_attributes['pixel_type']:
                     self.select_pixel_type(campaign_attributes['pixel_type'])

                if campaign_attributes['pixel_type'] == 'Conversion Pixel':
                     self.enter_conversion_pixel_value(campaign_attributes['pixel_value'])

                self.enter_filters(campaign_attributes['filters_value'])

                if campaign_attributes['tag_server']:
                     self.select_tag_server(campaign_attributes['tag_server'])
                self.enter_tag_id(campaign_attributes['tag_id'])
        elif campaign_attributes['objective'] == 'ctr':
            self.click_campaign_objective_ctr()
            self.wait_till_visible('id', 'campaign_goal_ctr')
            self.enter_goal_ctr(campaign_attributes['goal_ctr'])

        elif campaign_attributes['objective'] == 'distribution':
            self.click_campaign_objective_distribution()
        
        elif campaign_attributes['objective'] == 'views':
            self.click_campaign_objective_ad_views()

        self.click_add_new_tactic()
        self.click_end_date()
        if campaign_attributes['tactics']:
            self.select_tactic_name(campaign_attributes['tactics'])
            if campaign_attributes['tactics'] == 'Custom...':
                  self.enter_cutom_value(campaign_attributes['tactics_value'])
            self.enter_tactics_budget(campaign_attributes['tactics_budget'])
            self.enter_impression(campaign_attributes['icaps'])

        self.expand_add_on_cost()
        self.click_new_aoc()
        self.click_end_date()
        if campaign_attributes['aoc_name']:
            self.select_aoc_name(campaign_attributes['aoc_name'])
            self.click_end_date()

            if campaign_attributes['aoc_name'] == 'Custom...':
                self.enter_cutom_aoc_value(campaign_attributes['aoc_custom'])
            self.click_aoc_rate()
            self.enter_aoc_rate(campaign_attributes['aoc_rate'])

            if campaign_attributes['fee_type']:
                self.select_fee_type(campaign_attributes['fee_type'])

            if campaign_attributes['is_billable']:
                self.click_billable()

            if campaign_attributes['is_marketpalce']:
                self.click_is_marketplace()

        self.expand_external_ids()
        self.click_new_external_id()
        if campaign_attributes['source']:
            self.select_external_id_source(campaign_attributes['source'])
            self.enter_external_id_value(campaign_attributes['source_value'])

        self.expand_lang_targeting()
        if campaign_attributes['base_lang_target']:
            self.select_base_lang_targeting(campaign_attributes['base_lang_target'])

        if campaign_attributes['lang_target']:
            self.select_lang_targeting(campaign_attributes['lang_target'])
            self.click_move_selected_lang()

        if campaign_attributes['geo_target_type']:
            self.select_geo_targeting_type(campaign_attributes['geo_target_type'])
            if campaign_attributes['geo_target_type'] == 2:
                self.select_geo_target_country(campaign_attributes['geo_target_type'])
            if campaign_attributes['geo_target_type'] == 0:
                self.upload_geofenced_file(campaign_attributes['geofenced_file'])
                self.enter_geofenced_group_name(campaign_attributes['geofenced_group_name'])
                self.click_geofenced_submit()

        if campaign_attributes['geo_target']:
            self.select_avail_countries(campaign_attributes['geo_target'])
            self.click_move_selected_country()

        self.expand_brand_safety()
        if campaign_attributes['brand_safety_level']:

            if campaign_attributes['brand_safety_level'] == '1':
                self.click_brand_safety_level_one()

            if campaign_attributes['brand_safety_level'] == '2':
                self.click_brand_safety_level_two()

            if campaign_attributes['brand_safety_level'] == '3':
                self.click_brand_safety_level_three()

            if campaign_attributes['brand_safety_level'] == '4':
                self.click_brand_safety_level_four()
                self.expand_whitelist()
                if campaign_attributes['whitelist']:
                    self.enter_whitelist(campaign_attributes['whitelist'])
                if campaign_attributes['whitelist_file']:
                    self.upload_whitelist(os.path.dirname(__file__)+ '/../../../data/domains_list/' + campaign_attributes['whitelist_file'])

        if campaign_attributes['blacklist']:
            self.expand_blacklist()
            self.enter_blacklist(campaign_attributes['blacklist'])

        if campaign_attributes['blacklist_file']:
            self.expand_blacklist()
            self.upload_blacklist(os.path.dirname(__file__)+ '/../../../data/domains_list/' + campaign_attributes['blacklist_file'])
        
        self.submit()
        return self

    def type_campaign_name(self, campaign):
        self.wait_till_visible('id', 'campaign_name')
        self.fill_field(self.campaign_name, campaign)

    def enter_start_date(self, start_date):
        self.fill_field(self.campaign_start_date, start_date)

    def click_start_date(self):
        self.click_element(self.campaign_start_date)

    def enter_end_date(self, end_date):
        self.fill_field(self.campaign_end_date, end_date)
    
    def enter_insertion_order(self, value):
        self.fill_field(self.insertion_order, value)

    def click_end_date(self):
        self.click_element(self.campaign_end_date)

    def select_cost_model(self, value):
        self.select_option(self.cost_model, value)

    def enter_cpa_goal(self, cpa):
        self.send_keys(self.cpa_goal, cpa)

    def enter_budget(self, budget):
        self.send_keys(self.order_budget, budget)

    def enter_cpm(self, cpm):
        self.send_keys(self.campaign_cpm, cpm)

    def enter_cogs(self, cogs):
        self.send_keys(self.campaign_cogs, cogs)

    def enter_margin(self, margin):
        self.send_keys(self.campaign_margin, margin)
    
    def click_auto_cruise_control(self):
        self.click_element(self.cruise_control_auto)
    
    def click_adhere_to_tactic(self):
        self.click_element(self.cruise_control_adhere)

    def click_campaign_objective_performance(self):
        self.click_element(self.campaign_objective_performance)

    def select_attribution_model(self, value):
        self.select_option(self.model, value)

    def select_activity_pixel(self, index):
        self.select_option(self.activity, index, 'index')

    def select_pixel_type(self, pixel):
        self.select_option(self.pixel, pixel)

    def enter_conversion_pixel_value(self, value):
        self.send_keys(self.pixel_value, value)

    def enter_filters(self, value):
        self.send_keys(self.filter, value)

    def select_tag_server(self, value):
        self.select_option(self.tag_server, value)

    def enter_tag_id(self, value):
        self.fill_field(self.tag_id, value)

    def click_bulk_assign_click(self):
        self.click_element(self.bulk_assign_pixel)

    def search_available_bulk_pixel(self, value):
        self.send_keys(self.bulk_available_search, value)

    def select_bulk_available_activities(self, activity_list):
        select = Select(self.find_element(self.bulk_available_activities))
        for activity in activity_list:
            select.select_by_visible_text(activity)
    
    def select_one_available_activity(self, activity):
        self.select_option(self.bulk_available_activities, activity)
    
    def enter_bulk_conversion_pixel_value(self, value):
        self.fill_field(self.pixel_type_learning, value)

    def click_add_pixel(self):
        self.wait_till_visible('css', '#bulk_pixel_assignment ~ div.ui-dialog-buttonpane > button')
        self.click_element(self.add_pixel)
    
    def click_remove_activity(self):
        self.click_element(self.remove_activity)

    def close_popup(self):
        self.click_element(self.bulk_assign_popup_close)

    def click_campaign_objective_ctr(self):
        self.click_element(self.campaign_objective_ctr)

    def enter_goal_ctr(self, value):
        self.fill_field(self.campaign_goal_ctr, value)

    def click_campaign_objective_distribution(self):
        self.click_element(self.campaign_objective_distribution)
    
    def click_campaign_objective_ad_views(self):
        self.click_element(self.campaign_objective_ad_views)

    def select_vendor(self, value):
        self.select_option(self.viewability_vendor, value)

    def select_category(self, value):
        self.select_option(self.category, value)

    def enter_impression_caps(self, value):
        self.fill_field(self.impression_caps, value)

    def click_add_new_tactic(self):
        self.click_element(self.new_tactics)

    def select_tactic_name(self, value):
        self.select_option(self.tactic_name, value)

    def enter_tactics_budget_second(self , value):
       self.fill_field(self.tactics_budget_second, value)

    def enter_cutom_value(self, value):
        self.fill_field(self.custom_field, value)

    def enter_tactics_budget(self, value):
        self.fill_field(self.tactics_budget, value)

    def enter_impression(self, value):
        self.fill_field(self.tactics_impression, value)

    def remove_tactics(self):
        self.click_element(self.remove_tactics)

    def click_new_aoc(self):
        self.click_element(self.new_add_on_cost)

    def click_view_change_histry(self):
        self.click_element(self.view_change_history)

    def select_aoc_name(self, value):
        self.select_option(self.add_on_cost_name, value)

    def enter_cutom_aoc_value(self, value):
        self.fill_field(self.add_on_cost_custom, value)
    
    def click_aoc_rate(self):
        self.click_element(self.add_on_cost_rate)
    
    def enter_aoc_rate(self, value):
        self.fill_field(self.add_on_cost_rate, value)

    def select_fee_type(self, value):
        self.select_option(self.add_on_cost_fee_type, value)

    def click_billable(self):
        self.click_element(self.add_on_cost_billable)

    def click_is_marketplace(self):
        self.click_element(self.add_on_cost_marketplace)

    def click_on_remove_aoc_button(self):
        self.click_element(self.remove_add_on_cost)

    def click_new_external_id(self):
        self.click_element(self.new_external_ids)

    def select_external_id_source(self,value):
        self.select_option(self.external_id_source, value)

    def enter_external_id_value(self, value):
        self.fill_field(self.external_id_value, value)

    def remove_external_id(self):
        self.click_element(self.remove_external_id)

    def select_base_lang_targeting(self, value):
        self.select_option(self.base_lang_targeting, value)

    def select_lang_targeting(self, value):
        self.select_option(self.lang_targeting_available, value)

    def click_move_selected_lang(self):
        self.click_element(self.move_selected_lang)

    def click_remove_selected_lang(self):
        self.click_element(self.remove_selected_lang)

    def click_move_all_selected_lang(self):
        self.click_element(self.move_all_selected_lang)

    def click_remove_all_selected_lang(self):
        self.click_element(self.remove_all_selected_lang)

    def select_lang_targeting_selected(self, value):
        self.select_option(self.lang_targeting_selected, value)

    def select_geo_targeting_type(self, value):
        self.select_option(self.geo_target_type, value, 'index')

    def search_avail_countries(self, value):
        self.send_keys(self.country_available_search, value)

    def select_avail_countries(self, value):
        self.select_option(self.country_available, value)

    def select_selected_countries(self, value):
        self.select_option(self.country_selected, value)

    def click_move_selected_country(self):
        self.click_element(self.move_selected_country)

    def click_remove_selected_country(self):
        self.click_element(self.remove_selected_country)

    def click_move_all_selected_countries(self):
        self.click_element(self.move_all_selected_country)

    def click_remove_all_selected_countries(self):
        self.click_element(self.remove_all_selected_country)

    def select_geo_target_country(self, value):
        self.select_option(self.geo_target_country_id, value)

    def select_area_type(self, value):
        self.select_option(self.geo_target_area_type, value ,'index')

    def search_avail_countries_dual(self, value):
        self.fill_field(self.dual_select_avail_search, value)

    def select_avail_countries_dual(self, value):
        self.select_option(self.dual_avail_country, value)

    def select_selected_countries_dual(self, value):
        self.select_option(self.dual_applied_country, value)
    
    def search_avail_countries_metro(self, value):
        self.fill_field(self.mc_select_avail_search, value)

    def select_avail_countries_metro(self, value):
        self.select_option(self.mc_avail_country, value)

    def select_selected_countries_metro(self, value):
        self.select_option(self.mc_applied_country, value)

    def upload_geofenced_file(self, value):
        self.fill_field(self.geofenced_file, value)

    def enter_geofenced_group_name(self, value):
        self.send_keys(self.geofenced_name, value)

    def click_geofenced_submit(self):
        self.click_element(self.geofenced_submit)
    
    def upload_postalcode_file(self, value):
        self.fill_field(self.postal_code_upload, value)

    def enter_postalcode_group_name(self, value):
        self.send_keys(self.postal_code_group_name, value)

    def click_postalcode_submit(self):
        self.click_element(self.postal_code_group_submit)

    def click_brand_safety_level_one(self):
        self.click_element(self.brand_safety_level_one)

    def click_brand_safety_level_two(self):
        self.click_element(self.brand_safety_level_two)

    def click_brand_safety_level_three(self):
        self.click_element(self.brand_safety_level_three)

    def click_brand_safety_level_four(self):
        self.click_element(self.brand_safety_level_four)

    def enter_whitelist(self, value):
        self.fill_field(self.whitelist_domains, value)

    def enter_blacklist(self, value):
        self.fill_field(self.blacklist_domains, value)

    def upload_whitelist(self, value):
        self.fill_field(self.whitelist_domains_file, value)

    def upload_blacklist(self, value):
        self.fill_field(self.blacklist_domains_file, value)

    def close_domains_popup(self):
        self.click_element(self.list_dialogue_close)

    def submit(self):
        self.click_element(self.create_campaign)

    def expand_impression_caps(self):
        self.click_element(self.impression)

    def enter_impression_caps(self, value):
        self.fill_field(self.impression_caps, value)

    def expand_tactics(self):
        self.click_element(self.tactics)

    def expand_add_on_cost(self):
        self.click_element(self.add_on_cost)

    def expand_external_ids(self):
        self.click_element(self.external_ids)

    def expand_lang_targeting(self):
        self.click_element(self.lang_targeting)

    def expand_brand_safety(self):
        self.click_element(self.brand_safety)

    def expand_whitelist(self):
        self.click_element(self.whitelist)

    def expand_blacklist(self):
        self.click_element(self.blacklist)

    def wait_for_campaign_details(self):
        self.wait_till_visible(self.campaign_details[0], self.campaign_details[1])

    def wait_for_bulk_assign_pixel(self):
        self.wait_till_visible(self.bulk_assign_pixel_popup[0], self.bulk_assign_pixel_popup[1])

    def wait_for_upload_error_message(self):
        self.wait_till_visible(self.geotargeting_upload_error[0], self.geotargeting_upload_error[1])

    def open_blacklist(self):
        self.click_element(self.blacklist_domains_link)
        self.wait_till_visible('css', self.domains_popup[1])
        self.wait_till_visible('css', '.ui-dialog-content.ui-widget-content>ul')

    def open_whitelist(self):
        self.click_element(self.whitelist_domains_link)
        self.wait_till_visible('css', self.domains_popup[1])
        self.wait_till_visible('css', '.ui-dialog-content.ui-widget-content>ul')

    def assert_list(self,domains):
        self.page_should_contain(domains)
        self.click_element(self.close_domains_popup)

    def verify_uploads(self, filename):
        splits = filename.split('.')
        filetype = splits[1]

        if filetype == "csv" or filetype == "txt":
            with open(os.path.dirname(__file__)+ '/../../../data/domains_list/' + filename, 'rb') as csvfile:
                csvreader = csv.reader(csvfile)
                for reader in csvreader:
                    self.page_should_contain(reader[0])
        elif filetype == "xls" or filetype == "xlsx":
            with xlrd.open_workbook(os.path.dirname(__file__)+ '/../../../data/domains_list/' + filename) as book:
                sheet=book.sheet_by_index(0)
                for row in range(sheet.nrows):
                    self.page_should_contain(sheet.cell(row,0).value)
        self.click_element(self.close_domains_popup)

    def select_bulk_pixel_type(self, value):
        self.select_option(self.pixel_type_value, value)

    def get_first_activity(self):
        select = Select(self.find_element(self.bulk_available_activities))
        for option in select.options:
            return option.text

    def get_first_pixel_type(self):
        select = Select(self.find_element(self.pixel))
        for option in select.options:
            if option.is_selected():
                return option.text

    def hover_and_visible(self, element, popover):
        ActionChains(self.driver).move_to_element(self.find_element(getattr(self, element))).perform()
        if EC.visibility_of_element_located(getattr(self, popover)):
            return True
        else:
            return False

    def assert_dropdown_options_not_in(self,loc,dropdown_option):
        widget=self.find_element(loc)
        select = Select(widget)
        for option in select.options:
            if option.text == dropdown_option:
                raise AssertionError

    def select_tactic_retargeting(self):
        self.select_tactic_name('Retargeting')

    def select_tactic_optimized(self):
        self.select_option(self.tactic_name_second, 'Optimized')

    def click_single_device(self):
        self.click_element(self.single_device_enabled)
        time.sleep(2)

    def click_high_precision(self):
        self.click_element(self.high_precision_enabled)

    def click_broad_reach(self):
        self.click_element(self.broad_reach_enabled)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)
    
    def get_investment_available_in_market(self):
        return self.get_content_text(self.investment_available_in_market)

    def get_impressions_available_in_market(self):
        return self.get_content_text(self.impressions_available_in_market)
    
    def get_impressions_budget(self):
        return self.get_content_text(self.impressions_budget)

    def click_oneview_popup_ok(self):
        self.click_element(self.oneview_popup_ok)

    def click_oneview_popup_cancel(self):
        self.click_element(self.oneview_popup_cancel)
