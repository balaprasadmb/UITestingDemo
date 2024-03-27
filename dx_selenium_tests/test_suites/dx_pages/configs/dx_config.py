import yaml
import os.path

from dx_search_file_path import SearchFilePath

class DXConfig(object):

    def __init__(self):
        config_file = SearchFilePath('dx_config.yml', os.path.abspath(os.path.dirname(__file__) + '/../../../configs/')).file_name
        with open(config_file, 'r') as ymlfile:
             cfg = yaml.load(ymlfile)
        for key, value in cfg.iteritems():
            setattr(self, key, value)
