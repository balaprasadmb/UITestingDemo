from dx_test_helper.dx_test_helper import DXTestHelper
from lib.dx_date import DXDate
from advertiser_list import AdvertiserListPage
from advertiser_details import AdvertiserDetailsPage
from edit_advertiser import EditAdvertiser
from configs.dx_constant import DXConstant
from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
from new_advertiser import NewAdvertiser
from agencies.agencies_list_page import AgenciesListPage
from agencies.agency_details import AgencyDetailsPage
from agencies.agency_edit import AgencyEdit
from agencies.new_agency import NewAgency
from new_advertiser import NewAdvertiser

class CommonHelper():

    def validate_result(self, result, criteria):
        expected_result = False if criteria == False else True
        assert result == expected_result, result

    def assert_is_element_present(self, page_object, loc, criteria=True):
        if type(loc) == list:
            actual_result = page_object.is_element_present(loc)
        else:
            actual_result = page_object.is_element_present(getattr(page_object, loc))
        self.validate_result(actual_result, criteria)

    def assert_is_selected(self, page_object, loc, criteria=True):
        if type(loc) == list:
            actual_result = page_object.find_element(loc).is_selected()
        else:
            actual_result = page_object.find_element(getattr(page_object, loc)).is_selected()
        self.validate_result(actual_result, criteria)

    def validate_add_on_cost(self, page_object, loc, add_on_cost_name, method='text'):
        flag = False
        if type(loc) == list:
            element_list = page_object.find_elements(loc)
        else:
            element_list = page_object.find_elements(getattr(page_object, loc))
        for element in element_list:
            if method == 'value':
                if add_on_cost_name == page_object.get_content_value(element):
                    flag = True
                    break
            else:
                if add_on_cost_name == page_object.get_content_text(element):
                    flag = True
                    break
        assert flag is True
