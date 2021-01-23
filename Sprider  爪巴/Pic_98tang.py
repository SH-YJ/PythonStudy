from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
import threading

baseurl = 'https://www.qwewqrtetrretr.xyz/forum-48-{}.html'


def thread_down(img, title):  # 多线程下载
    for i in range(1):
        thread1 = threading.Thread(target=download_pic, args=(img, title))
        thread1.start()


def download_pic(img, title):
    root = "D:/98tang/亚洲/{}/".format(title)  # 保存的路径
    path = root + img.split('/')[-1]  # 预览图路径
    print(path)
    try:
        if not os.path.exists(root):  # 判断文件夹是否存在
            os.makedirs(root)  # 创建多级目录
        if not os.path.exists(path):  # 判断图片是否存在
            read = requests.get(img)
            with open(path, "wb")as f:
                f.write(read.content)
                f.close()
                print("文件保存成功！")
        else:
            pass
    except:
        print("文件爬取失败！")


def mainDown():
    for y in range(1, 10):
        option = Options()
        option.add_argument('--headless')
        browser = webdriver.Chrome(options=option)
        browser.get(baseurl.format(y))
        tbody = browser.find_elements_by_xpath('.//preceding-sibling::tbody/tr/td/a')
        for i in range(14, len(tbody), 2):
            tbody[i] = tbody[i].get_attribute('href')
            browser1 = webdriver.Chrome(options=option)
            browser1.get(tbody[i])
            file = browser1.find_elements_by_xpath(
                './/preceding-sibling::ignore_js_op/dl/dd/div[@class="mbn savephotop"]/img')
            title = browser1.find_element_by_xpath('.//h1[@class="ts"]/span')
            for x in range(len(file)):
                file[x] = file[x].get_attribute('file')
            for i in file:
                thread_down(i, title.text)


if __name__ == '__main__':
    mainDown()