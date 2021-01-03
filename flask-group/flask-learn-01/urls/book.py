# -*- coding:utf-8 -*-

import pymysql


class User:
    def __init__(self, name, pwd, user_id):
        self.name = name
        self.pwd = pwd
        self.user_id = user_id


def test_db_01():
    # 连接数据库
    db = pymysql.connect("localhost", "chengchao", "Ab1234++", "demo_01")

    # 创建游标
    cursor = db.cursor()

    # Execute
    cursor.execute("select * from user")
    data = cursor.fetchall()

    print(type(data))
    print(data)

    users = []
    for row in data:
        username = row[0]
        password = row[1]
        user_id = row[2]
        user = User(username, password, user_id)
        users_len = len(users)
        print("user_len => ", users_len)
        users.append(user)

    cursor.close()
    db.close()

    return users


if __name__ == "__main__":
    users = test_db_01()
    for u in users:
        print(" u => ", u.name)
