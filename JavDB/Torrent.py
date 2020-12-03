import requests
import pymysql
from bs4 import BeautifulSoup
import os
import threading

'''
获得某个作品的所有种子和所有预览图
'''
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)
glock = threading.Lock()
table_sql = {'有码': 'actors', '无码': 'uncensored', '欧美': 'western'}


def JudgeDownloadAll(kind, name, id, pic: list):  # 判断是否下载所有章节
    root = "D:/JavDB/Preview/{}/{}/{}/".format(kind, name, id)  # 下载路径
    sum = 0
    for i in pic:
        path = root + i.split('/')[-1]
        if os.path.exists(path):
            sum += 1
    if sum == len(pic):
        return True


def download_pic(id, pic: list, name, kind):  # 下载预览图
    root = "D:/JavDB/Preview/{}/{}/{}/".format(kind, name, id)  # 保存的路径
    while True:
        # glock.acquire()
        if JudgeDownloadAll(kind, name, id, pic) is True:
            # glock.release()
            break
        else:
            for img in pic:
                # glock.release()
                path1 = root + img.split('/')[-1]  # 预览图路径
                print(path1)
                try:
                    if not os.path.exists(root):  # 判断文件夹是否存在
                        os.makedirs(root)  # 创建多级目录
                    if not os.path.exists(path1):  # 判断图片是否存在
                        read = requests.get(img)
                        with open(path1, "wb")as f:
                            f.write(read.content)
                            f.close()
                            print("文件保存成功！")
                    else:
                        pass
                except:
                    print("文件爬取失败！")


def w_torrent_txt(id, torrentlist: list, title, capacitylist: list, name, kind):  # 将种子写入txt
    root = "D:/JavDB/Preview/{}/{}/{}/".format(kind, name, id)  # 保存的路径
    path2 = root + id + '-种子.txt'
    file = open(path2, 'w')
    file.write(title + '\n')
    sum = 1
    for i, j in zip(torrentlist, capacitylist):
        file.write('链接' + str(sum) + ':\n')
        file.write(i + '\n')
        file.write('种子大小：' + j + '\n')
        sum += 1
    file.close()


def thread_down(id, pic: list, name, kind):  # 多线程下载
    for i in range(3):
        thread1 = threading.Thread(target=download_pic, args=(id, pic, name, kind))
        thread1.start()


def Main_Down(url: list, uid: list, name, kind):  # 爬取主函数
    for u, idd in zip(url, uid):
        html = requests.get(u).text
        soup = BeautifulSoup(html, "html.parser")
        try:
            pre_pic = soup.find('div', class_='tile-images preview-images').find_all('a', class_='tile-item')  # 预览图
            td = soup.find_all('td', class_='magnet-name')  # td标签下所有种子
            title = soup.find('h2', class_='title is-4').find('strong').text  # 片名

            pic = []  # 图片列表
            for i in pre_pic:
                pic.append(i['href'])
            thread_down(idd, pic, name, kind)

            torrentlist = []  # 种子列表
            capacitylist = []  # 视频大小列表
            for i in td:
                torrent = i.find('a')
                torrentlist.append(torrent['href'])  # 获得a标签下的种子链接
                capacity = i.find('span', class_='meta')  # 获得span标签下的视频大小
                # replace去除所有多余元素
                a = capacity.text.replace(' ', '')
                a = a.replace('\n\xa0', '')
                a = a.replace('\n', '')
                capacitylist.append(a)
            w_torrent_txt(idd, torrentlist, title, capacitylist, name, kind)
        except:
            print("%s无可下载磁力" % idd)
            print("%s无预览图" % idd)


def Fetch_name(kind, page):
    cursor1 = conn.cursor()
    sql = 'select 名字 from {}'.format(kind)
    cursor1.execute(sql)
    data = cursor1.fetchall()
    Actor_name = []
    sum = 1
    for i in range(page * 50):
        Actor_name.append(data[i][0])
    for x in Actor_name:
        print('(%d)%s' % (sum, x))
        sum += 1
    return Actor_name


def Fetch_ID(name):  # 抓取所有番号
    cursor = conn.cursor()
    name = name.replace(' ', '')
    sql = 'select UID,URL from {}'.format(name)
    cursor.execute(sql)  # 执行sql语句
    fid = cursor.fetchall()  # 抓取到的所有数据
    uid = []  # 番号
    for i in range(len(fid)):
        uid.append(fid[i][0])
    return uid


def Fetch_URL(name):  # 抓取所有番号地址
    cursor = conn.cursor()
    name = name.replace(' ', '')
    sql = 'select UID,URL from {}'.format(name)
    cursor.execute(sql)  # 执行sql语句
    fid = cursor.fetchall()  # 抓取到的所有数据
    url = []  # 地址
    for i in range(len(fid)):
        url.append(fid[i][1])
    return url


if __name__ == '__main__':
    print("输入类型：", end='')
    kind = input()
    print('输入需要查看的页数：', end='')
    page = int(input())
    a_list = Fetch_name(table_sql[kind], page)
    s = 1
    a_dict = {}
    for x in a_list:
        a_dict.setdefault(s, x)
        s += 1
    print('输入你选择的序号：', end='')
    choose = int(input())
    print('您选择的是：' + a_list[choose-1])
    Main_Down(Fetch_URL(a_dict[choose]), Fetch_ID(a_dict[choose]), a_dict[choose], kind)
