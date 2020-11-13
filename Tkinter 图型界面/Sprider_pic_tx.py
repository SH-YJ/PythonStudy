import requests
from bs4 import BeautifulSoup
import re
import tkinter
import tkinter.messagebox as messagebox
import threading
import os


def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


def download():
    html_url = getUrl(entry1.get())
    all_url = re.findall('<a href="(.*?)" class="img" target=".*?">', html_url)
    for url in all_url:
        try:
            I_url = 'https://www.woyaogexing.com/' + url
            II_url = getUrl(I_url)
            soup = BeautifulSoup(II_url, "html.parser")
            file_name = re.findall('<h1>(.*?)</h1>', II_url)[-1]
            all_img = soup.find('ul', class_='artCont cl').find_all('img')
            for img in all_img:
                src = img['src']
                img_url = 'https:' + src
                root = entry3.get() + str(file_name) + '/'  # 保存的路径
                path = root + img_url.split('/')[-1]  # 获取img的文件名
                print(path)
                try:
                    if not os.path.exists(root):  # 判断是否存在文件并下载img
                        os.mkdir(root)
                    if not os.path.exists(path):
                        read = requests.get(img_url)
                        with open(path, "wb")as f:
                            f.write(read.content)
                            f.close()
                            print("文件保存成功！")
                    else:
                        print("文件已存在！")
                except:
                    print("文件爬取失败！")
        except:
            print("未找到图片网址")
    messagebox.showinfo('提示', '下载完成')


def thread_it(func, *args):  # 开线程防止卡死
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


head = tkinter.Tk()
head.title("爬取头像")
head.geometry("400x400")
head.resizable(0, 0)
head.iconbitmap('5f4226701e4e0.128px.ico')

label1 = tkinter.Label(head, text="输入地址:", fg="pink", bg="gray", width=9, height=1, font=("黑体", 15), justify="left",
                       anchor="w")
label1.pack()

entry1 = tkinter.Entry(head, width=50)
entry1.pack()

label3 = tkinter.Label(head, text="输入保存路径:", fg="Wheat", bg="LimeGreen", width=13, height=1, font=("黑体", 15),
                       justify="left", anchor="w")
label3.pack()

entry3 = tkinter.Entry(head, width=50)
entry3.pack()

button = tkinter.Button(head, text="获取图片", bg="orange", fg="purple", command=lambda: thread_it(download)).pack()

head.mainloop()
