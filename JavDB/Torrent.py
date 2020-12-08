import requests
import pymysql
from bs4 import BeautifulSoup
import os
import threading
import time

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
table_sql = {'有码': 'actors', '无码': 'uncensored', '欧美': 'western', '演员月榜': 'actors_month','收藏':'actors_collection'}


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


def write_torrent(id, torrentlist: list, title, capacitylist: list, name, kind, duration):  # 将种子写入txt
    root = "D:/JavDB/Preview/{}/{}/{}/".format(kind, name, id)  # 保存的路径
    path2 = root + id + '-种子.txt'
    while True:
        if not os.path.exists(root):
            os.makedirs(root)
        # 不判断文件文件是否存在，以便后续更新
        file = open(path2, 'w', encoding='utf-8')  # 设置编码格式utf-8,防止有的种子出现非gbk字符，而报错，导致无法写入全部
        file.write(title + '\n')
        file.write('影片时长：' + duration + '\n')
        sum = 1
        for i, j in zip(torrentlist, capacitylist):
            file.write('链接' + str(sum) + ':\n')
            file.write(i + '\n')
            file.write('种子大小：' + j + '\n')
            sum += 1
        file.close()
        print(id + '-种子写入成功！')
        break


def download_video(kind, name, id, url):  # 多线程下载预告片
    root = "D:/JavDB/Preview/{}/{}/{}/".format(kind, name, id)  # 下载路径
    path = root + id + '.mp4'  # 以番号命名的视频文件
    if not os.path.exists(path):
        read = requests.get(url, headers=None, stream=True, timeout=30)
        time.sleep(0.5)
        headers = {}
        all_thread = 1
        file_size = int(read.headers['content-length'])  # 视频文件大小
        # 如果获得视频大小，创建一个需要下载文件一样大小的文件
        if file_size:
            f = open(path, 'wb')
            f.truncate(file_size)
            print(id + '-预告片大小：' + str(int(file_size / 1024 / 1024)) + "MB")
            f.close()

        size = 5242880  # 每个线程每次下载大小
        if file_size > size:
            all_thread = int(file_size / size)  # 线程数量
            if all_thread > 10:
                all_thread = 10  # 最大线程数为10
        part = file_size // all_thread  # 分成多个部分
        threads = []
        for i in range(all_thread):
            start = part * i  # 每个线程文件开始的位置
            if i == all_thread - 1:
                end = file_size
            else:
                end = start + part
            if i > 0:
                start += 1
            headers = headers.copy()
            headers['Range'] = "byte=%s-%s" % (start, end)
            t = threading.Thread(target=Handler, name='th-' + str(i),
                                 kwargs={'start': start, 'end': end, 'url': url, 'filename': path, 'headers': headers})
            t.setDaemon(True)
            threads.append(t)

        for t in threads:
            time.sleep(0.5)
            t.start()
        for t in threads:
            t.join()

        print(id + '-预告片下载完成！')
    else:
        print(id + '-预告片已存在！')


def Handler(start, end, url, filename, headers=None):
    if headers is None:
        headers = {}
    tt_name = threading.current_thread().getName()
    print(tt_name + ' is begin')
    r = requests.get(url, headers=headers, stream=True)
    total_size = end - start
    downsize = 0
    startTime = time.time()
    with open(filename, 'r+b') as fp:
        fp.seek(start)
        var = fp.tell()
        for chunk in r.iter_content(204800):
            if chunk:
                fp.write(chunk)
                downsize += len(chunk)
                line = tt_name + '-downloading %d KB/s - %.2f MB， 共 %.2f MB'
                line = line % (
                    downsize / 1024 / (time.time() - startTime), downsize / 1024 / 1024,
                    total_size / 1024 / 1024)
                print(line, end='\r')


def thread_down(id, pic: list, name, kind):  # 多线程下载
    for i in range(3):
        thread1 = threading.Thread(target=download_pic, args=(id, pic, name, kind))
        thread1.start()


def Main_Down(url: list, uid: list, name, kind):  # 爬取主函数
    for u, idd in zip(url, uid):
        html = requests.get(u, timeout=500).text
        soup = BeautifulSoup(html, "html.parser")
        time.sleep(1)
        # 处理没有预览图的异常
        try:
            pre_pic = soup.find('div', class_='tile-images preview-images').find_all('a', class_='tile-item')  # 预览图

            pic = []  # 图片列表
            for i in pre_pic:
                pic.append(i['href'])
            thread_down(idd, pic, name, kind)  # 下载预览图
        except:
            print(idd + '-无预览图！')
        # 处理没有种子的异常
        try:
            video = soup.find('video', id='preview-video')  # video标签

            video_souce = 'https:' + video.find('source')['src']  # 视频地址
            download_video(kind, name, idd, video_souce)  # 下载预告片
        except:
            print(idd + '-无预告片！')
        # 处理没有种子的异常
        try:
            td = soup.find_all('td', class_='magnet-name')  # td标签下所有种子
            title = soup.find('h2', class_='title is-4').find('strong').text  # 片名
            nav = soup.find('nav', class_='panel video-panel-info').find_all('div', class_='panel-block')[2]  # nav标签
            duration = nav.find('span').text  # 影片时长

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
            # 若文本文件中只有名称，表示当前没有种子
            write_torrent(idd, torrentlist, title, capacitylist, name, kind, duration)  # 将种子写入txt
        except:
            print(idd + '-无可下载种子！')


def Fetch_name(kind, page):
    cursor1 = conn.cursor()
    sql = 'select 名字 from {}'.format(kind)
    cursor1.execute(sql)
    data = cursor1.fetchall()
    Actor_name = []
    sum = 1
    try:
        for i in range((page - 1) * 50, page * 51):
            Actor_name.append(data[i][0])
    except:
        pass
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
    print('您选择的是：' + a_list[choose - 1])
    Main_Down(Fetch_URL(a_dict[choose]), Fetch_ID(a_dict[choose]), a_dict[choose], kind)
