from base.dx import Dx

class FlightsShowPage(Dx):

    def click_advertiser_link(self):
        self.click_element(self.advertiser_link)

    def click_campaign_link(self):
        self.click_element(self.campaign_link)

    def edit(self):
        self.click_element(self.edit_link)

    def view_all_campaigns(self):
        self.click_element(self.view_all_campaigns_link)

    def click_creatives_link(self):
        self.click_element(self.creatives_link)

    def campaign_flight_budget_setup(self):
        self.click_element(self.campaign_flight_budget_setup_link)

    def view_blacklist(self):
        self.click_element(self.blacklist_link)

    def view_whitelist(self):
        self.click_element(self.whitelist_link)

    def wait_for_flight_basics(self):
        self.wait_till_visible(self.flight_basics[0], self.flight_basics[1])
