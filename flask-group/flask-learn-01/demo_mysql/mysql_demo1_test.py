# -*- coding:utf-8 -*-
# This file's name is mysql_demo1_test.py
import unittest
import logging
# from demo_mysql import mysql_demo1
import mysql_demo1
import log_config

log_config.init_basic_config()


class MysqlDemo1TestCase(unittest.TestCase):
    """测试 MySQL Demo1"""

    def test_select(self):
        res = mysql_demo1.get_sites("google")
        for x in res:
            print("x => "+ str(x))

        self.assertTrue(True)


if __name__ == "__main__":
    logging.info("test get")
    unittest.main()
