# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine  # python中一个通过ORM操作数据库的框架

# 具体格式是dialect[+driver]: //user:password@host/dbname[?key=value…]
# dialect :指定连接数据库类型 我填的是mysql
# driver：驱动，也就是数据库连接驱动，python中数据库的连接驱动挺多的，我使用的是pymysql
# user：数据库的用户名
# password：数据库的密码
# host：主机地址 本地通常是localhost 或者127.0.0.1
# dbname：数据库库名


conn = create_engine('mysql+pymysql://syj:syj21408@localhost:3306/url?charset=utf8')


def reader(sql):
    data = pd.read_sql(sql, conn)
    return data


def write():
    data = pd.read_excel('xyz.xlsx')
    print(data.head())
    try:
        data.to_sql('福利姬', conn, if_exists='replace', index=False)
        # data.to_sql(‘表名’，连接器，if_exists=’ ') if_exists 这个属性有三种值，为fail时，如果次表名重复，则报错；为replace时，删除已存在的这个表。
    except:
        print('error')


if __name__ == '__main__':
    write()