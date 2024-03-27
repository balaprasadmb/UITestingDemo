from base.dx import Dx

class BulkEditCreatives(Dx):
    
    def click_add_creative(self):
        self.click_element(self.add_creative)

    def click_cancel(self):
        self.click_element(self.cancel_creative)

    def click_save_creatives(self):
        self.click_element(self.save_creatives)

    def click_bulk_upload_new_creative(self):
        self.click_element(self.bulk_upload_new_creative)

    def input_first_creative_name(self, value):
        self.fill_field(self.first_creative_name, value)

    def input_first_start_date(self, value):
        self.fill_field(self.first_start_date, value)

    def input_first_end_date(self, value):
        self.fill_field(self.first_end_date, value)

    def input_first_concept(self, value):
        self.click_element(self.first_concept)
        self.fill_field(self.first_concept, value)

    def input_first_tag(self, value):
        self.click_element(self.first_tag)
        self.fill_field(self.first_tag, value)

    def input_first_url(self, value):
        self.fill_field(self.first_url, value)

    def click_preview_first(self):
        self.click_element(self.first_preview)

    def click_remove_first(self):
        self.click_element(self.first_remove)

    def input_second_creative_name(self, value):
        self.fill_field(self.second_creative_name, value)

    def input_second_start_date(self, value):
        self.fill_field(self.second_start_date, value)

    def input_second_end_date(self, value):
        self.fill_field(self.second_end_date, value)

    def input_second_concept(self, value):
        self.fill_field(self.second_concept, value)

    def input_second_tag(self, value):
        self.fill_field(self.second_tag, value)

    def input_second_url(self, value):
        self.fill_field(self.second_url, value)

    def click_preview_second(self):
        self.click_element(self.second_preview)

    def click_remove_second(self):
        self.click_element(self.second_remove)

    def input_third_creative_name(self, value):
        self.fill_field(self.third_creative_name, value)

    def input_third_start_date(self, value):
        self.fill_field(self.third_start_date, value)

    def input_third_end_date(self, value):
        self.fill_field(self.third_end_date, value)

    def input_third_concept(self, value):
        self.fill_field(self.third_concept, value)

    def input_third_tag(self, value):
        self.fill_field(self.third_tag, value)

    def input_third_url(self, value):
        self.fill_field(self.third_url, value)

    def click_preview_third(self):
        self.click_element(self.third_preview)

    def click_remove_third(self):
        self.click_element(self.third_remove)

    def wait_for_creative_forms(self):
        self.wait_till_visible(self.creative_forms[0], self.creative_forms[1])
