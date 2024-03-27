from base.dx import Dx

class NewCreatives(Dx):
    
    def click_bulk_edit(self):
        self.click_element(self.bulk_edit_link)

    def click_detailed_edit(self):
        self.click_element(self.detailed_edit_link)

    def click_bulk_upload_new_creatives(self):
        self.click_element(self.bulk_upload_new_creatives)

    def click_bulk_upload_new_assets(self):
        self.click_element(self.bulk_upload_new_assets)
