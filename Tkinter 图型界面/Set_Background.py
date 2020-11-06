import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont


def C_Gui():
    root = tk.Tk()
    root.resizable(0, 0)  # 设置窗口大小不可变

    # 指定字体名称、大小、样式
    Ft_Jet = tkFont.Font(family='JetBrains Mono', size=20, weight=tkFont.BOLD)

    # 背景
    canvas = tk.Canvas(root, width=700, height=700, bd=0, highlightthickness=0)  # 设置画布大小  bd=文本框边框宽度
    # 只支持gif格式图片,不清楚
    imgpath = r'S:\Desktop\素材\1.png'  # 图片绝对路径
    # imgpath = '5f3757be38934.gif'  当前文件夹下相对路径
    img = Image.open(imgpath)
    photo = ImageTk.PhotoImage(img)

    canvas.create_image(350, 350, image=photo)  # 图片位置 (0,0)点为图片中心
    canvas.pack()
    # 显示entry
    entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
    entry.pack()

    btn = tk.Button(root, text='Click', font=Ft_Jet, fg='#53c49e')
    btn.pack()

    canvas.create_window(50, 10, width=100, height=20, window=entry)
    canvas.create_window(200, 20, width=200, height=40, window=btn)

    root.mainloop()

C_Gui()