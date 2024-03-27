from base.dx import Dx


class AgenciesListPage(Dx):
    def click_on_new_agency_button(self):
        self.click_element(self.new_agency_button)
        
    def filter_agency_name_in_filterbox(self, agency_name):
        self.clear_and_send_value(agency_name, self.search_filter_agency)    
        
    def click_edit_icon(self, agency_name):
        agency_name_id = self.get_id_from_link(agency_name)
        edit_icon_loc = "a[title='Edit'][href*='{0}']".format(agency_name_id)
        self.click_element(edit_icon_loc)

    def click_delete_icon(self, agency_name):
        agency_name_id = self.get_id_from_link(agency_name)
        edit_icon_loc = "a[title='Delete'][href*='{0}']".format(agency_name_id)
        self.click_element(edit_icon_loc)

    def select_agency_group(self, agency_group, method='label'):
        self.select_option(self.pick_agency_group, agency_group, method)

    def click_first_edit_icon(self):
        self.click_element(self.edit_icon)

    def click_first_delete_icon(self):
        self.click_element(self.delete_icon)

    def click_first_agency(self):
        self.click_element(self.agency_link)
