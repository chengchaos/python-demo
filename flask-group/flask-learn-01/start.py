# -*- coding:utf-8 -*-
# This file's name is start.py.py

# 从 project 文件夹中的 __init__.py 中导入 create_app 函数
from project import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
