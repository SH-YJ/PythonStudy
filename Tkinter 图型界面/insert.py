import pymysql

db = pymysql.Connect(  # 连接mysql
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='utf8'
)

cursor = db.cursor()

sql = "insert into UES values(%s,%s)"
data = ('asd', '123456')

cursor.execute(sql , data)

db.commit()
cursor.close()
db.close()