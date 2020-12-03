import pymysql
import tkinter as tk
import os
import random

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='gb2312'
)

if __name__ == '__main__':
    cursor = conn.cursor()
    table =input()
    create_sql = "create table {}" \
          "(" \
          "id int unsigned not null auto_increment primary key," \
          "UID varchar(255) not null," \
          "URL varchar(255) not null" \
          ");"
    cursor.execute(create_sql.format(table))
    conn.commit()
