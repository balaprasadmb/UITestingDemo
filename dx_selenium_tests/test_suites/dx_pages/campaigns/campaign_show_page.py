from base.dx import Dx

class CampaignShowPage(Dx):

    def click_advertiser_link(self):
        self.click_element(self.advertiser_link)

    def edit(self):
        self.click_element(self.edit_link)

    def view_all_campaigns(self):
        self.click_element(self.view_all_campaigns_link)

    def switch_to_campaigns_dashboard(self):
        self.click_element(self.dashboard_link)

    def export_flights(self):
        self.click_element(self.export_flights_button)

    def iab_quality_guidelines(self):
        self.click_element(self.iab_quality_guideline_link)

    def view_blacklist(self):
        self.click_element(self.blacklist_link)

    def view_whitelist(self):
        self.click_element(self.whitelist_link)

    def reports(self):
        self.click_element(self.reports_link)

    def blocked_publishers(self):
        self.click_element(self.blocked_publishers_link)

    def smart_assign_creatives(self):
        self.click_element(self.smart_assign_creatives_link)

    def bulk_upload_flights(self):
        self.click_element(self.bulk_upload_flights_buttons)

    def edit_budget_schedules(self):
        self.click_element(self.edit_budget_schedules_buttons)

    def add_flights(self):
        self.click_element(self.add_flights_buttons)

    def click_flights_link(self):
        self.click_element(self.flights_link)

    def click_creatives_link(self):
        self.click_element(self.creatives_link)

    def wait_for_loading(self):
        self.wait_till_visible(self.tactic_flight_table[0], self.tactic_flight_table[1])
