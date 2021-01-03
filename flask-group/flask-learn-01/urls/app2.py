# -*- coding:utf-8 -*-
from flask import Flask
from flask import url_for

import pymysql


app = Flask(__name__)


@app.route("/")
def hello_url():
    # url_for 中的参数是函数名。
    url1 = (url_for("list_news", id=100))
    return "这是 url 参数演示, url = %s" % url1


@app.route("/user/<name>")
def get_user_name(name):
    return "接收的名称为： %s " % name


@app.route("/news/<int:id>")
def list_news(id):
    return "接收到的 ID 为： %s" % id



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
