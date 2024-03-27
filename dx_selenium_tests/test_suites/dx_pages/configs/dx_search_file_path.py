import os

class SearchFilePath(object):

    def __init__(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                setattr(self, 'file_name', os.path.join(root, name))
