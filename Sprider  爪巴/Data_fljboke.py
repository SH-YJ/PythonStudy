from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import re


def getUrl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return "连接失败！"


if __name__ == '__main__':
    option = Options()
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    browser.get('https://1flj.fun/')
    all_page = browser.find_element_by_id('primary')
    for i in range(3):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 拖拽
        browser.find_element_by_id('pagination').click()
        time.sleep(5)
        i += 1


    url = all_page.find_elements_by_xpath('.//div[@class="post-thumb"]/a')
    for i in range(len(url)):
        url[i] = url[i].get_attribute('href')
    title = all_page.find_elements_by_xpath('.//a[@class="post-title"]/h3')  # 标题名
    for i in range(len(title)):
        title[i] = title[i].get_attribute('textContent')
    print(title)
    browser.close()
    list1 = []  # 所有下载地址
    list2 = []
    for x,y in zip(url, title):
        if x == 'https://1flj.fun/archives/595':
            down_url = ' '
            jieya_url = ' '
        else:
            html = getUrl(x)
            down_url = re.findall('<a style=".*?" href=".*?" target=".*?" rel=".*?">(.*?)</a>', html)
            jieya_url = re.findall('<a style=".*?" href="(.*?)" target=".*?" rel=".*?">.*?</a>', html)
        list1.append(down_url[0])
        list2.append(jieya_url[0])
    print(list2)
