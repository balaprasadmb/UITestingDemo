from base.dx import Dx

class AgencyDetailsPage(Dx):
    
    def go_to_agency_list_page(self):
        self.click_element(self.agency_list_page_link)

    def go_to_agency_group(self):
        self.click_element(self.agency_group_link)

    def go_to_first_advertiser_in_list(self):
        self.click_element(self.advertiser_list)

    def add_new_advertiser(self):
        self.click_element(self.add_advertiser_button)

    def click_edit_details(self):
        self.click_element(self.edit_details_button)
