# python-demo

## 使用 Docker 部署

参考： [https://zhuanlan.zhihu.com/p/78432719](https://zhuanlan.zhihu.com/p/78432719)

### Gunicorn + Gevent

安装：

```bash
pip install gunicorn gevent
```
编辑 gunicorn.conf.py 文件：

```python
# -*- coding:utf-8 -*-
# This file's name is gunicorn.conf.py

workers = 5  # 定义同时开启的处理请求的进程数量，根据流量适当调整
worker_class = "gevent"  # 采用 gevent 库，支持一部处理请求，提高吞吐量
bind = "0.0.0.0:8788"

```

启动一下试一试：

```shell
gunicorn app:app -c gunicorn.conf.py
```

创建 Dockerfile 文件

```shell
touch Dockfile
vim Dockfile
FROM python:3.6
WORKDIR /Project/demo

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]

:wq

docker build -t 'testflask' .
```
启动

```shell
docker run -d --name mytest -p 8080:8341 testflask
```