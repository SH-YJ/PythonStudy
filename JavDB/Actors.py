from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymysql
import os
import requests

'''
获得所有演员的名字，作品地址，头像
'''
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)
baseurl1 = 'https://javdb6.com/actors?page={}'  # 有码地址
baseurl2 = 'https://javdb6.com/actors/uncensored?page={}'  # 无码地址
baseurl3 = 'https://javdb6.com/actors/western?page={}'  # 欧美地址
baseurl = {'有码': baseurl1, '无码': baseurl2, '欧美': baseurl3}
table_sql = {'有码': 'actors', '无码': 'uncensored', '欧美': 'western'}


def download_pic(name, img, page, kind):  # 保存演员头像
    root = "D:/JavDB/Actors/{}/P{}/".format(kind, page)  # 保存的路径
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


def Main_Down(kurl, page, kind, tablename):
    option = Options()
    option.add_argument('--headless')  # 无界面模式
    browser = webdriver.Chrome(options=option)
    browser.get(kurl.format(page))
    browser.find_elements_by_xpath('.//div[@class="modal-card"]/footer/a')[0].click()  # 点击已承诺
    url = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a')  # 所有作品的地址
    name = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/strong')  # 演员名字
    pic = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/figure/span')  # 演员头像

    cursor = conn.cursor()
    sql = "insert into {}(名字, 地址) value(%s, %s)".format(tablename)

    namelist = []  # 名称
    for i in range(len(name)):
        url[i] = url[i].get_attribute('href')  # 获取作品地址
        name[i] = name[i].text  # 演员名字
        pic[i] = pic[i].get_attribute('style')  # 演员头像
        namelist.append(name[i])
        cursor.execute(sql, [name[i], url[i]])  # 执行sql语句
        conn.commit()  # 提交到数据执行

    picturelist = []  # 头像
    for i in pic:
        p = str(i)  # 将列表元素转为字符串
        # replace 去除所有不必要元素
        pp = p.replace('background-image: url("', '')
        pp = pp.replace('");', '')
        picturelist.append(pp)

    for x, y in zip(namelist, picturelist):
        download_pic(x, y, page, kind)
    browser.close()


if __name__ == '__main__':
    print("输入类型：", end='')
    kind = input()
    print('输入页数：', end='')
    page = input()
    Main_Down(baseurl[kind], page, kind, table_sql[kind])
