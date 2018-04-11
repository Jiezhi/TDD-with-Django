#!/usr/bin/env python
"""
Created on 4/10/18

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_start(self):
        self.browser.get('http://localhost:8000/credit/test/')
        self.assertIn('Django', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
