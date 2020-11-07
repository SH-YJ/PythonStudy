# -- coding:UTF-8 --
import requests
from bs4 import BeautifulSoup
import os
import re
import openpyxl

'''
思路：获取网址
      获取图片地址
      爬取图片并保存
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'
}


# 获取网址
def getUrl(url):
    try:
        read = requests.get(url, headers=headers)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


if __name__ == '__main__':
    for i in range(2, 15):
        html_url = getUrl('http://www.obzhi.com/category/fengjingbizhi/page/' + str(i))
        soup = BeautifulSoup(html_url, "html.parser")
        url = soup.find('ul', class_='masonry clearfix').find_all('a', class_='zoom')  # 获取所有图片所在网页
        for u in url:
            u_url = u['href']
            html_url2 = getUrl(u_url)
            soup2 = BeautifulSoup(html_url2, "html.parser")
            img_url = soup2.find('img', class_='alignnone')  # 获取具体图片地址
            img = img_url['src']
            root = "S:/Pic/"  # 保存的路径
            path = root + img.split('/')[-1]  # 获取img的文件名
            print(path)
            try:
                if not os.path.exists(root):  # 判断是否存在文件并下载img
                    os.mkdir(root)
                if not os.path.exists(path):
                    read = requests.get(img)
                    with open(path, "wb")as f:
                        f.write(read.content)
                        f.close()
                        print("文件保存成功！")
                else:
                    print("文件已存在！")
            except:
                print("文件爬取失败！")
