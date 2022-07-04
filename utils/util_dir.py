#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Description :
 @Time        : 2022/06/01 13:55
 @Author      : xiaowei
"""

import os
import time


def make_dir(root_dir, postfix):
    """
    根据文件目录和文件后缀返回文件绝对路径
    :param root_dir: 要创建的目录名称
    :param postfix: 文件后缀名
    :return: 文件路径
    """
    # 创建文件目录
    if os.path.exists(root_dir) and os.path.isdir(root_dir):
        pass
    else:
        os.mkdir(root_dir)
    # 时间戳
    timestamp = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # 文件名
    file_name = f'{timestamp}.{postfix}'
    # 文件路径
    file_path = os.path.join(root_dir, file_name)
    return file_path
