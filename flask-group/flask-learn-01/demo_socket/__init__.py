# -*- coding:utf-8 -*-
# File name is __init__.py
# https://www.runoob.com/python3/python3-socket.html
# 日志:
# https://www.cnblogs.com/yuanyongqiang/p/11913812.html
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
)


def change_this():
    logging.debug("kao")
    logging.info("info")
    return


if __name__ == "__main__":
    print("nothing.")
    change_this()
