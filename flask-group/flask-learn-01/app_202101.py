# -*- coding:utf-8 -*-
# 导入 Flask
import builtins

import redis as redis
from flask import Flask, render_template, url_for, redirect, session, abort
from flask import request
import requests as requests
import json as json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import config

app = Flask(__name__, static_folder="static", template_folder="templates")

# 配置文件实例化
app.config.from_object(config)

db = SQLAlchemy(app)


# 创建数据库
# db.create_all()

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now)

db.create_all()

app.logger.debug("__name__ => ", __name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

USER_KEY_REDIS = "login-user"
USER_KEY_SESSION = "user"

redis_helper = redis.StrictRedis(host="127.0.0.1", port=6379, db=0, password='DvBrBY8yiii_7')


@app.route("/say-hai", methods=['GET'])
def say_hai():
    # builtins.print(Flask.__doc__)
    return {
        "message": "hello world"
    }


# @app.errorhandler(401)
@app.route("/user-login.asp", methods=['GET'])
def user_login_view():
    app.logger.debug('debug as user_login_view!')
    app.logger.info('info as user_login_view!')
    app.logger.warning('warning as user_login_view!')
    app.logger.error('error as user_login_view!')
    admin = "admin"
    random = "1379"
    # 使用 **locals() 可以传入全部的本地变量。
    return render_template("user-login.html", **locals())


@app.route("/user-login-auth.asp", methods=['POST'])
def user_login_auth():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)

    saved_pwd = redis_helper.hget("auth-hash", username)

    if saved_pwd is None:
        target = url_for("user_login_view")
    elif saved_pwd.decode() != password:
        target = url_for("user_login_view")
    else:
        session[USER_KEY_SESSION] = username
        target = url_for("index")

    print(target)
    return redirect(target)


@app.route("/user-log-out.asp")
def user_logout():
    session.pop(USER_KEY_SESSION)
    return redirect(url_for("user_login_view"))


@app.route("/", methods=['GET'])
@app.route("/index.asp")
def index():
    print("request.path => ", request.path)
    print("request.full_path => ", request.full_path)

    username = session.get(USER_KEY_SESSION)
    print("username => ", str(username))

    if username is None:
        # abort(401)
        return redirect(url_for("user_login_view"))

    info = request.args.get("info", "WTF!")
    name = redis_helper.get(USER_KEY_REDIS)
    if name is None:
        name = "chengchao"
        redis_helper.set(USER_KEY_REDIS, name)
    else:
        # 一种方法时是使用 str
        # name = str(name, encoding='utf-8')
        # 一种方法是使用 decode()
        name = name.decode()

    get_some_data()

    return render_template("index.html", name=info)


def get_some_data():
    url = "http://127.0.0.1:8080/some-data"
    headers = {"content-type": "application/json"}
    request_data = {"name": "chengchao", "age": 28}

    res = requests.post(url, json=request_data, headers=headers)

    if res.status_code == 200:
        text = res.text

        jstr = json.loads(text)
        print("json => ", jstr)
        m1 = jstr['message']
        print("m1 => ", m1)


@app.route("/some-data", methods=['GET', 'POST'])
def some_data():
    return {
        "message": "Are you OK?"
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
