import docx
import requests
import re
from bs4 import BeautifulSoup

Title = {
    '1': 'http://www.wulewala.com/article/list/4',
    '2': 'http://www.wulewala.com/article/list/3',
    '3': 'http://www.wulewala.com/article/list/5',
    '4': 'http://www.wulewala.com/article/list/7'
}


def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


def GetDetailPara(url):  # 获得详细页面内容并保存
    html = getUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    para = soup.find('div', class_='body').find_all('p')  # 获取标题内容
    title = soup.find('div', class_='title').find('a')  # 获取标题
    name = title.text
    doc = docx.Document()
    for p in para:
        pa = p.text
        doc.add_paragraph(pa)
    doc.save(name + ".docx")


def GetTitleUrl(url):  # 获得标题目录
    html = getUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    title = re.findall('<a target="_blank" href=".*?">(.*?)</a>', html)
    URL = re.findall('<a target="_blank" href="(.*?)">.*?</a>', html)
    detailedURL = []
    i = 1
    for uu in URL:
        detailedURL.append("http://www.wulewala.com" + uu)
    print("------获得的目录内容------")
    for t in title:
        print("{0}：{1}".format(i, t))
        i += 1
    choose = input("请输入你的选择：")


if __name__ == '__main__':
    sole_title = ['伦理故事', '夫妻之间', '那年那人', '秘密日记']
    j = 1
    for i in range(0, 4, 1):
        print("{0}：{1}".format(j, sole_title[i]))
        j += 1
    key = input("请输入要爬取的内容：")
    if key == '1':
        GetTitleUrl(Title[key])
    elif key == '2':
        GetTitleUrl(Title[key])
    elif key == '3':
        GetTitleUrl(Title[key])
    elif key == '4':
        GetTitleUrl(Title[key])
