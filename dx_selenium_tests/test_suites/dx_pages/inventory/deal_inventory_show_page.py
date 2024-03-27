from base.dx import Dx

class DealInventoryShowPage(Dx):
    def click_on_deals_link(self):
        self.click_element(self.deals_link)
    
    def click_on_edit_deal_button(self):
        self.click_element(self.edit_deal_button)
