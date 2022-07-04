# -*- coding: utf-8 -*-
"""
@Description:
@version: V1.0
@Company: FT
@Author: xiao
@Time: 2022-07-01 13:24
"""

import os
import json
import pytest

global_env = {}


# 接收命令行选项-b选项的值，存到browser变量中，如果不指定命令行选项，browser变量默认值是chrome
def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     dest="browser",
                     default="chrome",
                     help="browser support: chrome/firefox/ie/headless")


def pytest_configure(config):
    browser = config.getoption('browser', default='chrome')
    browser_conf = {'browser': browser}
    global_env.update(browser_conf)
