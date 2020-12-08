import pymysql
import requests
import datetime
import threading
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import random

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)


def create(table):
    cursor = conn.cursor()
    create_sql = "create table {}" \
                 "(" \
                 "id int unsigned not null auto_increment primary key," \
                 "UID varchar(255) not null," \
                 "URL varchar(255) not null" \
                 ");"
    cursor.execute(create_sql.format(table))
    conn.commit()


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


def download_video(url):
    path = 'D:/BaiduNetdiskDownload/信条.mp4'
    time.sleep(1)
    r = requests.get(url, headers=None, stream=True, timeout=30)
    r.close()
    time.sleep(10)
    # print(r.status_code, r.headers)
    headers = {}
    all_thread = 1
    # 获取视频大小
    file_size = int(r.headers['content-length'])
    # 如果获取到文件大小，创建一个和需要下载文件一样大小的文件
    if file_size:
        fp = open(path, 'wb')
        fp.truncate(file_size)
        print('视频大小：' + str(int(file_size / 1024 / 1024)) + "MB")
        fp.close()
    # 每个线程每次下载大小为5M
    size = 5242880
    # 当前文件大小需大于5M
    if file_size > size:
        # 获取总线程数
        all_thread = int(file_size / size)
        # 设最大线程数为10，如总线程数大于10
        # 线程数为10
        if all_thread > 10:
            all_thread = 10
    part = file_size // all_thread
    threads = []
    starttime = datetime.datetime.now().replace(microsecond=0)
    for i in range(all_thread):
        # 获取每个线程开始时的文件位置
        start = part * i
        # 获取每个文件结束位置
        if i == all_thread - 1:
            end = file_size
        else:
            end = start + part
        if i > 0:
            start += 1
        headers = headers.copy()
        headers['Range'] = "bytes=%s-%s" % (start, end)
        t = threading.Thread(target=Handler, name='th-' + str(i),
                             kwargs={'start': start, 'end': end, 'url': url, 'filename': path, 'headers': headers})
        t.setDaemon(True)
        threads.append(t)
    # 线程开始
    for t in threads:
        time.sleep(0.2)
        t.start()
    # 等待所有线程结束
    for t in threads:
        t.join()
    endtime = datetime.datetime.now().replace(microsecond=0)
    print('用时：%s' % (endtime - starttime))


if __name__ == '__main__':
    url = 'https://v.tongwangjs.com/api/videoplay/28a5d5edbefb6c9e30d2643fdd1ccc7ee8b6216d.mp4?sign=3e27f939a10464aa567037a311b34745-time=1607250205-user=wanmeikk'
    download_video(url)
