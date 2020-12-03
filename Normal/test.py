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
    charset='utf8'
)

if __name__ == '__main__':
    cursor = conn.cursor()
    table =input()
    create_sql = "create table {}" \
          "(" \
          "id int unsigned not null auto_increment primary key," \
          "我 varchar(255) not null," \
          "十大 varchar(255) not null" \
          ");"
    sql = "insert ignore into 高崎聖子(UID, URL) value('MIDE-862', 'https://javdb6.com/v/mP8g5')"
    cursor.execute(create_sql.format(table))
    conn.commit()

