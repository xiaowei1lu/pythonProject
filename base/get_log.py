#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/06/01 13:55
 @Author      : xiaowei
"""

import logging.handlers
from utils.util_dir import make_dir


class GetLog:

    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器级别
            cls.logger.setLevel(logging.DEBUG)
            # 获取处理器 控制台
            stream_handler = logging.StreamHandler()

            # 日志路径
            log_path = make_dir("logs", "log")
            # 获取处理器 文件-以时间分隔
            file_handler = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                                     when="midnight",
                                                                     interval=1,
                                                                     backupCount=30,
                                                                     encoding="utf-8")
            # 设置格式器
            log_format = "%(asctime)s %(levelname)s [%(filename)s %(funcName)s:%(lineno)d] - %(message)s"
            log_formatter = logging.Formatter(log_format)

            # 将格式器添加到 处理器 控制台
            stream_handler.setFormatter(log_formatter)
            # 设置控制台处理器日志级别
            stream_handler.setLevel(logging.DEBUG)

            # 将格式器添加到 处理器 文件
            file_handler.setFormatter(log_formatter)
            # 设置文件处理器日志级别
            file_handler.setLevel(logging.DEBUG)

            # 将处理器添加到 日志器
            cls.logger.addHandler(stream_handler)
            cls.logger.addHandler(file_handler)
        return cls.logger


if __name__ == '__main__':
    log = GetLog().get_logger()
    log.info("halou")

