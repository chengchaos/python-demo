# -*- coding:utf-8 -*-
# This file's name is log_config.py
# 日志:
# https://www.cnblogs.com/yuanyongqiang/p/11913812.html
import logging


def init_basic_config():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
    )
