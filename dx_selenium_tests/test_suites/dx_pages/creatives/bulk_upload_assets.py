from base.dx import Dx

class UploadAssets(Dx):
    
    def click_upload(self, file_path):
        self.upload_file(file_path, self.assets_file)

    def click_more_assets(self):
        self.click_element(self.more_assets)

    def click_upload_assets(self):
        self.click_element(self.upload_assets)

    def click_generate_creatives(self):
        self.click_element(self.generate_creatives)
    
    def click_use_creatives_link(self):
        self.click_element(self.use_creatives)