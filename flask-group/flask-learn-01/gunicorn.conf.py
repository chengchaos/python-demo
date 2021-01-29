# -*- coding:utf-8 -*-
# This file's name is gunicorn.conf.py

workers = 2  # 定义同时开启的处理请求的进程数量，根据流量适当调整
threads = 4  # 每个 Worker 的工作线程数
bind = "0.0.0.0:8341"
worker_class = "gevent"  # 采用 gevent 库，支持一部处理请求，提高吞吐量
worker_connections = 2000  # 最大并发量
# 进程文件目录
# pidfile = 'gunicorn.pid'
accesslog = '/Project/gunicorn_access.log'
errorlog = '/Project/gunicorn_error.log'
loglevel = 'info'
reload = True  # 代码发生变化是否重启
