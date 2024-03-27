from base.dx import Dx

class SegmentShowPage(Dx):

    def click_on_edit_link(self):
        self.click_element(self.edit_link)

    def click_on_view_all_link(self):
        self.click_element(self.view_all_link)

    def click_see_all_pixels_link(self):
        self.click_element(self.see_all_pixels_link)

    def get_innerhtml_text(self, locator, attribute = 'innerHTML'):
        innerhtml_text = str(self.find_element(getattr(self, locator)).get_attribute(attribute))
        return innerhtml_text
