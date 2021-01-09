# -*- coding:utf-8 -*-
# File name is mysql_demo1

import mysql.connector

conn = mysql.connector.connect(
    host="192.168.56.102",
    user="chengchao",
    password="Ab1234++",
    database="my_demo1",
)


def insert_one(db_conn, name):
    dbcursor = db_conn.cursor()
    data_sql = "insert into site (name, url) values (%s, %s)"
    data_var = (name, "https://cn.bing.com")
    dbcursor.execute(data_sql, data_var)
    db_conn.commit()
    return dbcursor.lastrowid


def insert_batch(db_conn):
    data_sql = "insert into site (name, url) values (%s, %s)"
    data_var = [
        ('google', "https://www.google.com"),
        ("github", "https://github.com")
    ]
    db_cursor = db_conn.cursor()
    db_cursor.executemany(data_sql, data_var)
    db_conn.commit()


def get_sites(name):
    db_sql = "SELECT name, url FROM site WHERE name = %s"
    db_cursor = conn.cursor()
    db_cursor.execute(db_sql, (name, ))
    db_result = db_cursor.fetchall()
    db_cursor.close()
    return db_result



if __name__ == "__main__":
    print(conn)
    cursor = conn.cursor()
    # cursor.execute("create database my_demo1")
    # cursor.execute("create table site(name varchar(25), url varchar(255))")
    # insert_one(db_conn=conn)
    # insert_batch(db_conn=conn)
    rowid = insert_one(conn, 'bing3')
    conn.close()
    print("添加记录完成。%s" % rowid)
