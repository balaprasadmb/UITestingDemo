from base.dx import Dx

class CustomInventoryShowPage(Dx):
    def click_on_custom_inventory_link(self):
        self.click_element(self.custom_inventory_link)
    
    def click_on_edit_custom_inventory_button(self):
        self.clik_element(self.edit_custom_inventory_button)
