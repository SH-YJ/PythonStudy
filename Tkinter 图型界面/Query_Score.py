from tkinter import *
import pymysql
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import re

pattern = '[0-9]{8,}'

db = pymysql.Connect(  # 连接mysql
    host='192.168.0.103',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='utf8'
)


def JudgeTF(user, password):  # 判断输入的用户名密码是否正确
    # 利用db方法创建游标对象
    cursor = db.cursor()

    # 利用游标对象execute()方法执行SQL命令
    cursor.execute("select * from ues ")

    data = cursor.fetchall()  # 利用游标对象fetchall()方法获取全部内容
    row = cursor.rowcount
    for i in range(row):
        while user == data[i][0] and password == data[i][1]:
            return True

    cursor.close()


def Judge_user_Exist(user):  # 判断用户名是否存在
    cursor = db.cursor()
    cursor.execute("select * from ues")
    data = cursor.fetchall()  # 获取所有数据
    row = cursor.rowcount  # 获取数据行数
    for i in range(row):
        while data[i][0] == user:
            messagebox.showinfo("提示", "用户名已存在！")
            return False


def Judge_pass(password, sec_password):  # 判断密码是否相同
    if re.match(pattern, password) is None:
        messagebox.showinfo("提示", "密码长度不够，至少8位")
        return False
    elif password != sec_password:
        messagebox.showinfo("提示", "密码不一致")
        return False


def Sign_in(n_user, n_password, nn_password):  # 注册账号
    cursor = db.cursor()
    sql = "insert into UES(user, password) values(%s, %s)"
    if Judge_user_Exist(n_user) is not False and Judge_pass(n_password, nn_password) is not False:
        cursor.execute(sql, [n_user, n_password])
        db.commit()  # 提交到数据库执行
        cursor.close()
        messagebox.showinfo("提示", "注册成功")


def Log_in():  # 主界面登录
    if JudgeTF(entry1.get(), entry2.get()) is True:
        Student()
        messagebox.showinfo("提示", "登录成功！")
    else:
        messagebox.showinfo("提示", "用户名或密码错误！")


def Student():  # 学生界面
    stu = Toplevel()
    stu.title('学生界面')
    stu.geometry('700x700')
    stu.resizable(0, 0)
    root.withdraw()  # 实现窗口的隐藏
    canvas1 = Canvas(stu, width=700, height=700)
    canvas1.pack()

    # 创建画布背景图
    imgpath1 = r'pic/3.png'  # 图片绝对路径
    # imgpath = '5f3757be38934.gif'  当前文件夹下相对路径
    img1 = Image.open(imgpath1)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(350, 350, image=photo1)

    # 创建控件
    en1 = Entry(stu, insertbackground='orange', highlightthickness=0)
    en1.pack()
    en2 = Entry(stu, insertbackground='orange', highlightthickness=0)
    en2.pack()
    canvas1.create_window(350, 50, window=en1)
    canvas1.create_window(350, 80, window=en2)
    x0, y0, x1, y1 = 0, 0, 120, 120
    canvas1.create_arc(x0, y0, x1, y1, fill='red')

    mainloop()


def Sign_Gui():  # 注册界面
    sign = Toplevel()
    sign.title('注册界面')
    sign.resizable(0, 0)
    sign.iconbitmap('pic/1.ico')  # 改变图标
    canvas1 = Canvas(sign)
    canvas1.pack(side='top')
    # 创建标签
    en1 = Entry(sign, insertbackground='orange', highlightthickness=0)
    en1.pack()

    en2 = Entry(sign, insertbackground='orange', highlightthickness=0, show='*')
    en2.pack()

    en3 = Entry(sign, insertbackground='orange', highlightthickness=0, show='*')
    en3.pack()

    canvas1.create_window(100, 50, window=Label(sign, font=('宋体', 10), text='用户名:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 90,
                          window=Label(sign, font=('宋体', 10), width=5, text='密码:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 130,
                          window=Label(sign, font=('宋体', 10), width=7, text='二次密码:', justify='left', padx=5, pady=4))
    # 账号密码输入框
    canvas1.create_window(210, 50, window=en1)
    canvas1.create_window(210, 90, window=en2)
    canvas1.create_window(210, 130, window=en3)

    # 创建画布背景图
    imgpath1 = r'pic/2.png'  # 图片绝对路径
    # imgpath = '5f3757be38934.gif'  当前文件夹下相对路径
    img1 = Image.open(imgpath1)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(350, 350, image=photo1)

    # 创建注册按钮
    canvas1.create_window(210, 200, window=Button(sign, width=15, bg='#d37000', text='注册',
                                                  command=lambda: Sign_in(en1.get(), en2.get(), en3.get())))
    # lambda 有参数函数也不会直接执行
    mainloop()


# 创建根窗口，并添加组件
root = Tk()
root.title('登录')
root.resizable(0, 0)  # 设置窗口大小不可变
root.iconbitmap('pic/1.ico')  # 改变图标

canvas = Canvas(root)
canvas.pack(side='top')

# 下拉菜单
m1 = Menu(root)  # 创建菜单实例
root.config(menu=m1)  # 为窗体设置菜单属性
filemenu = Menu(m1)  # 在m1实例建立新的子菜单实例
m1.add_cascade(label="File", menu=filemenu)  # 在m1实例上设置子菜单并关联子菜单1
filemenu.add_command(label="New")  # 在子菜单增加选择项名称和事件
filemenu.add_separator()  # 增加分隔线

# 创建标签
entry1 = Entry(root, insertbackground='orange', highlightthickness=0)
entry1.pack()

entry2 = Entry(root, insertbackground='orange', highlightthickness=0, show='*')
entry2.pack()

canvas.create_window(100, 50, window=Label(root, font=('宋体', 10), text='用户名', justify='left', padx=5, pady=4))
canvas.create_window(100, 90, window=Label(root, font=('宋体', 10), width=5, text='密码', justify='left', padx=5, pady=4))

# 账号密码输入框
canvas.create_window(210, 50, window=entry1)
canvas.create_window(210, 90, window=entry2)
canvas.create_window(330, 90, window=Label(root, text='忘记密码', fg='red', font=('宋体', 10)))

# 创建画布背景图
imgpath = r'pic/1.png'  # 图片绝对路径
# imgpath = '5f3757be38934.gif'  当前文件夹下相对路径
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(350, 350, image=photo)

# 创建登录按钮
canvas.create_window(250, 200, window=Button(root, width=15, bg='#88CEEB', text='立即登录', command=Log_in))
# 创建注册按钮
canvas.create_window(100, 200, window=Button(root, width=15, bg='#d37000', text='注册', command=Sign_Gui))

mainloop()
