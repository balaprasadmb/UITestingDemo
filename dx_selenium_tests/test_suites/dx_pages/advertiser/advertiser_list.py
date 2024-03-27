from base.dx import Dx

class AdvertiserListPage(Dx):
    def click_on_new_advrtiser_button(self):
        self.click_element(self.new_advertiser)
        
    def type_advertiser_name_in_filterbox(self, advertiser_name):
        self.clear_and_send_value(advertiser_name, self.search_box)    
        
    def click_edit_icon(self, advertiser_name):
        advertiser_name_id = self.get_id_from_link(advertiser_name)
        edit_icon_loc = "a[title='Edit'][href*='{0}']".format(advertiser_name_id)
        self.click_element(edit_icon_loc)

    def click_delete_icon(self, advertiser_name):
        advertiser_name_id = self.get_id_from_link(advertiser_name)
        edit_icon_loc = "a[title='Delete'][href*='{0}']".format(advertiser_name_id)
        self.click_element(edit_icon_loc)

    def click_first_edit_icon(self):
        self.click_element(self.edit_icon)

    def click_first_delete_icon(self):
        self.click_element(self.delete_icon)

    def click_first_advertiser(self):
        self.click_element(self.advertiser_name_link)
