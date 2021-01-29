# -*- coding:utf-8 -*-
# This file's name is app.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index.asp")
def hello():
    return "Hello me"


if __name__ == "__main__":
    app.run(debug=True)
