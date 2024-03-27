import yaml

import os
import sys

class ManageOrganizations(object):

    def __init__(self):
        self.file_path = os.path.dirname(__file__) + "/../configs/dx_constants.yml"
        with open(self.file_path, 'r') as ymlfile:
            self.file_data = yaml.load(ymlfile)

    def override_advertiser(self, advertiser):
        self.file_data["advertiser_name"] = "{0}".format(advertiser)
        with open(self.file_path, 'w') as yaml_file:
            yaml_file.write( yaml.dump(self.file_data, default_flow_style=False))

    def override_agency(self, agency):
        self.file_data["agency_name"] = "{0}".format(agency)
        with open(self.file_path, 'w') as yaml_file:
            yaml_file.write( yaml.dump(self.file_data, default_flow_style=False))

    def override_agency_group(self, agency_group):
        self.file_data["agency_group_name"] = "{0}".format(agency_group)
        with open(self.file_path, 'w') as yaml_file:
            yaml_file.write( yaml.dump(self.file_data, default_flow_style=False))
