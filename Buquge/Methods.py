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
        Url.setdefault(i, "http://www.biquge.info/" + c)  # 将网址与数字加入Url字典
        Article.setdefault(i, a)  # 将文章名与数字加入Article字典
        i += 1
    print("请输入要下载的小说序号：", end='')
    choose = int(input())
    for x in range(1, len(Url), 1):
        if x == choose:
            print("你选择的是《" + Article[x] + "》")
            GetDetailPage(Url[x], Article[x])


def GetDetailPage(url, articlename):  # 获得选择的小说的详细界面内容
    time.sleep(1)
    html = getUrl(url)
    everyChapterName = re.findall('<a href="[0-9]+.html" title=".*?">(.*?)</a>', html)  # 每一章节的名称
    Url = re.findall('<a href="([0-9]+.html)" title=".*?">.*?</a>', html)  # 每一章节的网址
    everyChapterUrl = []
    lenth = len(everyChapterName)
    for URL in Url:
        everyChapterUrl.append(url + URL)
    count = 1
    ReeveryChapterName = []
    for a in everyChapterName:
        t = a
        li = ['<', '>', '/', '\\', ':', '?', '*']  # Windows中文件名不允许的字符
        if JudgeSpecialChar(a) is True:
            for b in li:
                t = t.replace(b, '')
        ReeveryChapterName.append(t)
    for x, y in zip(everyChapterUrl, ReeveryChapterName):
        multithreading(x, articlename, y, lenth, count)
        count += 1


def Download(url, articlename, chaptername):  # 下载每一章内容
    time.sleep(1)
    new_html = getUrl(url)
    html = new_html.replace('<br/>', ' ')  # 替换获得源码的<br/>标签
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find('div', id='content')
    root = "D:/BaiduNetdiskDownload/Biquge/" + articlename + '/'  # 文件夹路径
    path = root + chaptername + '.docx'  # 文件保存路径
    try:
        if not os.path.exists(root):  # 若文件夹不存在，则创建
            os.mkdir(root)
        if not os.path.exists(path):
            doc = docx.Document()
            # 设置字体
            doc.styles['Normal'].font.name = u'楷体'
            doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'楷体')
            doc.styles['Normal'].font.size = Pt(15)  # 设置字体大小
            # 初号=42磅 小初=36磅 一号=26磅 小一=24磅 二号=22磅 小二=18磅 三号=16磅 小三=15磅 四号=14磅 小四=12磅 五号=10.5磅 小五=9磅 六号=7.5磅 小六=6.5磅 七号=5.5磅 八号=5磅
            for p in content.text.split(' '):
                doc.add_paragraph(p)
            doc.save(path)  # 文件保存
        else:
            print("文件已存在")
        return True  # 方便判断是否下载完成
    except Exception as e:
        pass


def Main_Download(chapterurl, articlename, chaptername, length, count):
    while JudgeDownloadAll(chaptername, articlename) is False:  # 当前章节未下载时，进入循环，直至下载完成
        try:
            if Download(chapterurl, articlename, chaptername):
                percent = count / length * 100  # 小说下载进度
                print('正在下载章节{0} 进度{1:.2f}%'.format(chaptername, percent))
                count += 1
                break
        except Exception as e:
            pass


def multithreading(chapterurl, articlename, chaptername, length, count):  # 多线程下载
    threading_1 = []
    for i in range(1):
        threading1 = threading.Thread(target=Main_Download, args=(chapterurl, articlename, chaptername, length, count,))
        threading1.start()
        threading_1.append(threading1)
    for t in threading_1:
        t.join()


def JudgeDownloadAll(chaptername, articlename):  # 判断是否下载所有章节
    root = "D:/BaiduNetdiskDownload/Biquge/" + articlename + '/'
    docname = root + chaptername + ".docx"
    if os.path.exists(docname):
        return True
    if not os.path.exists(docname):
        return False


def JudgeSpecialChar(text):  # 判断章节名的特殊字符
    pattern = ("[^a-zA-Z0-9_\u4e00-\u9fa5]+")
    a = re.search(pattern, text)
    if a is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    print("请输入搜索关键字：", end='')
    starttime = time.time()
    searchkey = input()
    Search(searchkey)
    endtime = time.time()
    print('下载完成，总耗时:%.f秒' % (endtime - starttime))
