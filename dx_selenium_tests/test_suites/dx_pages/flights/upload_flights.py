from base.dx import Dx
from selenium.webdriver.support.ui import Select

class UploadFlights(Dx):
    
    def select_file(self, value):
        self.fill_field(self.browse_file, value)
    
    def click_upload_file(self):
        self.click_element(self.upload_file)
    
    def click_flights_submit(self):
        self.click_element(self.flight_submit)
    
    def click_cancel_delete(self):
        self.click_element(self.cancel)
    
    def type_frequency_cap(self, value):
        self.fill_field(self.frequency_cap, value)
    
    def type_frequency(self, value):
        self.fill_field(self.frequency, value)
    
    def select_frequency_type(self, value):
        self.select_option(self.frequency_type, value)
    
    def select_flight_type(self, value):
        self.select_option(self.flight_type, value)
    
    def select_algorithm_for_fbx(self, value):
        self.select_option(self.fbx_algorithm, value)
    
    def select_placement_for_fbx(self, value):
        self.select_option(self.placement_fbx, value)
    
    def select_algorithm_for_standard_exchange(self, value):
        self.select_option(self.algorithm, value)
    
    def select_placement_for_standard_exchange(self, value):
        self.select_option(self.placement_standard, value)

    def select_viewability_vendors(self, value):
        self.select_option(self.viewability, value)
    
    def select_viewability_selections(self, value):
        self.select_option(self.selections, value)
    
    def select_placement_for_tracking(self, value):
        self.select_option(self.placement_tracking, value)
    
    def click_dayparting_sunday(self):
        self.click_element(self.dayparting_sunday)
    
    def click_dayparting_monday(self):
        self.click_element(self.dayparting_monday)

    def click_dayparting_tuesday(self):
        self.click_element(self.dayparting_tuesday)

    def click_dayparting_wednesday(self):
        self.click_element(self.dayparting_wednesday)

    def click_dayparting_thursday(self):
        self.click_element(self.dayparting_thursday)

    def click_dayparting_friday(self):
        self.click_element(self.dayparting_friday)

    def click_dayparting_saturday(self):
        self.click_element(self.dayparting_saturday)

    def click_select_all(self):
        self.click_element(self.select_all)
    
    def click_first_suppliers(self):
        self.click_element(self.select_first)

    def click_select_all_tracking(self):
        self.click_element(self.select_all_tracking)

    def select_avail_channel(self, value):
        self.select_option(self.avail_channels, value)
    
    def select_applied_channel(self, value):
        self.select_option(self.selected_channels, value)
    
    def click_select_channels(self):
        self.click_element(self.select_channels)
    
    def click_remove_channels(self):
        self.click_element(self.remove_channels)
    
    def click_select_all_channels(self):
        self.click_element(self.select_all_channels)
    
    def click_remove_all_channels(self):
        self.click_element(self.remove_all_channels)
    
    def click_inherit_lang_targeting(self):
        self.click_element(self.inherit_lang_targeting)
    
    def click_separate_lang_targeting(self):
        self.click_element(self.separate_lang_targeting)
        
    def select_base_lang_targeting(self, value):
        self.select_option(self.base_lang_targeting, value, 'index')

    def select_avail_langs(self, value):
        self.select_option(self.avail_langs, value)

    def select_applied_langs(self, value):
        self.select_option(self.selected_langs, value)

    def click_select_langs(self):
        self.click_element(self.select_langs)
    
    def click_remove_langs(self):
        self.click_element(self.remove_langs)
    
    def click_select_all_langs(self):
        self.click_element(self.select_all_langs)
    
    def click_remove_all_langs(self):
        self.click_element(self.remove_all_langs)
    
    def click_inherit_geo_targeting(self):
        self.click_element(self.inherit_geo_targeting)
    
    def click_separate_geo_targeting(self):
        self.click_element(self.separate_geo_targeting)

    def select_geo_targeting_type(self, index):
        self.select_option(self.selected_langs, index, 'index')
    
    def search_country(self, value):
        self.fill_field(self.search_countries, value)

    def select_avail_country(self, value):
        self.select_option(self.avail_countries, value)

    def select_applied_country(self, value):
        self.select_option(self.selected_countries, value)

    def click_select_country(self):
        self.click_element(self.select_countries)
    
    def click_remove_country(self):
        self.click_element(self.remove_countries)
    
    def click_select_all_countries(self):
        self.click_element(self.select_all_countries)
    
    def click_remove_all_countries(self):
        self.click_element(self.remove_all_countries)
    
    def search_geofenced_country(self, value):
        self.fill_field(self.geofenced_search_countries, value)

    def select_avail_geofenced_country(self, value):
        self.select_option(self.geofenced_avail_countries, value)

    def select_applied_geofenced_country(self, value):
        self.select_option(self.geofenced_selected_countries, value)

    def click_select_geofenced_country(self):
        self.click_element(self.geofenced_select_countries)
    
    def click_remove_geofenced_country(self):
        self.click_element(self.geofenced_remove_countries)
    
    def click_select_all_geofenced_countries(self):
        self.click_element(self.geofenced_select_all_countries)
    
    def click_remove_all_geofenced_countries(self):
        self.click_element(self.geofenced_remove_all_countries)

    def select_geofenced_file(self, value):
        self.fill_field(self.geofenced_browse_file, value)
    
    def type_geofenced_group_name(self, value):
        self.fill_field(self.geofenced_group_name, value)
    
    def click_geofenced_group_submit(self):
        self.click_element(self.geofenced_group_submit)
    
    def select_geo_target_country(self, value):
        self.select_option(self.country, value)

    def select_geo_target_area_type(self, value):
        self.select_option(self.area_type, value)
    
    def search_dual_country(self, value):
        self.fill_field(self.dual_search_countries, value)

    def select_avail_dual_country(self, value):
        self.select_option(self.dual_avail_countries, value)

    def select_applied_dual_country(self, value):
        self.select_option(self.dual_selected_countries, value)

    def click_select_dual_country(self):
        self.click_element(self.dual_select_countries)
    
    def click_remove_dual_country(self):
        self.click_element(self.dual_remove_countries)
    
    def click_select_all_dual_countries(self):
        self.click_element(self.dual_select_all_countries)
    
    def click_remove_all_dual_countries(self):
        self.click_element(self.dual_remove_all_countries)

    def search_metrocodes_country(self, value):
        self.fill_field(self.mc_search_countries, value)

    def select_avail_metrocodes_country(self, value):
        self.select_option(self.mc_avail_countries, value)

    def select_applied_metrocodes_country(self, value):
        self.select_option(self.mc_selected_countries, value)

    def click_select_metrocodes_country(self):
        self.click_element(self.mc_select_countries)
    
    def click_remove_metrocodes_country(self):
        self.click_element(self.mc_remove_countries)
    
    def click_select_all_metrocodes_countries(self):
        self.click_element(self.mc_select_all_countries)
    
    def click_remove_all_metrocodes_countries(self):
        self.click_element(self.mc_remove_all_countries)

    def search_postal_country(self, value):
        self.fill_field(self.pc_search_countries, value)

    def select_avail_postal_country(self, value):
        self.select_option(self.pc_avail_countries, value)

    def select_applied_postal_country(self, value):
        self.select_option(self.pc_selected_countries, value)

    def click_select_postal_country(self):
        self.click_element(self.pc_select_countries)
    
    def click_remove_postal_country(self):
        self.click_element(self.pc_remove_countries)
    
    def click_select_all_postal_countries(self):
        self.click_element(self.pc_select_all_countries)
    
    def click_remove_all_postal_countries(self):
        self.click_element(self.pc_remove_all_countries)

    def search_creatives(self, value):
        self.fill_field(self.creative_search, value)
    
    def clear_search(self):
        self.clear(self.creative_search)
    
    def select_all_creatives(self):
        self.click_element(self.master_select)
    
    def select_first_creative(self):
        self.click_element(self.first_select)
    
    def select_avail_audience(self, value, method = 'index'):
        self.select_option(self.avail_audience, value, method)
    
    def select_included_audience(self, value, method = 'index'):
        self.select_option(self.included_audience, value, method)

    def select_excluded_audience(self, value, method = 'index'):
        self.select_option(self.excluded_audience, value, method)

    def include_audience(self):
        self.click_element(self.move_included_audience)
    
    def exclude_audience(self):
        self.click_element(self.move_excluded_audience)
    
    def include_all_audience(self):
        self.click_element(self.move_all_included_audience)
    
    def exclude_all_audience(self):
        self.click_element(self.move_all_excluded_audience)
    
    def click_remove_audience(self):
        self.click_element(self.remove_audience)
    
    def click_remove_all_audience(self):
        self.click_element(self.remove_all_audience)
    
    def click_wifi_gateway(self):
        self.click_element(self.wifi)
    
    def click_carrier_gateway(self):
        self.click_element(self.carrier)
        
    def click_other_gateway(self):
        self.click_element(self.other)
    
    def select_mobile_options(self, value):
        self.select_option(self.mobile_option, value)
    
    def select_carrier(self, value):
        self.select_option(self.mobile_carrier_avail, value)
    
    def select_applied_carrier(self, value):
        self.select_option(self.mobile_carrier_applied, value)
    
    def click_select_carrier(self):
        self.click_element(self.move_mobile_carrier)
    
    def click_remove_carrier(self):
        self.click_element(self.remove_mobile_carrier)
    
    def click_select_all_carrier(self):
        self.click_element(self.move_all_mobile_carrier)
    
    def click_remove_all_carrier(self):
        self.click_element(self.remove_all_mobile_carrier)
    
    def select_platform(self, value):
        self.select_option(self.mobile_platform_avail, value)
    
    def select_applied_platform(self, value):
        self.select_option(self.mobile_platform_applied, value)
    
    def click_select_platform(self):
        self.click_element(self.move_mobile_platform)
    
    def click_remove_platform(self):
        self.click_element(self.remove_mobile_platform)
    
    def click_select_all_platform(self):
        self.click_element(self.move_all_mobile_platform)
    
    def click_remove_all_platform(self):
        self.click_element(self.remove_all_mobile_platform)
    
    def filter_mobile_devices(self, value):
        self.fill_field(self.devices_filter, value)
    
    def select_designation_filter(self, value):
        self.select_option(self.designation_filter, value)
    
    def click_all_tabs(self):
        self.click_element(self.all_tabs)
    
    def click_all_smartphones(self):
        self.click_element(self.all_smartphones)
    
    def click_all_featurephones(self):
        self.click_element(self.all_feature_phones)
    
    def select_all_manufacturers(self):
        self.click_element(self.select_all_mms)
    
    def expand_first(self):
        self.click_element(self.expand_first_mms)
    
    def select_first_manufacturer(self):
        self.click_element(self.select_first_mms)

    def select_first_model(self):
        self.click_element(self.select_first_model)

    def assert_value(self, element, expected_value):
        element = self.find_element(getattr(self, element))
        actual_value = str(element.get_attribute('value')).strip()
        assert actual_value == expected_value, 'actual value is {0} , expected {1}'.format(actual_value, expected_value)
    
    def check_frquency_cap(self, value):
        expected_text = value + '/1 day'
        self.assert_value('sv_frequency_cap', expected_text)
    
    def verify_selected_channels(self, element, channel = None, channels = None):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            selected.append(option.text)
        if channel:
            assert channel in selected, 'option not present'
        else:
            for channel in channels:
                assert channel in selected, 'option not present'

    def verify_creative_search(self):
        element = self.find_element(self.first_creative)
        creative = str(element.get_attribute('innerHTML'))
        creative = creative.replace('<wbr>', '')
        creative = creative.replace('_', ' ')
        flag = creative.find(str(self.inputs['creative']))
        assert not flag < 0, 'searching creative not present'
    
    def verify_selected_creative(self):
        element = self.find_element(self.first_creative)
        creative = str(element.get_attribute('innerHTML'))
        creative = creative.replace('<wbr>', '')
        creative = creative.strip()
        self.assert_value('sv_creatives', creative)

    def get_audiences(self, element, index = 0):
        widget = self.find_element(getattr(self, element))
        select = Select(widget)
        selected = []
        for option in select.options:
            return option.text
    
    def search_devices(self):
        element = self.find_element(self.devices_td)
        device = str(element.get_attribute('innerHTML'))
        flag = device.find(str(self.inputs['search']))
        assert not flag < 0, 'searching devices not present'
