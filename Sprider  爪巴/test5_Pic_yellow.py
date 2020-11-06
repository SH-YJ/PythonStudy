import requests
import re
from bs4 import BeautifulSoup
import os

# 获取网址
def getUrl(url):
    try:
        read = requests.get(url)  #获取url
        read.raise_for_status()   #状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  #从内容中分析出响应内容编码方式
        return read.text   #Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"

if __name__ == "__main__":
    for page in range(2,29):
        html_url =getUrl("https://www.bpx5.com/meinv/list-%E7%BE%8E%E5%AA%9B%E9%A6%86%E6%96%B0%E5%88%8A-"+str(page)+".html")
        all_url =re.findall('<a href="(.*?)" title=".*?" target=".*?">',html_url)
        title ='https://www.bpx5.com'
        for urls in all_url:
            src =title + urls   #单个网页地址
            html_urls = getUrl(src)
            soup = BeautifulSoup(html_urls, "html.parser")
            all_img = soup.find('div',class_='content').find_all('img')
            for img in all_img:
                img_src = img['data-original']
                print(img_src)
                dir_name = img['title']
                root = "E:/Pic2/" + dir_name + '/'  # 保存的路径
                path = root + img_src.split('/')[-1]  # 获取img的文件名
                print(path)
                try:
                    if not os.path.exists(root):  # 判断是否存在文件并下载img
                        os.mkdir(root)
                    if not os.path.exists(path):
                        read = requests.get(img_src)
                        with open(path, "wb")as f:
                            f.write(read.content)
                            f.close()
                            print("文件保存成功！")
                    else:
                        print("文件已存在！")
                except:
                    print("文件爬取失败！")