from base.dx import Dx

class AgencyGroupDetails(Dx):
    def go_to_list_page(self):
        self.click_element(self.agency_group_list_page)

    def click_add_agency(self):
        self.click_element(self.add_agency)

    def click_edit_details(self):
        self.click_element(self.edit_details)
