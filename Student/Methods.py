import pymysql

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='utf8'
)


def ConnectSql(sql):
    cursor = conn.cursor()  # 利用conn方法创建游标方法
    cursor.execute(sql)  # 利用游标对象execute()方法执行SQL命令
    data = cursor.fetchall()  # 利用游标对象fetchall()方法获取全部内容
    row = cursor.rowcount  # 获取数据的行数
    list1 = []
    for i in range(row):
        list1.append(data[i][0])
    cursor.close()  # 关闭游标
    return list1




if __name__ == '__main__':
   list2 = ['select 姓名 from student where 姓名 like "%伟%"','select 性别 from student where 姓名 like "%伟%"','select 学号 from student','select 成绩 from student']
   for i in list2:
       print(ConnectSql(i))