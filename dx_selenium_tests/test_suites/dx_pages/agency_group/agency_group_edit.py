from new_agency_group import NewAgencyGroup

class AgencyGroupEdit(NewAgencyGroup):
    def sort_segment_name(self):
        self.click_element(self.segment_name)

    def sort_external_id(self):
        self.click_element(self.external_id)

    def sort_cost(self):
        self.click_element(self.cost)

    def sort_price(self):
        self.click_element(self.price)

    def sort_inherited(self):
        self.click_element(self.inherited)
