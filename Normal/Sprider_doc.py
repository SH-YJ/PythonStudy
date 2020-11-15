import docx
import requests
import re
from bs4 import BeautifulSoup
import os
from docx.oxml.ns import qn

Title = {
    '1': 'http://www.wulewala.com/article/list/4/',
    '2': 'http://www.wulewala.com/article/list/3/',
    '3': 'http://www.wulewala.com/article/list/5/',
    '4': 'http://www.wulewala.com/article/list/7/'
}
sole_title = ['伦理故事', '夫妻之间', '那年那人', '秘密日记']
sum_page = [4, 3, 2, 4]


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
    root = "S:/Word/" + name + ".docx"
    if not os.path.exists(root):
        doc = docx.Document()
        # 设置字体
        doc.styles['Normal'].font.name = u'楷体'
        doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'楷体')
        for p in para:
            pa = p.text
            doc.add_paragraph(pa)
        doc.save(root)
        print(name + ".docx下载完成.")
    else:
        print("文件已存在")


def GetTitleUrl(url, page):  # 获得标题目录
    html = getUrl(url + page)
    soup = BeautifulSoup(html, "html.parser")
    title = re.findall('<a target="_blank" href=".*?">(.*?)</a>', html)
    URL = re.findall('<a target="_blank" href="(.*?)">.*?</a>', html)
    detailedURL = []
    num_URL = {}
    i = 1
    for uu in URL:
        detailedURL.append("http://www.wulewala.com" + uu)
    for x in range(0, len(detailedURL), 1):
        num_URL.setdefault(x + 1, detailedURL[x])
    print("------获得的目录内容------")
    for t in title:
        print("{0}：{1}".format(i, t))
        i += 1
    print("{0}:返回上一级界面\n{1}:退出".format(len(detailedURL) + 1, len(detailedURL) + 2))
    while True:
        choose = int(input("-----请输入你的选择："))
        if choose == len(detailedURL) + 1:
            mainInterface()
        elif choose == len(detailedURL) + 2:
            exit()
        else:
            GetDetailPara(num_URL[choose])


def mainInterface():
    j = 1
    for i in range(0, 4, 1):
        print("{0}：{1} ({2}页)".format(j, sole_title[i], sum_page[i]))
        j += 1
    print("5：退出")
    key = input("请输入要爬取的内容：")
    if key == '5':
        exit()
    page = input("请输入要爬取内容的页数：")
    if key == '1':
        GetTitleUrl(Title[key], page)
    elif key == '2':
        GetTitleUrl(Title[key], page)
    elif key == '3':
        GetTitleUrl(Title[key], page)
    elif key == '4':
        GetTitleUrl(Title[key], page)


if __name__ == '__main__':
    mainInterface()
