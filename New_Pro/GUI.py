import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
import Methods

root = tk.Tk()
root.resizable(0, 0)  # 设置窗口大小不可变
root.iconbitmap('S:\\Desktop\\py文件\\Tkinter 图型界面\\5f4226701e4e0.128px.ico')

# Set_Background():
canvas = tk.Canvas(root, width=700, height=700, bd=0, highlightthickness=0)  # 设置画布
imgpath = r'S:\Desktop\素材\1.png'  # 图片绝对路径
# imgpath = '1.png'  当前文件夹下相对路径
img = Image.open(imgpath)  # 打开图片
photo = ImageTk.PhotoImage(img)
canvas.create_image(350, 350, image=photo)  # 图片位置 (0,0)点为图片中心
canvas.pack()

# 指定字体名称、大小、样式
Ft_Jet = tkFont.Font(family='JetBrains Mono', size=20, weight=tkFont.BOLD)

# 组件
entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
entry.pack()
canvas.create_window(50, 10, width=100, height=20, window=entry)
button = tk.Button(root, text='Click', font=Ft_Jet, command=Methods.pri)
button.pack()
canvas.create_window(50, 40, width=100, height=40, window=button)

root.mainloop()
