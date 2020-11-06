import pymysql

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='gb2312'
)

# 利用db方法创建游标对象
cursor = db.cursor()

# 利用游标对象execute()方法执行SQL命令
cursor.execute("select * from user")

data = cursor.fetchall()  # 利用游标对象fetchall()方法获取全部内容

for i in range(3):
    print(data[i][0], data[i][1])

# db.commit()  # 提交到数据库执行

cursor.close()
db.close()
