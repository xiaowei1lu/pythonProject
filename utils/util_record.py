#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/6/8 13:40
 @Author      : xiaowei
"""

import allure
from utils.util_dir import make_dir
from base.base_api import Base
from base.get_log import GetLog
from base.get_driver import GetDriver
log = GetLog.get_logger()

base = Base(GetDriver.get_driver())


def exception_record(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 这里添加所有的异常情况处理
            # 日志
            log.warning("执行过程中发生异常")
            # 截图
            image_path = make_dir("images", "png")
            base.base_image(image_path)
            # page_source
            page_source_path = make_dir("page_source", "html")
            base.base_page_source(page_source_path)
            allure.attach.file(image_path, name="image", attachment_type=allure.attachment_type.PNG)
            # HTML格式page source
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            # 文本格式page source
            # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise e

    return wrapper



