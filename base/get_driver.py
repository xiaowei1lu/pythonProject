#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/06/01 13:55
 @Author      : xiaowei
"""


import os
from selenium import webdriver

from conftest import global_env


class GetDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 多浏览器兼容
            cls.browser = global_env.get('browser')
            if cls.browser == "firefox":
                cls.driver = webdriver.Firefox()
            elif cls.browser == "ie":
                cls.driver = webdriver.Ie()
            elif cls.browser == "headless":
                cls.driver = webdriver.PhantomJS()
            else:
                cls.driver = webdriver.Chrome()
            # 设置全局隐式等待 5s
            cls.driver.implicitly_wait(5)
            # 最大化浏览器
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

