import requests
from bs4 import BeautifulSoup
import re
import math
import os

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'
}


def getUrl(url):
    try:
        read = requests.get(url, headers=headers)  # 获取url
        read.raise_for_status()   # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text   # Http响应内容的字符串，即url对应的页面内容
    except :
        return "连接失败！"


def get_sum_page(t_url):  # 获取当前页总数
    try:
        t_html = getUrl(t_url)
        t_soup = BeautifulSoup(t_html,"html.parser")
        t_sum_pic = t_soup.find('div', id='dinfo').find_all('span')
        for t_s in t_sum_pic:
            t_ss = t_s.string[0] + t_s.string[1]
            t_sum_page = int(t_ss) / 3
            t_real_sum_page = math.ceil(t_sum_page)
        return t_real_sum_page
    except:
        return "访问失败！"


def download_img(x_root,x_src,x_path): # 以二进制下载图片
    try:
        if not os.path.exists(x_root):  # 判断是否存在文件并下载img
            os.mkdir(x_root)
        if not os.path.exists(x_path):
            read = requests.get(x_src,allow_redirects=False)
            with open(x_path, "wb")as f:
                f.write(read.content)
                f.close()
                print("文件保存成功！")
        else:
            print("文件已存在！")
    except :
        print("文件爬取失败！")


if __name__ == '__main__':
    html = getUrl("https://www.nvshens.org/gallery/meiguo/")
    soup = BeautifulSoup(html,"html.parser")
    urls = soup.find('div',class_='listdiv').find_all('a',class_='galleryli_link')
    for url in urls:
        i_url = "https://www.nvshens.org"+url['href']
        html3 = getUrl(i_url)
        soup3 = BeautifulSoup(html3,"html.parser")
        dir_name = re.findall('<title>(.*?)</title>',html3)[-1]
        print(dir_name)
        for i in range(1,get_sum_page(i_url)+1,1):
            i_i_url = i_url +str(i)+".html"
            html2 = getUrl(i_i_url)
            soup2 = BeautifulSoup(html2,"html.parser")
            img = soup2.find('div',class_='gallery_wrapper').find_all('img')
            for x_img in img:
                i_img = x_img['src']
                print(i_img)
                root = "S:/XiuRen/" + dir_name + '/'  # 保存的路径
                path = root + i_img.split('/')[-1]  # 获取img的文件名
                download_img(root, i_img, path)