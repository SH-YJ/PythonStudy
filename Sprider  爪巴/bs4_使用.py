# -- coding:UTF-8 --
import requests
from bs4 import BeautifulSoup
import os
import re


# 获取网址
def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


while True:
    page = 1
    name1 = input("shuru:")
    html_url = getUrl("https://www.taotuxp.com/" + str(name1))
    # dir_name = re.findall('<a href=".*?">(.*?)</a>', html_url)
    # print(dir_name)
    soup = BeautifulSoup(html_url, "html.parser")
    # 通过分析网页内容，查找img的统一父类及属性
    all_page = soup.find('ul', class_='menu').find_all('a')  # img为图片的标签
    print(all_page.string)
