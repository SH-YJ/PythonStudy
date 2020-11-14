from tkinter import *
from tkinter.ttk import *

root = Tk()
# 进度条控件的mode参数有两个值，"indeterminate"表示来回反弹样式，"determinate"表示步进样式
progress1 = Progressbar(root, mode='indeterminate', length=100)
# 可拉伸
progress1.pack(side='left', expand=1, fill="both")
# 需要start函数去启动进度条
progress1.start()
progress2 = Progressbar(root, mode='determinate', length=100)
progress2.pack(side=LEFT, expand=1, fill="both")
progress2.start()

root.mainloop()
