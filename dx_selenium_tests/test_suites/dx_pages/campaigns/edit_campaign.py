from base.dx import Dx
from selenium.webdriver.support.ui import Select

class EditCampaign(Dx):

    def type_campaign_name(self, campaign):
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

    def click_add_pixel(self):
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

    def click_new_external_id(self):
        self.click_element(self.new_external_ids)

    def select_external_id_source(self,value):
        self.select_option(self.external_id_source, value)

    def enter_external_id_value(self, value):
        self.fill_field(self.external_id_value, value)

    def remove_external_id(self):
        self.click_element(self.remove_external_id)

    def select_base_lang_targeting(self, value):
        self.select_option(self.select_base_lang_targeting, value)

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
        self.fill_field(self.geofenced_name, value)

    def click_geofenced_submit(self):
        self.click_element(self.geofenced_submit)

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

    def wait_for_details(self):
        self.wait_till_visible(self.campaign_details[0], self.campaign_details[1], 30)
