from base.dx import Dx

class GuaranteedInventoryShowPage(Dx):
    def click_on_advertiser_link(self):
        self.click_element(self.advertiser_link)
    
    def click_on_default_creative_name(self):
        self.click_element(self.default_creative_name)
        
    def click_on_edit_guaranteed_media_button(self):
        self.click_element(self.edit_guaranteed_media_button)
