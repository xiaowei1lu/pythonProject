#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/06/01 13:55
 @Author      : xiaowei
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from base.get_driver import GetDriver
from utils.util_dir import make_dir
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Base:

    # =====================
    # 初始化
    # =====================
    def __init__(self, driver: webdriver):
        self.driver = driver

    # def __init__(self):
    #     self.driver = GetDriver.get_driver()

    # =====================
    # 浏览器操作
    # =====================

    # 打开网址
    def base_get(self, url):
        self.driver.get(url)

    # 获取当期url
    def base_current_url(self):
        return self.driver.current_url

    # 刷新
    def base_refresh(self):
        self.driver.refresh()

    # 前进
    def base_forward(self):
        self.driver.forward()

    # 后退
    def base_back(self):
        self.driver.back()

    # =====================
    # 元素定位
    # =====================

    # 查找页面元素
    def base_find_element(self, location, timeout=10, poll=0.1):
        """
        :param location:
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(*location))

    # 多元素查找
    def base_find_elements(self, location):
        return self.driver.find_elements(*location)

    """"控件交互"""

    # 元素点击操作
    def base_click(self, location):
        WebDriverWait(self.driver).\
            until(expected_conditions.element_to_be_clickable(location)).\
            click()

    # 元素输入操作
    def base_input(self, location, value):
        el = self.base_find_element(location)
        el.clear()
        el.send_keys(value)

    # 获取元素文本操作
    def base_get_text(self, location):
        return self.base_find_element(location).text

    # 判断元素是否存在
    def base_element_is_exist(self, location):
        try:
            self.base_find_element(location, timeout=2)
            return True
        except:
            return False

    # =====================
    # 数据记录
    # =====================
    # 截图
    def base_image(self, image_path):
        self.driver.get_screenshot_as_file(image_path)

    # page source
    def base_page_source(self, path):
        with open(path, "w", encoding="u8") as f:
            f.write(self.driver.page_source)

    # =====================
    # 下拉列表操作
    # =====================

    def base_select_options(self, location):
        """
        返回所有的选项个数
        :return:
        """
        el = self.base_find_element(location)
        optionList = Select(el).options
        count = len(optionList)
        return count

    def base_select_by_value(self, location, value):
        """
        根据选项值选择
        :return:
        """
        el = self.base_find_element(location)
        Select(el).select_by_value(value)

    def base_select_by_index(self, location, index):
        """
        根据选项值选择
        :return:
        """
        el = self.base_find_element(location)
        Select(el).select_by_index(index)

    # =====================
    # 鼠标操作ActionChains
    # =====================

    def base_move_to_element(self, location):
        """
        鼠标移动到元素上
        """
        # el = self.base_find_element(location)
        ActionChains(self.driver). \
            move_to_element(self.base_find_element(location)). \
            perform()

    def base_move_to_element_click(self, location):
        """
        鼠标移动到元素上点击
        """
        # el = self.base_find_element(location)
        ActionChains(self.driver). \
            move_to_element(self.base_find_element(location)). \
            click(). \
            perform()

    def base_click_right(self, location):
        """右键单击"""
        ActionChains(self.driver). \
            context_click(self.base_find_element(location)). \
            perform()

    # =====================
    # frame操作
    # =====================
    def base_switch_to_frame(self, frame):
        """切换至指定Frame"""
        self.driver.switch_to.frame(frame)

    def base_switch_to_default_frame(self):
        """返回默认Frame"""
        self.driver.switch_to.default_content()

    def base_switch_to_parent_frame(self):
        """跳出子iframe,进入父iframe"""
        self.driver.switch_to.parent_frame()

    # =====================
    # window操作
    # =====================

    # 获取当前窗口句柄
    def base_get_current_window(self):
        return self.driver.current_window_handle

    # 获取所有窗口句柄
    def base_get_windows(self):
        return self.driver.window_handles

    # 切换窗口，句柄的顺序：先出现的先加入列表。后出现的，后加入列表。
    def base_switch_to_window(self, window):
        self.driver.switch_to.window(window)
