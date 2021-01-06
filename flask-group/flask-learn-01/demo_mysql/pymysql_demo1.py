# -*- coding:utf-8 -*-
# File name is pymysql_demo1
import pymysql
import log_config
import logging

log_config.init_basic_config()
conn = pymysql.connect(
    host="192.168.56.102",
    user="chengchao",
    password="Ab1234++",
    database="my_demo1",
    port=3306
)


def show_version(db_conn):
    db_cursor = db_conn.cursor()
    db_cursor.execute("select version()")
    data = db_cursor.fetchone()

    return data


if __name__ == "__main__":
    version = show_version(conn)
    print("version => %s " % version)
    logging.info("version => %s" % version)
    conn.close()
