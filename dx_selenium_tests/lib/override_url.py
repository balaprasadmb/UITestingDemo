import sys
import os
import yaml

class ReplaceURLValue(object):
    def override_url(self, url):
        file_path = os.getcwd() + "/configs/dx_config.yml"
        with open(file_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        new_url = "http://{0}/".format(url)
        cfg["URL"] = "{0}".format(new_url)
        with open(file_path, 'w') as yaml_file:
            yaml_file.write( yaml.dump(cfg, default_flow_style=False))

ReplaceURLValue().override_url(sys.argv[1])
