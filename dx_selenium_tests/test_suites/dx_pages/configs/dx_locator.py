import yaml
import os

from dx_yaml_loader import Loader
from dx_search_file_path import SearchFilePath

class DXLocator(object):

    def __init__(self, locator_name):
        file_to_search = locator_name + '.yml'
        _file = SearchFilePath(file_to_search, os.path.abspath(os.path.dirname(__file__) + '/../../../configs/locators/')).file_name
        with open(_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader)
        data = cfg[locator_name]
        setattr(self, locator_name, data)
