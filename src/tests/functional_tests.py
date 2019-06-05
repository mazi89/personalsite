from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import os
import time
import unittest


MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()

        def test_browse_to_site(self):
            self.browser.get('https://abdinasirnoor.com')
            time.sleep(MAX_WAIT)
            self.assertIn("Python", driver.title)

        def tearDown(self):
            self.browser.quit()


if __name__ == '__main__':
    unittest.main()
