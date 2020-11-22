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
    os.system('cls')
    S_page = input("输入第几页:")
    a_html_url = getUrl("https://www.taotuxp.com/xinggan/page/" + str(S_page))
    sum_url = re.findall('<a href="(.*?)" class=".*?" target=".*?">', a_html_url)  # 获取一网页12个网址
    for s_url in sum_url:
        html_urls = getUrl(s_url)
        soups = BeautifulSoup(html_urls, "html.parser")
        pagelist = soups.find('div', class_='pagelist').find_all('a')  # 获取当前网页总页数
        sum_page = int(pagelist[-1].string) + 1
        for page in range(1, int(sum_page)):  # 页数爬取
            html_url = getUrl(s_url + '/' + str(page))
            dir_name = re.findall('<h1>(.*?)</h1>', html_url)[-1]  # 获取标题名
            soup = BeautifulSoup(html_url, "html.parser")
            # 通过分析网页内容，查找img的统一父类及属性
            all_img = soup.find('div', class_='context').find_all('img')  # img为图片的标签
            for img in all_img:
                src = img['src']  # 获取img标签里的src内容
                img_url = src
                print(img_url)
                root = "S:/Pic/" + dir_name + '/'  # 保存的路径
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
