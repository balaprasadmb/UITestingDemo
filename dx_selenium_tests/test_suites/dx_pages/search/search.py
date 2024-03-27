from base.dx import Dx

class SearchPage(Dx):

    def click_search_icon(self):
        self.click_element(self.search_icon)

    def click_creative_link(self):
        self.click_element(self.click_creative)

    def click_campaign_link(self):
        self.click_element(self.click_campaign)

    def click_first_campaign(self):
        self.click_element(self.click_first_campaign_link)

    def click_audience_link(self):
        self.click_element(self.click_audience)

    def click_activity_tab(self):
        self.click_element(self.activity_tab)
    
    def click_inventory_link(self):
        self.click_element(self.click_inventory)

    def click_logo(self):
        self.click_element(self.logo)

    def wait_for_campaign_link(self):
        self.wait_till_visible(self.click_campaign[0], self.click_campaign[1])
