import uuid
import time
from selenium.webdriver.common.keys import Keys
from dx_test.dx_test import DXTest
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
from campaigns.campaign_list import CampaignList
from campaigns.create_media_plan import CreateMediaPlan
from campaigns.edit_media_plan import EditMediaPlan

class MediaPlanTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(DXConstant().user_by_role['campaign_manager'])
        self.list_page = CampaignList(self.driver.get_browser())
        self.media_page = CreateMediaPlan(self.driver.get_browser())
        self.edit_media = EditMediaPlan(self.driver.get_browser())

    @test_case()
    def open_campaigns_page(self):
        for element in ['campaign_link', 'search_box']:
            self.list_page.click_element(getattr(self.list_page,element))
        self.list_page.select_orgnization(DXConstant().advertiser_name)
        time.sleep(15)
        self.list_page.click_new_media()
        self.media_page.wait_till_visible('id','new_media_plan')

    @test_case()
    def media_plan_page_contents(self):
        self.media_page.click_add_row()
        time.sleep(5)
        for element in ['Last View', 'Last Click']:
            self.media_page.select_attribution_model(element)
        for value in ['Percent Of Price', 'Fixed']:
            self.media_page.select_value_type(value)
        options = ['Days', 'Hours', 'Minutes']
        for option in options:
            self.media_page.select_last_click(option)
        for option in options:
            self.media_page.select_last_view(option)
        self.media_page.page_should_contain('Reporting and Learning Lookback Windows')
        contents = ['name', 'start_date', 'end_date', 'budget', 'currency', 'attribution_model', 'add_row',
                     'activity_pixel', 'activity_filter', 'value_type', 'value', 'delete_activity', 'campaign_filter',
                     'master_select', 'last_click_input', 'last_click_select', 'last_view_input',
                      'last_view_select', 'cancel', 'submit']
        for element in contents:
            assert self.media_page.is_element_present(getattr(self.media_page, element))
 
    @test_case()   
    def fill_media_plan_details(self):
        self.name = DXConstant().media_plan + str(uuid.uuid4())
        self.media_page.type_name(self.name)
        self.media_page.type_start_date(DXDate().todays_date())
        self.media_page.type_end_date(DXDate().date_after_two_days())
        self.media_page.type_budget('5000')
        self.media_page.type_value('9')
        self.media_page.click_submit()
        self.media_page.page_should_contain(self.name)
        self.media_page.go_to_link(self.media_page.show_page)
        self.media_page.page_should_contain(self.name)

    @test_case()
    def go_to_edit_media_plan(self):
        self.list_page.filter_campaigns(self.name)
        self.list_page.go_to_link(self.name)
        self.list_page.wait_till_visible('id','details')
        self.list_page.edit_media_plan()
    
    def check_messages(self, key):
        self.edit_media.page_should_contain(self.edit_media.messages[key])

    @test_case()
    def validate_plan_budget(self):
        for message in ['strings', 'special_char', 'alphanumeric_value']:
            self.edit_media.type_budget(getattr(DXConstant(), message))
            self.edit_media.click_submit()
            self.edit_media.wait_till_visible('id','flash_message')
            time.sleep(10)
            self.check_messages('budget')
        self.edit_media.type_budget(DXConstant().budget)
        self.edit_media.click_submit()
        self.edit_media.wait_till_visible('id','details')
        self.check_messages('update')

    @test_case()
    def validate_activity_value(self):
        self.edit_media.go_to_link(self.media_page.show_page)
        self.go_to_edit_media_plan()
        for message in ['strings', 'special_char', 'alphanumeric_value']:
            self.edit_media.type_value(DXConstant().strings)
            self.edit_media.click_submit()
            self.edit_media.wait_till_visible('id','flash_message')
            time.sleep(10)
            self.check_messages('activity_value')
        self.edit_media.type_value(DXConstant().value)
        self.edit_media.click_submit()
        self.edit_media.wait_till_visible('id','details')
        self.check_messages('update')

    @test_case()
    def media_plan_with_currency_euro(self):
        self.list_page.click_element(self.list_page.campaign_link)
        self.list_page.click_new_media()
        self.media_page.wait_till_visible('id', 'new_media_plan')
        self.media_page.click_add_row()
        self.name = DXConstant().media_plan + str(uuid.uuid4())
        self.media_page.type_name(self.name)
        self.media_page.type_start_date(DXDate().todays_date())
        self.media_page.type_end_date(DXDate().date_after_two_days())
        self.media_page.type_budget('5000')
        self.media_page.select_currency('Euro (EUR)')
        self.media_page.type_value('9')
        self.media_page.click_campaign_filter()
        self.media_page.type_campaign_filter(Keys.ENTER)
        self.media_page.page_should_contain('New Media Plan')
        self.media_page.click_submit()

    @test_case()
    def verify_media_plan_created(self):
        self.media_page.wait_till_visible('id','flash_message')
        self.media_page.page_should_contain(self.media_page.messages['success'])
        self.media_page.page_should_contain('Euro (EUR)')
