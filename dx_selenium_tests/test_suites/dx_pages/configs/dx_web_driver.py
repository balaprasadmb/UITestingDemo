from pytractor.webdriver import Firefox

class DXWebDriver(object):

    def __init__(self):
        self.driver = None

    def get_browser(self):
        if self.driver != None:
            return self.driver
        else:
            self.driver = Firefox()
            self.driver.ignore_synchronization = True
            return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
