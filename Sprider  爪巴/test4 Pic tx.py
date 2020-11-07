import requests
from bs4 import BeautifulSoup
import re
import urllib.request


def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


if __name__ == "__main__":
    html_url = getUrl('https://www.woyaogexing.com/touxiang/nan/index.html')
    soups = BeautifulSoup(html_url, "html.parser")
    all_url = re.findall('<a href="(.*?)" class="img" target=".*?">', html_url)
    for url in all_url:
        I_url = 'https://www.woyaogexing.com/' + url
        II_url = getUrl(I_url)
        soup = BeautifulSoup(II_url, "html.parser")
        all_img = soup.find('ul', class_='artCont cl').find_all('img')
        for img in all_img:
            src = img['src']
            img_url = 'https:' + src
            print(img_url)
            urllib.request.urlretrieve(img_url, 'S:/Nan/' + img_url.split('/')[-1])
            print('下载完成')
