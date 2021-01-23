from tkinter import *

strtoname = {'A': '福', 'B': '水', 'C': '窦', 'D': '章', 'E': '云', 'F': '苏', 'G': '潘', 'H': '葛', 'I': '奚', 'J': '范',
             'K': '彭',
             'L': '郎',
             'M': '鲁', 'N': '韦', 'O': '昌', 'P': '马', 'Q': '苗', 'R': '凤', 'S': '花', 'T': '方', 'U': '俞', 'V': '任',
             'W': '袁',
             'X': '柳',
             'Y': '唐', 'Z': '罗', 'a': '褚', 'b': '卫', 'c': '蒋', 'd': '沈', 'e': '韩', 'f': '杨', 'g': '朱', 'h': '秦',
             'i': '尤',
             'j': '许',
             'k': '何', 'l': '吕', 'm': '施', 'n': '张', 'o': '孔', 'p': '曹', 'q': '严', 'r': '华', 's': '金', 't': '魏',
             'u': '陶',
             'v': '姜',
             'w': '戚', 'x': '谢', 'y': '邹', 'z': '喻', '0': '赵', '1': '钱', '2': '孙', '3': '李', '4': '周', '5': '吴',
             '6': '郑',
             '7': '王',
             '8': '冯', '9': '陈', '#': '顾', '%': '尹', '&': '江', '*': '钟', '-': '伍', '=': '贝', '+': '米', '_': '余',
             '/': '姚',
             '.': '薛',
             '?': '孟'}
nametostr = dict((map(reversed, strtoname.items())))  # 反转字典
title = 'magnet:?xt=urn:btih:'


# magnet:?xt=urn:btih:2CAB88301CF13C843DEB07B7CF50E81F03299948
# 孙窦福水冯冯李赵钱窦苏钱李窦冯周李章云水赵王水王窦苏吴赵云冯钱苏赵李孙陈陈陈周冯

def change_to_name(str1):
    magnet = str1[20:]
    namelist = ''
    for i in magnet:
        namelist = namelist + strtoname[i]
    return namelist


def change_to_str(allname: str):
    print(title, end='')
    for i in allname:
        print(nametostr[i], end='')


if __name__ == '__main__':
    root = Tk()
    root.title('百家姓')
    root.geometry('500x500')
    entry1 = Entry(root, width=60)
    entry1.pack()
    btn1 = Button(root, text='百家姓->', width=10, command=lambda: change_to_name(str(entry1.get()))).pack()
    txt1 = StringVar()
    entry2 = Entry(root, width=60, textvariable=txt1)
    root.mainloop()
