#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2021/11/11 15:13
 @Author      : xiaowei
"""
from selenium import webdriver

import page


class GetDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
