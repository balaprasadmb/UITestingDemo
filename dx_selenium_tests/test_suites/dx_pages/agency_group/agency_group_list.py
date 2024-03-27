from selenium.webdriver.common.by import By
from base.dx import Dx

class AgencyGroupList(Dx):
    def go_to_new_agency(self):
        self.click_element(self.new_agency_group_link)

    def go_to_agency_group(self, agency_group):
        agency_group_loc = (By.LINK_TEXT, agency_group)
        self.click_element(agency_group_loc)

    def click_edit_icon_with_agency_name(self, agency_group):
        agency_group_id = self.get_id_from_link(agency_group)
        edit_icon_loc = "a[title='Edit'][href*='{0}']".format(agency_group_id)
        self.click_element(edit_icon_loc)

    def click_delete_icon_with_agency_name(self, agency_group):
        agency_group_id = self.get_id_from_link(agency_group)
        edit_icon_loc = "a[title='Delete'][href*='{0}']".format(agency_group_id)
        self.click_element(edit_icon_loc)

    def click_first_edit_icon(self):
        self.click_element(self.edit_icon)

    def click_first_delete_icon(self):
        self.click_element(self.delete_icon)

    def type_in_filter(self, string):
        self.clear_and_send_value(string, self.search_box)
