from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import os
import requests

'''
获得自己账号收藏的所有演员名字，作品地址，头像
'''
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)
baseurl = 'https://javdb6.com'
# 抓包对比登陆前后的cookie变化，将变化部分写入cookie1中
cookie1 = {'name': '_jdb_session',
           'value': 'IufnzenCPwSTkGTebmRcN2PY4tbrqmlwXIpfE0GvuDGgRh8eAIBjDJuFeaTRSiOGO6lE2hcGtR%2BF1NR9B72t9%2FCrlSoyZ%2BTgG7FvrDeIO06vwxAowdqnXQAn43RtjRR4QJ7Ix5qsfW4xiS4JIxmTjqzI9Ui6w2wZbrettrcXfQ0FLmZeOaCzyK6J3MJHzXkxO4cvtK8vLo8jR2DnXFJRW3MEugCjojOlaSWTEmoCBTXEr4H%2FCjvPhkrf9a%2FnFSu%2Bjodgqz5zXcMfERzw%2FyYSyINaKcfUZUqbAKZShfDko2yahC7j1Ydv318h8sXtLLsh7L0C08WjZKvRBbXDHOLR5UtB--5PyYjHGjwjZaUxzZ--ThewbR%2FGV5FOkQL39Xdrvw%3D%3D'}


def download_pic(name, img):  # 保存演员头像
    root = "D:/JavDB/Actors/收藏/"  # 保存的路径
    path = root + name + '.jpg'  # 图片的文件名
    print(path)
    try:
        if not os.path.exists(root):  # 判断文件夹是否存在
            os.makedirs(root)
        if not os.path.exists(path):  # 判断图片是否存在
            read = requests.get(img)
            with open(path, "wb")as f:
                f.write(read.content)
                f.close()
                print("文件保存成功！")
        else:
            print("文件已存在！")
    except:
        print("文件爬取失败！")


def Main_Down():
    option = Options()
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    browser.get(baseurl)
    browser.find_elements_by_xpath('.//div[@class="modal-card"]/footer/a')[0].click()  # 点击已承诺
    browser.add_cookie(cookie1)  # 添加cookie直接跳过登录
    browser.refresh()  # 刷新界面后，直接登录
    browser.find_element_by_xpath(
        './/div[@class="navbar-item has-dropdown is-hoverable"]/a[@href="/users/profile"]').click()  # 进入用户界面
    browser.find_element_by_xpath('.//ul[@class="menu-list"]/li/a[@href="/users/collection_actors"]').click()  # 点击收藏的演员
    pic = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/figure/span')  # 收藏演员的头像
    url = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a')  # 收藏演员的作品地址
    name = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/strong')  # 收藏演员的名字

    cursor = conn.cursor()
    sql = "insert into actors_collection(名字, 地址) value(%s, %s)"

    namelist = []  # 名称
    for i in range(len(name)):
        name[i] = name[i].text  # 演员名字
        pic[i] = pic[i].get_attribute('style')  # 演员头像
        namelist.append(name[i])

    urllist = []  # 地址
    for i in range(0, len(url), 2):
        url[i] = url[i].get_attribute('href')  # 获取作品地址
        urllist.append(url[i])

    for x, y in zip(namelist, urllist):  # 写入数据库
        cursor.execute(sql, [x, y])
        conn.commit()

    picturelist = []  # 头像
    for i in pic:
        p = str(i)  # 将列表元素转为字符串
        # replace 去除所有不必要元素
        pp = p.replace('background-image: url("', '')
        pp = pp.replace('");', '')
        picturelist.append(pp)

    for x, y in zip(namelist, picturelist):
        download_pic(x, y)


def Clear():  # 把表清空，只要更新一次，就会导致插入大量重复数据
    cursor = conn.cursor()
    sql = 'truncate table actors_collection'
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    print('请问是否需要清表（若收藏更新，建议清表！）Y/N？')
    choose = input()
    if choose == 'Y' or choose == 'y':
        Clear()
    Main_Down()