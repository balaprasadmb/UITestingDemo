import uuid
from dx_test.dx_test import DXTest
from search.search import SearchPage
from creatives.creative_list_page import CreativeList
from creatives.new_creatives import NewCreatives
from creatives.bulk_upload_creatives import BulkUploadCreatives
from creatives.bulk_edit_creatives import BulkEditCreatives
from creatives.detailed_edit_creatives import DetailedEditCreatives
from creatives.edit_creatives import EditCreatives
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate
from lib.gui_tests import test_case
import os
import time

class CreativeTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(DXConstant().user_by_role['campaign_manager'])
        self.search_page = SearchPage(self.driver.get_browser())
        self.creative_list = CreativeList(self.driver.get_browser())
        self.new_creatives = NewCreatives(self.driver.get_browser())
        self.bulk_upload_creative = BulkUploadCreatives(self.driver.get_browser())
        self.bulk_edit_creative = BulkEditCreatives(self.driver.get_browser())
        self.detailed_edit_creatives = DetailedEditCreatives(self.driver.get_browser())
        self.edit_creatives = EditCreatives(self.driver.get_browser())

    def navigate_to_creative_list(self):
        self.search_page.click_creative_link()
        self.search_page.accept_alert()
        self.creative_list.wait_for_creatives_list()
        self.creative_list.select_advertiser(DXConstant().advertiser_name)
        time.sleep(20)

    @test_case()
    def working_of_advertiser_dropdown(self):
        self.navigate_to_creative_list()
        self.creative_list.page_should_contain(DXConstant().advertiser_name)

    def wait_for_spinner(self):
        self.creative_list.wait_till_visible(self.creative_list.creative_tag_spinner[0], self.creative_list.creative_tag_spinner[1])
        self.creative_list.wait_till_invisible(self.creative_list.creative_tag_spinner[0], self.creative_list.creative_tag_spinner[1])

    @test_case()
    def offer_type_should_not_present(self):
        self.creative_list.page_should_not_contain('Offer Type')

    @test_case()
    def offer_type_should_not_present(self):
        self.creative_list.page_should_not_contain('Offer Type')

    @test_case()
    def working_of_filter_creatives(self):
        try:
            self.creative_list.search_filters(self.creative_list.search)
            self.wait_for_spinner()
            assert self.creative_list.search in self.creative_list.get_first_creative()
            self.creative_list.search_filters('Dns#3Bpd')
            self.wait_for_spinner()
            self.creative_list.page_should_contain('There are no  creatives on AppNexus and RMX for this advertiser.')
            self.creative_list.search_filters('')
        except Exception as e:
            self.creative_list.search_filters('')
            raise e

    @test_case()
    def working_of_master_checkbox(self):
        self.navigate_to_creative_list()
        self.creative_list.click_select_all()
        assert self.creative_list.find_element(self.creative_list.first_creative_checkbox).is_selected()
        self.creative_list.click_select_all()
        assert not self.creative_list.find_element(self.creative_list.first_creative_checkbox).is_selected()

    @test_case()
    def working_of_creative_link(self):
        contents = [self.creative_list.get_first_creative(), 'AppNexus', 'RMX RTB', 'Edit', 'All Creatives']
        self.creative_list.click_first_creative()
        self.detailed_edit_creatives.wait_for_details_view()
        for content in contents:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def working_of_cancel_button(self):
        self.navigate_to_creative_list()
        self.creative_list.click_new_creatives()
        self.bulk_edit_creative.wait_for_creative_forms()
        self.creative_list.go_to_link('Detailed Edit')
        self.detailed_edit_creatives.wait_for_detailed_form()
        self.detailed_edit_creatives.click_cancel_first()
        self.detailed_edit_creatives.accept_alert()
        self.creative_list.wait_for_creatives_list()
        self.creative_list.page_should_contain('Creative tags')

    @test_case()
    def working_of_new_creatives_button(self):
        self.creative_list.click_new_creatives()
        self.bulk_edit_creative.wait_for_creative_forms()
        self.bulk_edit_creative.page_should_contain('Set Up Creatives')

    @test_case()
    def verify_contents_of_bulk_edit(self):
        self.bulk_edit_creative.wait_for_creative_forms()
        contents = ['add_creative', 'cancel_creative', 'save_creatives', 'first_creative_name', 'first_start_date',
                    'first_end_date', 'first_concept', 'first_tag', 'first_url', 'first_preview', 'first_remove']
        for element in contents:
            assert self.bulk_edit_creative.is_element_present(getattr(self.bulk_edit_creative, element))

    @test_case()
    def working_of_add_creatives_button(self):
        self.bulk_edit_creative.click_add_creative()
        time.sleep(5)
        contents = ['second_creative_name', 'second_start_date', 'second_end_date', 'second_concept',
                     'second_tag', 'second_url', 'second_preview', 'second_remove']
        for element in contents:
            assert self.bulk_edit_creative.is_element_present(getattr(self.bulk_edit_creative, element))

    @test_case()
    def working_of_cancel_bulk_edit(self):
        self.bulk_edit_creative.click_cancel()
        self.bulk_edit_creative.accept_alert()
        self.creative_list.wait_for_creatives_list()
        self.creative_list.page_should_contain('Creative tags')

    @test_case()
    def get_creative_tags(self, type = None):
        filepath = '/../../../data/bulk_upload_creative_files/creative_tags.txt'
        tag_file = open(os.path.dirname(__file__) + filepath)
        tags =  tag_file.read()
        tag_file.close()
        return tags

    @test_case()
    def fill_bulk_edit_creative_details(self):
        creative = DXConstant().creative_name + self.bulk_edit_creative.get_random_string()
        self.bulk_edit_creative.input_first_creative_name(creative)
        concept = DXConstant().creative_concept_name + self.bulk_edit_creative.get_random_string()
        self.bulk_edit_creative.input_first_concept(concept)
        self.bulk_edit_creative.input_first_tag(self.get_creative_tags())
        time.sleep(10)
        self.bulk_edit_creative.click_save_creatives()

    @test_case()
    def working_of_save_creatives(self):
        self.navigate_to_creative_list()
        self.creative_list.click_new_creatives()
        self.bulk_edit_creative.wait_for_creative_forms()
        self.fill_bulk_edit_creative_details()
        self.creative_list.wait_for_creatives_list()
        self.creative_list.page_should_contain(self.bulk_edit_creative.success_message)

    @test_case()
    def working_of_detailed_edit_link(self):
        self.navigate_to_creative_list()
        self.creative_list.click_new_creatives()
        self.bulk_edit_creative.wait_for_creative_forms()
        time.sleep(5)
        self.new_creatives.go_to_link('Detailed Edit')
        self.detailed_edit_creatives.wait_for_detailed_form()
        self.detailed_edit_creatives.page_should_contain('Creatives List')

    @test_case()
    def verify_contents_of_detailed_edit(self):
        self.detailed_edit_creatives.wait_for_detailed_form()
        elements = [
                    'add_detailed_creative', 'first_creative_link', 'first_creative_name', 'first_concept',
                    'first_size', 'first_ad_type', 'first_ad_feature', 'first_tag_type', 'first_url',
                    'first_offer_type', 'first_additional', 'first_start_date', 'first_end_date',
                    'first_lang_targeting', 'first_is_flash', 'first_new_vendor', 'first_placement', 'first_z_index',
                    'first_new_external_id', 'first_new_add_on', 'first_click_tracking','first_original_link',
                    'first_processed_link', 'first_secure_link', 'first_secure_processed_link',
                    'first_edit_tags', 'first_cancel', 'first_validate', 'first_preview', 'first_save'
                ]
        for element in elements:
            assert self.detailed_edit_creatives.is_element_present(getattr(self.detailed_edit_creatives, element))
        for index in range(1,10):
            self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.page_contents[index])

    @test_case()
    def verify_options_in_size(self):
        assert self.detailed_edit_creatives.get_dropdown_selected_value(self.detailed_edit_creatives.first_size) == '- Select One -'
        sizes = ['300x250', '336x280', '720x300', '234x60' ,'120x90', '728x90', '300x600',
                 '320x50','300x75', '216x36', '168x28', '120x30', 'Custom Size...']
        self.detailed_edit_creatives.check_dropdown_options(sizes, self.detailed_edit_creatives.first_size)

    @test_case()
    def verify_custom_size_fields(self):
        self.detailed_edit_creatives.select_first_size('Custom Size...')
        time.sleep(5)
        for element in ['first_size_width', 'first_size_height']:
            assert self.detailed_edit_creatives.is_element_present(getattr(self.detailed_edit_creatives, element))

    @test_case()
    def verify_ad_type(self):
        self.detailed_edit_creatives.check_dropdown_options(self.detailed_edit_creatives.ad_type, self.detailed_edit_creatives.first_ad_type)

    @test_case()
    def verify_ad_features_for_banner(self):
        self.detailed_edit_creatives.check_dropdown_options(self.detailed_edit_creatives.banner_features,
                                                            self.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_ad_features_for_linear_video(self):
        self.detailed_edit_creatives.select_first_ad_type(self.detailed_edit_creatives.ad_type[1])
        time.sleep(10)
        self.detailed_edit_creatives.check_dropdown_options(self.detailed_edit_creatives.video_features,
                                                            self.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_ad_features_for_rich_media(self):
        self.detailed_edit_creatives.select_first_ad_type(self.detailed_edit_creatives.ad_type[2])
        time.sleep(10)
        self.detailed_edit_creatives.check_dropdown_options(self.detailed_edit_creatives.rich_media_features,
                                                            self.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_additional_url_not_mandatory(self):
        assert self.detailed_edit_creatives.find_element(self.detailed_edit_creatives.first_additional).text == ''

    @test_case()
    def verify_lang_targeting(self):
        assert self.detailed_edit_creatives.get_dropdown_selected_value(self.detailed_edit_creatives.first_lang_targeting) == 'None'
        langs = ['English', 'French', 'German', 'Italian', 'Polish', 'Portuguese', 'Spanish']
        self.detailed_edit_creatives.check_dropdown_options(langs, self.detailed_edit_creatives.first_lang_targeting)

    @test_case()
    def verify_creative_attributes(self):
        assert self.detailed_edit_creatives.get_dropdown_selected_value(self.detailed_edit_creatives.first_is_flash) == 'Flashless'
        options = ['- Select One -', 'Flash', 'Flashless']
        self.detailed_edit_creatives.check_dropdown_options(options, self.detailed_edit_creatives.first_is_flash)

    @test_case()
    def verify_oba_icon_placement(self):
        assert self.detailed_edit_creatives.get_dropdown_selected_value(self.detailed_edit_creatives.first_placement) == '- Select One -'
        options = ['Top Right', 'Top Left', 'Bottom Right', 'Bottom Left']
        self.detailed_edit_creatives.check_dropdown_options(options, self.detailed_edit_creatives.first_placement)

    @test_case()
    def verify_ad_tag_section(self):
        elements = ['first_original_link', 'first_processed_link', 'first_secure_link', 'first_secure_processed_link']
        for element in elements:
            assert self.detailed_edit_creatives.is_element_present(getattr(self.detailed_edit_creatives, element))
        options = ['iFrame', 'Javascript', 'URL', 'Legacy', 'Image',
                   'VAST 2.0.1', 'Facebook', 'ORMMA', 'MRAID v1', 'MRAID v2']
        self.detailed_edit_creatives.check_dropdown_options(options, self.detailed_edit_creatives.first_tag_type)

    @test_case()
    def verify_external_id_section(self):
        self.detailed_edit_creatives.click_first_external_id()
        self.detailed_edit_creatives.wait_for_external_id_source()
        for element in ['first_external_id_source', 'first_external_id_value']:
            assert self.detailed_edit_creatives.is_element_present(getattr(self.detailed_edit_creatives, element))
        assert self.detailed_edit_creatives.get_dropdown_selected_value(self.detailed_edit_creatives.first_external_id_source) == 'RMX'
        options = ['RMX', 'DFA', 'Atlas', 'BlueKai', 'WURFL', 'MediaMind', 'Facebook',
                   'Facebook Campaign', 'Facebook Page Post Ad', 'SalesForce']
        self.detailed_edit_creatives.check_dropdown_options(options, self.detailed_edit_creatives.first_external_id_source)

    @test_case()
    def fill_creative_details_with_blank(self):
        self.working_of_detailed_edit_link()
        self.detailed_edit_creatives.wait_for_detailed_form()
        self.detailed_edit_creatives.input_first_url('')
        self.detailed_edit_creatives.select_first_is_flash('- Select One -')
        self.detailed_edit_creatives.click_save_first()
        self.detailed_edit_creatives.wait_for_errors()

    def blank_message_validation(self, key):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.blank_messages[key])

    @test_case()
    def blank_creative_name(self):
        self.blank_message_validation('name')

    @test_case()
    def blank_concept_name(self):
        self.blank_message_validation('concept')

    @test_case()
    def size_should_not_selected(self):
        for key in ['height', 'width']:
            self.blank_message_validation(key)

    @test_case()
    def creative_attributes_kept_blank(self):
        self.blank_message_validation('flash')

    @test_case()
    def blank_ad_tag(self):
        for key in ['tags', 'ad_tag']:
            self.blank_message_validation(key)

    @test_case()
    def blank_advertiser_url(self):
        self.blank_message_validation('url')

    def fill_creative_details_with_special_chars(self):
        self.working_of_detailed_edit_link()
        time.sleep(5)
        self.detailed_edit_creatives.input_first_url(DXConstant().special_char)
        time.sleep(5)
        self.detailed_edit_creatives.input_first_add_url(DXConstant().special_char)
        self.detailed_edit_creatives.select_first_placement('Top Right')
        time.sleep(5)
        self.detailed_edit_creatives.input_first_z_index(DXConstant().special_char)
        self.detailed_edit_creatives.click_validate_first()
        self.detailed_edit_creatives.wait_for_errors()

    def special_chars_validation(self, key):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.special_chars[key])

    @test_case()
    def special_chars_urls(self):
        self.special_chars_validation('url')

    @test_case()
    def special_chars_z_index(self):
        self.special_chars_validation('z_index')

    def fill_creative_details_with_256_chars(self):
        self.detailed_edit_creatives.input_first_creative_name(self.detailed_edit_creatives.get_random_string(256))
        self.detailed_edit_creatives.input_first_concept(self.detailed_edit_creatives.get_random_string(201))
        self.detailed_edit_creatives.click_validate_first()
        time.sleep(10)

    def over_limit_validation(self, key):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.over_limit[key])

    @test_case()
    def over_limit_name(self):
        self.over_limit_validation('name')

    @test_case()
    def over_limit_concept(self):
        self.over_limit_validation('concept')

    def empty_creative_details(self):
        details = ['name', 'concept', 'first_url', 'size', 'lang', 'first_source',
                   'first_external_id', 'second_source', 'second_source']
        for field in details:
            self.creative_details[field] = ''

    @test_case()
    def fill_creative_details(self):
        self.detailed_edit_creatives.select_first_lang_targeting(self.creative_details['lang'])
        self.detailed_edit_creatives.input_first_creative_name(self.creative_details['name'])
        self.detailed_edit_creatives.input_first_concept(self.creative_details['concept'])
        if self.creative_details.has_key('advertiser_url'):
            self.detailed_edit_creatives.input_first_url(self.creative_details['advertiser_url'])
        self.detailed_edit_creatives.input_first_add_url(self.creative_details['first_url'])
        if self.creative_details.has_key('second_url'):
            self.detailed_edit_creatives.update_first_add_url(self.creative_details['second_url'])
        self.detailed_edit_creatives.select_first_size(self.creative_details['size'])
        if self.creative_details['size'] == 'Custom Size...':
            self.detailed_edit_creatives.input_first_width(self.creative_details['width'])
            self.detailed_edit_creatives.input_first_height(self.creative_details['height'])
        if self.creative_details.has_key('z_index'):
            self.detailed_edit_creatives.input_first_z_index(self.creative_details['z_index'])
        self.detailed_edit_creatives.click_first_external_id()
        time.sleep(5)
        self.detailed_edit_creatives.select_first_external_id_source(self.creative_details['first_source'])
        self.detailed_edit_creatives.input_first_external_id_value(self.creative_details['first_external_id'])
        if self.creative_details.has_key('second_source'):
            self.detailed_edit_creatives.click_first_external_id()
            time.sleep(5)
            self.detailed_edit_creatives.select_second_source(self.creative_details['second_source'])
            self.detailed_edit_creatives.input_second_value(self.creative_details['second_external_id'])
        self.detailed_edit_creatives.input_first_tags(self.get_creative_tags())

    @test_case()
    def fill_creative_details_with_valid_special_chars(self):
        self.working_of_detailed_edit_link()
        payload = DXConstant().special_char + self.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().creative_name + payload
        self.creative_details['concept'] = DXConstant().creative_concept_name + payload
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['size'] = '300x250'
        self.creative_details['lang'] = 'English'
        self.creative_details['first_source'] = 'RMX'
        self.creative_details['first_external_id'] = '3'
        self.creative_details['second_source'] = 'RMX'
        self.creative_details['second_external_id'] = '9'
        self.fill_creative_details()
        self.detailed_edit_creatives.click_validate_first()

    @test_case()
    def working_of_validate_creative(self):
        time.sleep(10)
        self.detailed_edit_creatives.page_should_contain(self.creative_details['name'])
        assert not self.detailed_edit_creatives.is_element_present(self.detailed_edit_creatives.errors)

    @test_case()
    def working_of_save_creative(self):
        self.detailed_edit_creatives.save_creative()
        self.creative_list.wait_for_creatives_list()
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.success_message)

    @test_case()
    def go_to_show_creative(self):
        self.creative_list.go_to_link(self.creative_details['name'])
        self.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_creative_name(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['name'])

    @test_case()
    def assert_creative_concept(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['concept'])

    @test_case()
    def assert_creative_size(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['size'])

    @test_case()
    def assert_additional_url(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['first_url'])

    @test_case()
    def assert_creative_attributes(self):
        self.detailed_edit_creatives.page_should_contain('Flashless')

    @test_case()
    def assert_oba_placement(self):
        self.detailed_edit_creatives.page_should_contain('top-right')

    @test_case()
    def assert_lang_targeting(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['lang'])

    @test_case()
    def assert_external_id_same_source(self):
        for content in ['RMX', '3', '9']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def creative_name_should_not_accept_script(self):
        self.working_of_detailed_edit_link()
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().html_tag
        self.creative_details['concept'] = DXConstant().html_tag
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['size'] = '300x250'
        self.creative_details['lang'] = 'English'
        self.creative_details['z_index'] = DXConstant().strings
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '9'
        self.creative_details['second_source'] = 'BlueKai'
        self.creative_details['second_external_id'] = '9'
        self.fill_creative_details()
        self.detailed_edit_creatives.input_first_tags(self.detailed_edit_creatives.get_random_string())
        self.detailed_edit_creatives.click_save_first()
        self.detailed_edit_creatives.wait_for_errors()
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.blank_messages['name'])

    @test_case()
    def assert_concept_not_accepts_script(self):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.validation['concept'])

    @test_case()
    def assert_z_index_should_not_accept_chars(self):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.special_chars['z_index'])

    @test_case()
    def assert_invalid_ad_tag(self):
        self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.validation['ad_tag'])

    @test_case()
    def assert_external_id_same_source_value(self):
        for content in ['BlueKai', '9', '9']:
            self.creative_list.page_should_contain(content)

    def validation_of_custom_size(self, width, height, messages):
        self.detailed_edit_creatives.input_first_width(getattr(DXConstant(), width))
        self.detailed_edit_creatives.input_first_height(getattr(DXConstant(), height))
        self.detailed_edit_creatives.click_save_first()
        time.sleep(10)
        for message in messages:
            self.detailed_edit_creatives.page_should_contain(self.detailed_edit_creatives.validation[message])

    @test_case()
    def validation_of_custom_size_number_name(self):
        self.working_of_detailed_edit_link()
        self.detailed_edit_creatives.select_first_size('Custom Size...')
        for value in [['strings', 'value', ['width']], ['value','strings', ['height']],
                      ['strings', 'strings', ['width','height']]]:
            self.validation_of_custom_size(value[0], value[1], value[2])
        self.creative_details = {}
        self.creative_details['name'] = self.detailed_edit_creatives.get_random_digits()
        self.creative_details['concept'] = DXConstant().creative_concept_name + self.detailed_edit_creatives.get_random_digits(5)
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['second_url'] = 'www.xyz.com'
        self.creative_details['size'] = 'Custom Size...'
        self.creative_details['width'] = DXConstant().value
        self.creative_details['height'] = DXConstant().value
        self.creative_details['lang'] = 'French'
        self.creative_details['z_index'] = '39'
        self.creative_details['first_source'] = 'Atlas'
        self.creative_details['first_external_id'] = '19'
        self.creative_details['second_source'] = 'DFA'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_custom_size(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['width'] + 'x' + self.creative_details['height'])

    @test_case()
    def assert_proper_url_accepted(self):
        self.detailed_edit_creatives.page_should_contain('http://www.someurl.com')

    @test_case()
    def assert_oba_placement_with_entered_index(self):
        for content in ['top-right', '39']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_external_id_different_source(self):
        for content in ['Atlas', 'DFA', '19']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_additional_url_accepts_more_than_one(self):
        for content in [self.creative_details['first_url'], self.creative_details['second_url']]:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def validation_for_limit(self):
        self.working_of_detailed_edit_link()
        self.creative_details = {}
        self.creative_details['name'] = str(self.detailed_edit_creatives.get_random_string(255)).lower()
        self.creative_details['concept'] = str(self.detailed_edit_creatives.get_random_string(200)).lower()
        self.creative_details['size'] = '300x250'
        self.creative_details['advertiser_url'] = str('www.' + self.detailed_edit_creatives.get_random_characters(247) + '.com').lower()
        self.creative_details['first_url'] = str('www.' + self.detailed_edit_creatives.get_random_characters(247) + '.com').lower()
        self.creative_details['lang'] = 'German'
        self.creative_details['first_source'] = 'MediaMind'
        self.creative_details['first_external_id'] = '11'
        self.creative_details['second_source'] = 'MediaMind'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_url_with_255_chars(self):
        self.detailed_edit_creatives.page_should_contain('http://' + self.creative_details['advertiser_url'])

    @test_case()
    def assert_additional_url_with_255_chars(self):
        self.detailed_edit_creatives.page_should_contain('http://' + self.creative_details['first_url'])

    @test_case()
    def assert_external_ids(self):
        for content in ['MediaMind', '11', '19']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def creatives_with_valid_details(self):
        self.working_of_detailed_edit_link()
        payload = self.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().creative_name + payload
        self.creative_details['concept'] = DXConstant().creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Italian'
        self.creative_details['first_source'] = 'WURFL'
        self.creative_details['first_external_id'] = '19'
        self.creative_details['second_source'] = 'SalesForce'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_different_external_ids(self):
        for content in ['WURFL', 'SalesForce', '19']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_salesforce_external_id(self):
        self.detailed_edit_creatives.page_should_contain('SalesForce')

    @test_case()
    def creatives_with_validation_of_external_ids(self):
        self.working_of_detailed_edit_link()
        payload = self.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().creative_name + payload
        self.creative_details['concept'] = DXConstant().creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Polish'
        self.creative_details['first_source'] = 'RMX'
        self.creative_details['first_external_id'] = '1903'
        self.creative_details['second_source'] = 'Facebook'
        self.creative_details['second_external_id'] = 'mshskn'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_external_ids_with_numbers(self):
        for content in ['RMX', '1903']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_external_ids_with_chars(self):
        for content in ['Facebook', 'mshskn']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def creatives_with_multiple_external_ids(self):
        self.working_of_detailed_edit_link()
        payload = self.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().creative_name + payload
        self.creative_details['concept'] = DXConstant().creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Portuguese'
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '19msh03'
        self.creative_details['second_source'] = 'MediaMind'
        self.creative_details['second_external_id'] = 'skn3919'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_multiple_external_ids(self):
        for content in ['BlueKai', '19msh03', 'MediaMind', 'skn3919']:
            self.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_click_tracking(self, click_tracking = True):
        status = self.detailed_edit_creatives.get_attribute_value(self.detailed_edit_creatives.click_tracking_status, 'innerHTML')
        if click_tracking:
            assert 'Enabled' in status
        else:
            assert 'Disabled' in status

    @test_case()
    def valid_tags_entered(self):
        self.detailed_edit_creatives.page_should_contain(self.creative_details['name'])

    def go_to_creative_edit(self):
        self.navigate_to_creative_list()
        self.creative_list.go_to_link(self.creative_details['name'])
        self.detailed_edit_creatives.wait_for_details_view()
        self.detailed_edit_creatives.go_to_link('Edit')
        self.edit_creatives.wait_for_update_form()

    @test_case()
    def validation_while_updating_creatives(self):
        self.go_to_creative_edit()
        self.edit_creatives.input_creative_name('')
        self.edit_creatives.input_creative_concept('')
        self.edit_creatives.click_save_creatives()
        self.edit_creatives.wait_for_errors()

    @test_case()
    def update_details_with_limit_values(self):
        self.edit_creatives.select_size('120x90')
        self.creative_name = str(self.detailed_edit_creatives.get_random_string(255)).lower()
        self.concept = str(self.detailed_edit_creatives.get_random_string(200)).lower()
        self.edit_creatives.input_creative_name(self.creative_name)
        self.edit_creatives.input_creative_concept(self.concept)
        self.edit_creatives.select_second_source('DFA')
        self.edit_creatives.input_external_id('190391')
        self.edit_creatives.click_save_creatives()
        self.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_updated_name(self):
        self.edit_creatives.page_should_contain(self.creative_name)

    @test_case()
    def assert_updated_concept(self):
        self.edit_creatives.page_should_contain(self.concept)

    @test_case()
    def assert_updated_size(self):
        self.edit_creatives.page_should_contain('120x90')

    @test_case()
    def assert_updated_external_ids(self):
        for content in ['DFA', '190391']:
            self.edit_creatives.page_should_contain(content)

    @test_case()
    def creatives_with_spanish_lang_targeting(self):
        self.working_of_detailed_edit_link()
        payload = self.detailed_edit_creatives.get_random_string()
        self.detailed_edit_creatives.click_first_click_tracking()
        self.detailed_edit_creatives.click_first_original_link()
        time.sleep(5)
        self.creative_details = {}
        self.creative_details['name'] = DXConstant().creative_name + payload
        self.creative_details['concept'] = DXConstant().creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Spanish'
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '3bpd9dns'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_click_tracking_disabled(self):
        self.assert_click_tracking(False)

    @test_case()
    def update_creatives_with_special_chars(self):
        self.go_to_creative_edit()
        payload = self.detailed_edit_creatives.get_random_string(5) + DXConstant().special_char
        self.creative_name = DXConstant().creative_name + payload
        self.concept = DXConstant().creative_concept_name + payload
        self.edit_creatives.click_add_external_ids()
        time.sleep(5)
        self.edit_creatives.select_second_source('WURFL')
        self.edit_creatives.input_second_external_id('b1p9d3')
        self.edit_creatives.input_creative_name(self.creative_name)
        self.edit_creatives.input_creative_concept(self.concept)
        self.edit_creatives.click_save_creatives()
        self.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_updated_multiple_external_ids(self):
        for content in ['BlueKai', '3bpd9dns', 'WURFL', 'b1p9d3']:
            self.edit_creatives.page_should_contain(content)
