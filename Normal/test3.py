import pygame
import time
from os import environ
import tkinter as tk
import threading


def play_music():
    filepath = r"l0qtb-zz95z.mp3"
    pygame.mixer.init()
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    # 加载音乐
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(start=0.0, )  # 开始播放
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    time.sleep(300)
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()  # 暂停


def unpause():
    pygame.mixer.music.unpause()  # 取消暂停


def thread_it(func, *args):  # 开线程防止卡死
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


win = tk.Tk()
win.title("Music")
win.geometry("400x400")
win.iconbitmap('5f38e8f147726.64px.ico')

b1 = tk.Button(win, text="start", command=lambda: thread_it(play_music)).pack()
b2 = tk.Button(win, text="pause", command=lambda: thread_it(pause)).pack()
b3 = tk.Button(win, text="unpause", command=lambda: thread_it(unpause)).pack()

win.mainloop()
