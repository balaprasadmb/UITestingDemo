from base.dx import Dx

class CreateAudience(Dx):
    
    def select_first_segment_from_segment_table(self):
        self.click_element(self.first_segment_checkbox)

    def select_first_audience_marketplace_from_audience_marketplace_table(self):
        self.click_element(self.first_audience_marketplace_checkbox)

    def click_use_advance_mode_checkbox(self):
        self.click_element(self.use_advance_mode_checkbox)

    def click_composed_audience_master_checkbox(self):
        self.click_element(self.composed_audience_master_checkbox)

    def click_and_button(self):
        self.click_element(self.and_button)

    def click_or_button(self):
        self.click_element(self.or_button)

    def click_remove_button(self):
        self.click_element(self.remove_button)

    def enter_audience_name(self, audience_name):
        self.clear_and_send_value(audience_name, self.audience_name_textbox)

    def click_create_audience_button(self):
        self.click_element(self.create_audience_button)

    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def get_inner_html_value(self, locator, attribute='innerHTML'):
        element = self.find_element(getattr(self, locator))
        value = str(element.get_attribute(attribute))
        return value

    def enter_composed_audience_rate_card_value(self, composed_audience_rate_card_value):
        self.clear_and_send_value(composed_audience_rate_card_value, self.first_composed_audience_rate_card_value)
