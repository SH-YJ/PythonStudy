import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import pymysql

'''
获得演员月榜的所有演员
'''
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='syj',
    passwd='syj21408',
    database='javdb',
    charset='utf8'
)
baseurl = 'https://javdb6.com/rankings/actor_monthly'  # 演员月榜地址


def download_pic(name, img):  # 保存演员头像
    root = "D:/JavDB/Actors/{}/".format('月榜演员')  # 保存的路径
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
    option.add_argument('--headless')  # 无界面模式
    browser = webdriver.Chrome(options=option)
    browser.get(baseurl)
    browser.find_elements_by_xpath('.//div[@class="modal-card"]/footer/a')[0].click()  # 点击已承诺
    url = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a')  # 所有作品的地址
    name = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/strong')  # 演员名字
    pic = browser.find_elements_by_xpath('.//div[@class="box actor-box"]/a/figure/span')  # 演员头像

    cursor = conn.cursor()
    sql = "insert into actors_month(名字, 地址) value(%s, %s)"

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
        download_pic(x, y)
    browser.close()


def Clear():  # 把表清空，只要更新一次，就会导致插入大量重复数据
    cursor = conn.cursor()
    sql = 'truncate table actors_month'
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    print('请问是否需要清表（若月榜更新，建议清表！）Y/N？')
    choose = input()
    if choose == 'Y' or choose == 'y':
        Clear()
    Main_Down()
