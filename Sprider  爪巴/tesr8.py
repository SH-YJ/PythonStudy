import requests
from bs4 import BeautifulSoup
import os
import re

# 获取网址
def getUrl(url):
    try:
        read = requests.get(url)  #获取url
        read.raise_for_status()   #状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
        return read.text   #Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"

if __name__ == '__main__':
    html = getUrl('https://www.youtube.com/')
    print(html)