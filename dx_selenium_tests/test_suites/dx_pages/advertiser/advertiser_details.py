from base.dx import Dx


class AdvertiserDetailsPage(Dx):
    
    def go_to_advertiser_list_page(self):
        self.click_element(self.advertiser_list_page_link)

    def go_to_agency_group(self):
        self.click_element(self.agency_group_link)

    def go_to_first_agency_in_list(self):
        self.click_element(self.agency_list)

    def click_edit_details(self):
        self.click_element(self.edit_details_button)
