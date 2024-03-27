from base.dx import Dx
from configs.dx_constant import DXConstant
from selenium.webdriver import ActionChains
import time

class NewCampaign(Dx):
    def click_new_campaign_link(self):
        self.click_element(self.new_campaign_link)

    def type_advertiser(self, advertiser):
        self.wait_till_visible('id', 'dataxu_dialog')
        self.wait_till_visible('id', 'advertiser')
        self.clear_and_send_value(advertiser, self.advertiser)
        time.sleep(3)
        suggestion = self.find_element(self.suggestions)
        ActionChains(self.driver).move_to_element(suggestion).perform()
        self.click_element(self.suggestion_link)

    def submit(self):
        self.submit_form(self.online_campaign_submit)

    def click_ford_campaign_link(self):
        self.wait_till_visible('link text', DXConstant().new_advertiser_name)
        self.click_and_hold(self.ford_campaign_link)

    def select_campaign_currency(self, value):
        self.wait_till_visible('id', 'campaign_currency_id')
        self.select_option(self.campaign_currency, value)

    def select_campaign_channel(self , value):
        self.wait_till_visible('id', 'pick_media_type')
        self.select_option(self.campaign_channel, value)

    def select_campaign_inventory(self, value):
        self.select_option(self.inventory_type, value)

    def check_channel_visible(self):
        element = self.find_element(self.campaign_channel)
        if element.is_displayed():
            return True
        else:
            return False

    def close(self):
        self.click_element(self.close_popup)

    def new_campaign_body_click(self):
        self.click_element(self.new_online_campaign_body_link)

    def clear_advertiser(self):
        self.clear(self.advertiser)
