import pymysql
from tkinter import *

db = pymysql.Connect(  # 连接mysql
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='utf8'
)

root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)

root.title("tkinter frame")

label = Label(fr1, text="Label", justify=LEFT)
label.pack(side=LEFT)

hi_there = Label(fr2, text="say hi~")
hi_there.pack()

fr1.pack(padx=1, pady=1)
fr2.pack(padx=10, pady=10)

root.mainloop()