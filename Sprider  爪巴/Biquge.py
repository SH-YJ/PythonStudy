import re
import requests
import threading
from docx.oxml.ns import qn
from docx.shared import Pt
import docx
import os
from bs4 import BeautifulSoup
import time


def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


def Search(searchkey):  # 搜索结果
    baseurl = "http://www.biquge.info/modules/article/search.php?searchkey="
    html = getUrl(baseurl + searchkey)
    articleName = re.findall('<a href="/[0-9]{1,}_[0-9]{2,}/">(.*?)</a>', html)  # 文字名称
    author = re.findall('<td class="odd">([\u4E00-\u9FA5]+)</td>', html)  # 作者名称
    latestChapter = re.findall('<a href="/[0-9]{1,}_[0-9]{2,}/[0-9]+.html" target="_blank">(.*?)</a>', html)  # 最新章节
    internetSite = re.findall('<a href="(/[0-9]{1,}_[0-9]{2,}/)">.*?</a>', html)  # 具体网址
    print("搜索结果如下:")
    Url = {}
    Article = {}
    i = 1
    for a, b, c, d in zip(articleName, author, internetSite, latestChapter):
        print('({num}).《{name:<{len}}\t作者：{auth:<{len}}\t最新章节：{chapter}'.format(num=i, name=a + '》', auth=b, chapter=d,
                                                                                len=22 - len(a.encode('GBK')) + len(a)))
        Url.setdefault(i, "http://www.biquge.info/" + c)
        Article.setdefault(i, a)
        i += 1
    print("请输入要下载的小说序号：", end='')
    choose = int(input())
    for x in range(1, len(Url), 1):
        if x == choose:
            print("你选择的是《" + Article[x] + "》")
            GetDetailPage(Url[x], Article[x])


def GetDetailPage(url, articlename):
    time.sleep(1)
    html = getUrl(url)
    everyChapterName = re.findall('<a href="[0-9]+.html" title=".*?">(.*?)</a>', html)  # 每一章节的名称
    Url = re.findall('<a href="([0-9]+.html)" title=".*?">.*?</a>', html)  # 每一章节的网址
    everyChapterUrl = []
    for URL in Url:
        everyChapterUrl.append(url + URL)
    for x, y in zip(everyChapterUrl,everyChapterName):
        Download(x, articlename, y)


def Download(url, articlename, chaptername):
    time.sleep(1)
    new_html = getUrl(url)
    html = new_html.replace('<br/>', ' ')
    soup = BeautifulSoup(html, "lxml")
    content = soup.find('div', id='content')
    root = "D:/BaiduNetdiskDownload/Biquge/" + articlename + '/'
    path = root + chaptername + '.docx'
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        doc = docx.Document()
        # 设置字体
        doc.styles['Normal'].font.name = u'楷体'
        doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'楷体')
        doc.styles['Normal'].font.size = Pt(12)
        for p in content.text.split(' '):
            doc.add_paragraph(p)
        doc.save(path)
        print("章节" + chaptername + " 下载完成")
    else:
        print("文件已存在")
    return True


def Main_Download(chapterurl: list, articlename, chaptername: list):
    while True:
        if len(chapterurl) == 0:
            break
        href = chapterurl.pop()
        name = chaptername.pop()
        try:
            if Download(href, articlename, name):
                print('线程{}正在下载章节{}'.format(threading.current_thread().getName(), name))
        except Exception as e:
            print(e)


def multithreading(chapterurl, articlename, chaptername):
    threading_1 = []
    for i in range(10):
        threading1 = threading.Thread(target=Main_Download, args=(chapterurl, articlename, chaptername,))
        threading1.start()
        threading_1.append(threading1)
    for t in threading_1:
        t.join()
    print('当前线程为{}'.format(threading.current_thread().getName()))


if __name__ == '__main__':
    print("请输入搜索关键字：", end='')
    searchkey = input()
    Search(searchkey)
