import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from Methods import *
import threading


def thread_it(fun, *args):
    thread = threading.Thread(target=fun, args=args)
    thread.setDaemon(True)
    thread.start()


root = tk.Tk()  # 设置根目录
root.resizable(0, 0)  # 设置窗口大小不可变
root.title("笔趣阁")  # 设置窗体名称

canvas = tk.Canvas(root, width=700, height=700, bd=0, highlightthickness=0)  # 设置画布
imgpath = r'S:\Desktop\素材\1.png'  # 图片绝对路径
img = Image.open(imgpath)  # 打开图片
photo = ImageTk.PhotoImage(img)
canvas.create_image(350, 350, image=photo)  # 图片位置 (0,0)点为图片中心
canvas.pack()

# 指定字体名称、大小、样式
Ft_Jet = tkFont.Font(family='JetBrains Mono', size=20, weight=tkFont.BOLD)
Ft_Kai = tkFont.Font(family='楷体', size=20, weight=tkFont.BOLD)  # 楷体加粗

# 组件
entry1 = tk.Entry(root, insertbackground='blue', highlightthickness=2)
entry1.pack()
canvas.create_window(350, 10, width=150, height=25, window=entry1)
btn1 = tk.Button(root, text='搜索', font=Ft_Kai, command=lambda: thread_it(Search,entry1.get()))
btn1.pack()
canvas.create_window(350, 40, width=100, height=40, window=btn1)

root.mainloop()
