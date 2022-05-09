#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2021/11/11 13:55
 @Author      : xiaowei
"""

import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找页面元素
    def base_find(self, location, timeout=30, poll=0.5):
        """
        :param location:
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*location))

    # 元素点击操作
    def base_click(self, location):
        self.base_find(location).click()

    # 元素输入操作
    def base_input(self, location, value):
        el = self.base_find(location)
        el.clear()
        el.send_keys(value)

    # 获取元素文本操作
    def base_get_text(self, location):
        return self.base_find(location).text

    # 判断元素是否存在
    def base_element_is_exist(self, location):
        try:
            self.base_find(location, timeout=2)
            return True
        except:
            return False

    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("Y%-m%-d% H%:M%:S%")))
