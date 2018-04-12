#!/usr/bin/env python
"""
Created on 4/10/18

@author: 'Jiezhi.G@gmail.com'

Reference:
"""
import sys
from unittest import skip

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.fail('wirte me!')
