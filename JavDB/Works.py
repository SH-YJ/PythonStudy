import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

'''
获得某个演员的所有单体作品的地址以及封面图
'''
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)
table_sql = {'有码': 'actors', '无码': 'uncensored', '欧美': 'western', '演员月榜': 'actors_month', '收藏': 'actors_collection'}
# 每一个类型的作品的class不一样需要用字典对应
work_dict = {'有码': '', '无码': ' horz-cover', '欧美': ' horz-cover', '演员月榜': '', '收藏': ''}
id_dict = {'有码': 'uid', '无码': 'uid', '欧美': 'video-title2', '演员月榜': 'uid', '收藏': 'uid'}


def download_pic(id, img, name, kind):  # 下载封面图
    root = "D:/JavDB/FrontCover/{}/{}/".format(kind, name)  # 保存的路径
    path = root + id + '.jpg'  # 获取img的文件名
    print(path)
    try:
        if not os.path.exists(root):  # 判断是否存在文件并下载img
            os.makedirs(root)  # 创建多级目录
        if not os.path.exists(path):
            read = requests.get(img)
            with open(path, "wb")as f:
                f.write(read.content)
                f.close()
                print("文件保存成功！")
        else:
            print("文件已存在！")
    except:
        print("文件爬取失败！")


def Main_Down(tablename, url, kind, ad, ac):  # 主下载函数
    option = Options()
    option.add_argument('--headless')  # 无界面模式
    browser = webdriver.Chrome(options=option)
    browser.get(url)  # 具体演员界面
    browser.find_elements_by_xpath('.//div[@class="modal-card"]/footer/a')[0].click()  # 点击已承诺
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 拖拽至底部
    time.sleep(20)
    id = browser.find_elements_by_xpath('.//div/a/div[@class="{}"]'.format(ad))  # 番号
    works = browser.find_elements_by_xpath('.//div[@class="grid-item column{}"]/a'.format(ac))  # 所有单体作品地址
    imgs = browser.find_elements_by_xpath('.//div[@class="grid-item column{}"]/a/div/img'.format(ac))  # 封面图
    try:
        for i in range(len(imgs)):
            id[i] = id[i].text.replace(' ', '')  # 替换欧美名的空格，sql不能有空格
            imgs[i] = imgs[i].get_attribute('data-src')
            download_pic(id[i], imgs[i], tablename, kind)
    except:
        print("无封面照!")
    print("下一页加载中~~~~~~")

    cursor = conn.cursor()
    sql = "insert into {}(UID, URL) value(%s, %s)".format(tablename)
    for i in range(len(works)):
        works[i] = works[i].get_attribute('href')  # 所有作品的地址
        print('数据写入中~~~~~~')
        cursor.execute(sql, [id[i], works[i]])
        conn.commit()
    browser.close()


def Fetch_name(kind, page):  # 抓取所有演员名字
    cursor1 = conn.cursor()
    sql = 'select 名字 from {}'.format(kind)
    cursor1.execute(sql)
    data = cursor1.fetchall()
    Actor_name = []
    sum = 1
    for i in range((page - 1) * 50, page * 51):
        try:
            Actor_name.append(data[i][0])
        except:
            pass
    for x in Actor_name:
        print('(%d)%s' % (sum, x))
        sum += 1
    return Actor_name


def Fetch_url(kind, page):  # 抓取演员详情地址
    cursor1 = conn.cursor()
    sql = 'select 地址 from {}'.format(kind)
    cursor1.execute(sql)
    data = cursor1.fetchall()
    Url_list = []
    for i in range((page - 1) * 50, page * 51):  # 每次只展示50或小宇50个演员
        try:  # 最后演员少于50时，会报错，所以使用try
            Url_list.append(data[i][0] + '?page={}&t=s')
        except:
            pass
    return Url_list


def Create(table):  # 创建单个演员作品表
    cursor = conn.cursor()
    table = table.replace(' ', '-')  # 去空格，欧美名有空格会导致创表失败
    create_sql = "create table {}" \
                 "(" \
                 "id int unsigned not null auto_increment primary key," \
                 "UID varchar(255) not null," \
                 "URL varchar(255) not null" \
                 ");"
    cursor.execute(create_sql.format(table))
    conn.commit()


def Clear(tablename):  # 把表清空，只要更新一次，就会导致插入大量重复数据
    cursor = conn.cursor()
    sql = 'truncate table {}'.format(tablename)
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    print("输入类型：", end='')
    kind = input()
    print('输入需要查看的页数：', end='')
    page = int(input())
    a_list = Fetch_name(table_sql[kind], page)
    u_list = Fetch_url(table_sql[kind], page)
    u_dict = {}
    a_dict = {}
    s = 1
    for x, y in zip(u_list, a_list):
        u_dict.setdefault(s, x)
        a_dict.setdefault(s, y)
        s += 1
    print('输入你选择的序号：', end='')
    choose = int(input())
    print('您选择的是：' + a_list[choose - 1])
    try:
        Create(a_dict[choose])
    except:
        print("表已经存在")
    finally:
        print('请问是否需要清空表（若是二次写入，建议清表，会有大量重复数据写入！）Y/N？')
        judge = input()
        if judge == 'Y' or judge == 'y':
            Clear(a_dict[choose])
            print('表已经清空！')
        for i in range(1, 30):
            Main_Down(a_dict[choose].replace(' ', ''), u_dict[choose].format(i), kind, id_dict[kind], work_dict[kind])
