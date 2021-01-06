# -*- coding:utf-8 -*-
# 文件名： using_sys.py

import sys


def echo():
    print("命令参数：")
    for i in sys.argv:
        print(i)

    print("\n\nPython 路径为： ", sys.path, "\n")
