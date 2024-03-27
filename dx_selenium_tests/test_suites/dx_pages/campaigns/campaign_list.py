from base.dx import Dx
from selenium.webdriver.common.keys import Keys

class CampaignList(Dx):
    
    def click_orgnization_dropdown(self):
        self.click_element(self.select_org)
        self.wait_till_visible('css', '.chzn-drop')
    
    def select_orgnization(self, organization):
        self.click_orgnization_dropdown()
        for value in [organization, Keys.TAB]:
            self.fill_field(self.search_org, value)
    
    def click_upload_new_flights(self):
        self.click_element(self.select_org)
    
    def click_upload_attribution_data(self):
        self.click_element(self.upload_attribution_data)
    
    def click_export_all_flights(self):
        self.click_element(self.export_all_flights)
    
    def filter_campaigns(self ,value):
        self.fill_field(self.campaign_filter, value)
    
    def click_new_campaign(self):
        self.click_element(self.new_campaign_button)
    
    def click_new_campaign_link(self):
        self.click_element(self.new_campaign_link)
    
    def click_new_media(self):
        self.click_element(self.new_media_plan_link)
    
    def click_campaign_link(self):
        self.click_element(self.first_campaign_link)
    
    def click_actions(self):
        self.click_element(self.first_actions)
    
    def click_edit_link(self):
        self.click_element(self.first_edit)
    
    def click_copy_link(self):
        self.click_element(self.first_copy)
    
    def click_export_flights_link(self):
        self.click_element(self.first_export_flights)
    
    def view_status(self):
        self.click_element(self.first_status)
    
    def close_actions_box(self):
        self.click_element(self.first_actions_box_close)
    
    def edit_media_plan(self):
        self.click_element(self.edit)
