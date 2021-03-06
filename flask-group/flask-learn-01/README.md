# flask-learn-01

## for MAC 

### for Terminal

把 venv 放到上层，主要是避免一个小项目生成一个 venv。占无谓的硬盘空间。

```bash

python3 --version
Python 3.9.1

cd github.com/chengchaos/
cd python-demo/flash-group/

python3 -m venv env

## 激活环境
source env/bin/activate
## 或者
. env/bin/activate

## 退出
deactivate

## 安装 flask
pip3 install flask
WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.
You should consider upgrading via the '/Users/chengchao/git-repo/github.com/chengchaos/python-demo/flask-group/env/bin/python3 -m pip install --upgrade pip' command.

/Users/chengchao/git-repo/github.com/chengchaos/python-demo/flask-group/env/bin/python3 -m pip install --upgrade pip

pip3 install flask-restful
pip3 install redis
pip3 install requests
pip3 install PyMySQL
# mysql-connector 是 MySQL 官方提供的驱动
pip3 install mysql-connector
pip3 install flask-sqlalchemy


pip3 freeze > requirements.txt
touch gunicorn_conf.py
cat > gunicorn_conf <EOF
workers = 5
worker_class = "gevent"
bind = "0.0.0.0:8000"
EOF

```

### Docker

FROM : "基础镜像"
MAINTAINER : "维护者信息"
RUN : "先干点啥"
ADD : COPY 文件进来
WORKDIR : ”工作目录“
VOLUME : "目录挂载"
EXPOSE : "开放的端口"
RUN : "运行"


```dockerfile
FORM python:3
MAINIAINER chengchaos@gmail.com
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "app_flask:app", "-c", "./gunicorn_conf.py"]
```

```bash
docker build -t flask_demo:1 .

```
### for IntelliJ IDEA / PyCharm

## MySQL (mysql-connector)

[https://www.runoob.com/python3/python-mysql-connector.html](https://www.runoob.com/python3/python-mysql-connector.html)

> 注意：如果你的 MySQL 是 8.0 版本，密码插件验证方式发生了变化，早期版本为 `mysql_native_password`，8.0 版本为 `caching_sha2_password`，所以需要做些改变：

先修改 my.ini 配置：

```ini
[mysqld]
default_authentication_plugin=mysql_native_password
```

然后在 mysql 下执行以下命令来修改密码：

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
```
