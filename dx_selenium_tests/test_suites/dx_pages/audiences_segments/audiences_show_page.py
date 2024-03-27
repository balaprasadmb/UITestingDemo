from base.dx import Dx
import time

class AudiencesShowPage(Dx):
    
    def click_edit_link(self):
        self.click_element(self.edit_link)

    def click_view_all_link(self):
        self.click_element(self.view_all_link)

    def get_inner_html_value(self, locator, attribute='innerHTML'):
        return self.get_attribute_value(getattr(self, locator),attribute)

    def select_currency(self, currency_name, method='label'):
        self.select_option(self.currency_dropdown, currency_name, method)
        time.sleep(1)
