from base.dx import Dx

class BulkUploadCreatives(Dx):
    
    def click_upload(self, file_path):
        self.upload_file(file_path, self.creatives_file)

    def input_start_date(self, value):
        self.fill_field(self.start_date, value)

    def input_end_date(self, value):
        self.fill_field(self.end_date, value)

    def input_concept(self, value):
        self.fill_field(self.concept, value)        

    def select_is_flash(self, value):
        self.select_option(self.is_flash, value)

    def click_submit(self):
        self.click_element(self.submit)

    def click_use_assets_link(self):
        self.click_element(self.use_assets)

    def click_setup_creatives_link(self):
        self.click_element(self.setup_creatives)

    def click_download_example_link(self):
        self.click_element(self.download_example)
