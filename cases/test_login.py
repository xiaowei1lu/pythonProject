#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/6/8 14:42
 @Author      : xiaowei
"""

from base.get_driver import GetDriver
from selenium.webdriver.common.by import By

from utils.util_record import exception_record


class Test123:
    def setup(self):
        self.driver = GetDriver.get_driver()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        GetDriver.quit_driver()

    @exception_record
    def test_123(self):
        self.driver.find_element(By.ID, "kw").send_keys("123")
        self.driver.find_element(By.ID, "su11")
