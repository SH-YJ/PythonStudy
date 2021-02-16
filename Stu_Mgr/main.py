from tkinter import *
import pymysql, re, smtplib, random, string, threading
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
from email.mime.text import MIMEText
from email.utils import formataddr

pattern = '[0-9A-Za-z]{8,}'  # 正则匹配大于等于8位的密码（包括数字字母）
sender = '2973211152@qq.com'  # 发件人邮箱账号
auth_code = 'udrswmyafeavdfhj'  # 邮箱授权码
ver_code = ''.join(random.sample(string.digits + string.ascii_letters, 6))  # 随机验证码

db = pymysql.Connect(  # 连接mysql
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='url',
    charset='utf8'
)


def thread_it(func, *args):  # 开线程防止卡死
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def mail(receiver):
    content = '<p><h3>您的验证码为：</h3></p></p><h1>{}</h1></p>'.format(ver_code)
    if Judge_Email_Exist(receiver) is False:
        messagebox.showinfo('提示', '该邮箱已被注册！')
        return None
    try:
        msg = MIMEText(content, 'html', 'utf-8')  # # 第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msg['From'] = formataddr(("SH_YJ", sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(("FK", receiver))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "注册账号 邮箱验证！"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(sender, auth_code)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        messagebox.showinfo('提示', '验证码发送成功！')
    except:
        messagebox.showinfo('提示', '验证码发送失败！')


def Judge_ver_code(ver_code, input_code):
    if bool(re.match(ver_code, input_code, re.IGNORECASE)) is False:
        messagebox.showinfo('提示', '验证码不正确！')
        return False


def JudgeTF(user, password):  # 判断输入的用户名密码是否正确
    # 利用db方法创建游标对象
    cursor = db.cursor()

    # 利用游标对象execute()方法执行SQL命令
    cursor.execute("select * from ues")

    data = cursor.fetchall()  # 利用游标对象fetchall()方法获取全部内容
    row = cursor.rowcount
    for i in range(row):
        while user == data[i][0] and password == data[i][1]:
            return True

    cursor.close()


def Judge_Email_Exist(email):  # 判断邮箱是否注册
    cursor = db.cursor()
    cursor.execute("select * from ues")
    data = cursor.fetchall()  # 获取所有数据
    row = cursor.rowcount  # 获取数据行数
    for i in range(row):
        while data[i][2] == email:
            messagebox.showinfo("提示", "该邮箱已被注册！")
            return False


def Judge_Pass(password, sec_password):  # 判断密码是否相同
    if re.match(pattern, password) is None:
        messagebox.showinfo("提示", "密码长度不够，至少8位")
        return False
    elif password != sec_password:
        messagebox.showinfo("提示", "密码不一致")
        return False


def Sign_In(n_user, n_email, n_password, nn_password, n_code):  # 注册账号
    cursor = db.cursor()
    sql = "insert into UES(user, password, Email) values(%s, %s, %s)"
    if Judge_Email_Exist(n_email) is not False and Judge_Pass(n_password, nn_password) is not False and Judge_ver_code(
            ver_code, n_code) is not False:
        cursor.execute(sql, [n_user, n_password, n_email])
        db.commit()  # 提交到数据库执行
        cursor.close()
        messagebox.showinfo("提示", "注册成功")


def Log_In():  # 主界面登录
    if JudgeTF(entry1.get(), entry2.get()) is True:
        Student()
        messagebox.showinfo("提示", "登录成功！")
    else:
        messagebox.showinfo("提示", "用户名或密码错误！")


def Student():  # 学生界面
    stu = Toplevel()
    stu.title('学生界面')
    stu.geometry('400x400')
    stu.iconbitmap('Source/2.ico')
    stu.resizable(0, 0)
    root.withdraw()  # 实现根窗口的隐藏

    # 创建控件
    en1 = Entry(stu, insertbackground='orange', highlightthickness=0)
    en1.pack()
    en2 = Entry(stu, insertbackground='orange', highlightthickness=0)
    en2.pack()
    btn = Button(stu, text="查询", relief='raised')
    btn.pack()
    t1 = Text(stu, width=50, height=10, relief='flat')
    t1.pack()

    # 利用db方法创建游标对象
    cursor = db.cursor()

    # 利用游标对象execute()方法执行SQL命令
    cursor.execute("select * from student ")

    data = cursor.fetchall()  # 利用游标对象fetchall()方法获取全部内容
    row = cursor.rowcount
    for i in range(row):
        t1.insert('end', data[i][0] + '\n')

    stu.mainloop()


def Sign_Gui():  # 注册界面
    sign = Toplevel()
    sign.title('注册界面')
    sign.resizable(0, 0)
    sign.iconbitmap('Source/1.ico')  # 改变图标
    canvas1 = Canvas(sign)
    canvas1.pack(side='top')
    # 创建标签
    en1 = Entry(sign, insertbackground='orange', highlightthickness=0)
    en1.pack()

    en2 = Entry(sign, insertbackground='orange', highlightthickness=0)
    en2.pack()

    en3 = Entry(sign, insertbackground='orange', highlightthickness=0, show='*')
    en3.pack()

    en4 = Entry(sign, insertbackground='orange', highlightthickness=0, show='*')
    en4.pack()

    en5 = Entry(sign, insertbackground='orange', highlightthickness=0)
    en5.pack()

    canvas1.create_window(100, 40, window=Label(sign, font=('宋体', 10), text='用户名:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 70, window=Label(sign, font=('宋体', 10), text='邮箱:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 100,
                          window=Label(sign, font=('宋体', 10), width=5, text='密码:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 130,
                          window=Label(sign, font=('宋体', 10), width=7, text='二次密码:', justify='left', padx=5, pady=4))
    canvas1.create_window(100, 160, window=Label(sign, font=('宋体', 10), text='验证码:', justify='left', padx=5, pady=4))
    # 账号密码输入框
    canvas1.create_window(210, 40, window=en1)
    canvas1.create_window(210, 70, window=en2)
    canvas1.create_window(210, 100, window=en3)
    canvas1.create_window(210, 130, window=en4)
    canvas1.create_window(210, 160, window=en5)

    # 创建画布背景图
    imgpath1 = 'Source/2.png'  # 图片绝对路径
    img1 = Image.open(imgpath1)
    photo1 = ImageTk.PhotoImage(img1)
    canvas1.create_image(350, 350, image=photo1)

    # 创建注册按钮
    canvas1.create_window(250, 200, window=Button(sign, width=15, bg='#d37000', text='注册',
                                                  command=lambda: Sign_In(en1.get(), en2.get(), en3.get(), en4.get(),
                                                                          en5.get())))
    canvas1.create_window(100, 200, window=Button(sign, width=15, bg='#d37000', text='发送验证码',
                                                  command=lambda: thread_it(mail(en2.get()))))
    mainloop()


# 创建根窗口，并添加组件
root = Tk()
root.title('登录')
root.resizable(0, 0)  # 设置窗口大小不可变
root.iconbitmap('Source/1.ico')  # 改变图标

canvas = Canvas(root)
canvas.pack(side='top')

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
imgpath = 'Source/1.png'  # 图片绝对路径
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(350, 350, image=photo)

# 创建登录按钮
canvas.create_window(250, 200, window=Button(root, width=15, bg='#88CEEB', text='立即登录', command=Log_In))
# 创建注册按钮
canvas.create_window(100, 200, window=Button(root, width=15, bg='#d37000', text='注册', command=Sign_Gui))

mainloop()
