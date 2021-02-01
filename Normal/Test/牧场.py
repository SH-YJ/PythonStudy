import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
import threading


def form():
    username = ''.join(random.sample(string.ascii_letters, 4))
    qq = ''.join(random.sample(string.digits, 9))
    password = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    file = open('Source/牧场账号密码.txt', 'w', encoding='UTF-8')
    file.write(username + '\n')
    file.write(qq + '\n')
    file.write(password + '\n')


def register(username, qq, password):
    try:
        option = Options()
        option.add_argument('--headless')
        browser = webdriver.Chrome(options=option)
        browser.get('https://mcwy.club/auth/login')
        time.sleep(5)
        browser.find_elements_by_xpath('.//div[@class="mt-10"]/a')[0].click()
        browser.find_elements_by_id('name')[0].send_keys(username)
        browser.find_elements_by_id('email')[0].send_keys(qq)
        browser.find_elements_by_id('passwd')[0].send_keys(password)
        browser.find_elements_by_id('repasswd')[0].send_keys(password)
        browser.find_elements_by_xpath(
            './/label[@class="checkbox checkbox-outline checkbox-white text-white m-0"]/span')[
            0].click()
        browser.find_elements_by_id('register_submit')[0].click()
        messagebox.showinfo('提示', '注册成功！')
    except TimeoutError:
        messagebox.showinfo('提示', '网络连接超时！')


def read_info():
    file = open('Source/牧场账号密码.txt', 'r', encoding='UTF-8')
    information = file.readlines()
    username = information[0]
    qq = information[1]
    password = information[2]
    return username, qq, password


def thread_it(func, *args):  # 开线程防止卡死
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


if __name__ == '__main__':
    form()
    info = read_info()
    root = tkinter.Tk()
    root.title('牧场账号获取')
    root.geometry('400x200')
    root.resizable(0, 0)
    root.iconbitmap('Source/mcwy.ico')

    l1 = tkinter.Label(root, text='牧场网页地址：https://mcwy.club/auth/login', bg='orange', fg='purple').pack()
    l2 = tkinter.Label(root, text='0开头不要注册！邮箱均为QQ邮箱!', fg='red').pack()
    l3 = tkinter.Label(root, text='使用谷歌浏览器实现，浏览器安装位置需是默认位置！', fg='red').pack()
    btn1 = tkinter.Button(root, text='注册随机账号', command=lambda: thread_it(register, info[0], info[1], info[2]))
    btn1.pack()

    Ft_Song = tkFont.Font(family='宋体', size=15, weight=tkFont.BOLD)
    t1 = tkinter.Text(root, height=5, width=35, relief='groove', font=Ft_Song)
    t1.pack()
    t1.insert('end', '用户名:' + info[0])
    t1.insert('end', '邮箱：' + info[1])
    t1.insert('end', '密码：' + info[2])

    root.mainloop()