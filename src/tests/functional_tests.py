from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import os
import time
import unittest


MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            staging_server = os.environ.get('abdinasirnoor.com')
            if staging_server:
                self.live_server_url = 'https://' + staging_server

        def tearDown(self):
            self.browser.quit()

        def test_static_files(self):

#  Django test runner intiates the test therefore
#  this code to begin app is unecessary. Keeping
#  this code for historical sake
# if __name__ == '__main__':
#     unittest.main()
