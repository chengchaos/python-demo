# -*- coding:utf-8 -*-

DIALECT = 'MySQL'
# DRIVER = 'MySQLdb' # pythn 2。x
DRIVER = 'pyMySQL'
USERNAME = 'chengchao'
PASSWORD = 'Ab1234++'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'demo_01'

SQLALCHEMY_DATABASE_URL = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)

# 固定格式化实例
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 查询时现实原始 sql
SQLALCHEMY_ECHO = True
