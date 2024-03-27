from selenium.webdriver.common.keys import Keys
from base.dx import Dx

class CreativeList(Dx):
    
    def select_advertiser(self, advertiser):
        self.click_element(self.advertiser_click)
        self.fill_field(self.advertiser_input, advertiser)
        self.fill_field(self.advertiser_input, Keys.ENTER)
    
    def search_filters(self, value):
        self.send_keys(self.filters, value)
    
    def click_new_creatives(self):
        self.click_element(self.new_creative_button)
    
    def click_select_all(self):
        self.click_element(self.select_all)
    
    def click_first_checkbox(self):
        self.click_element(self.first_creative_checkbox)
    
    def click_first_creative(self):
        self.click_element(self.first_creative_link)
    
    def click_get_rmx_id(self):
        self.click_element(self.get_rmx_id)
    
    def close_rmx_id_popup(self):
        self.click_element(self.close_rmx_ids_popup)

    def wait_for_creatives_list(self):
        self.wait_till_visible(self.creatives_view[0], self.creatives_view[1], 30)

    def get_first_creative(self):
        element = self.find_element(self.first_creative_link)
        creative = str(element.get_attribute('innerHTML'))
        creative = creative.replace('<wbr>', '')
        return creative.strip()
