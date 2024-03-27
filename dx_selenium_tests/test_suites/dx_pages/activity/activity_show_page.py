from base.dx import Dx

class ActivityShowPage(Dx):
    def click_activities_link(self):
        self.click_element(self.activities_link)

    def click_edit_link(self):
        self.click_element(self.edit_link)

    def get_activity_name(self):
        element = self.find_element(self.activity_name_title)
        activity_name = str(element.get_attribute('innerHTML'))
        return activity_name.strip('.')
    
    def get_pixel_tag_value(self):
        element = self.find_element(self.pixel_tag)
        pixel_tag_value = str(element.get_attribute('innerHTML'))
        return pixel_tag_value
