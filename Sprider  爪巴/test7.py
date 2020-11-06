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
    for i in range(2,200):
        html_url = getUrl('http://pic.netbian.com/4kfengjing/index_'+ str(i) +'.html')
        soup =BeautifulSoup(html_url,"html.parser")
        img_urls = soup.find('ul',class_='clearfix').find_all('a')#获取图片所在网址
        for img_url in img_urls:
            img = "http://pic.netbian.com" + img_url['href']
            html_url2 = getUrl(img)
            soup2 = BeautifulSoup(html_url2,"html.parser")
            i_img_url = soup2.find('div',class_='photo-pic').find('img')#获取图片具体地址
            ii_img = 'http://pic.netbian.com' + str(i_img_url['src'])
            root = "S:/4K/"  # 保存的路径
            path = root + ii_img.split('/')[-1]  # 获取img的文件名
            print(path)
            try:
                if not os.path.exists(root):  # 判断是否存在文件并下载img
                    os.mkdir(root)
                if not os.path.exists(path):
                    read = requests.get(ii_img)
                    with open(path, "wb")as f:
                        f.write(read.content)
                        f.close()
                        print("文件保存成功！")
                else:
                    print("文件已存在！")
            except:
                print("文件爬取失败！")

