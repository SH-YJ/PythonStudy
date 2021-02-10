import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def geturl(url):
    try:
        read = requests.get(url)  # 获取url
        read.raise_for_status()  # 状态响应 返回200连接成功
        read.encoding = read.apparent_encoding  # 从内容中分析出响应内容编码方式
        return read.text  # Http响应内容的字符串，即url对应的页面内容
    except:
        return '连接失败！'


if __name__ == '__main__':
    html = geturl(
        'https://mp.weixin.qq.com/s?__biz=MzIyNjU2NzIxNQ==&mid=2247505111&idx=1&sn=091454dde57184bf78fbe827705fdf29&chksm=e86ce197df1b6881748e772d2e7809673b66983012d048b59ec5ff3d6b145f1703569e271bf6&mpshare=1&scene=23&srcid=0202wnswcfYoEy9Ya5mkbiUh&sharer_sharetime=1612260041527&sharer_shareid=d081e720b4231c9d5b6d95a384e657fc')
    Url = re.findall('<span style=".*?">(.*?)</span>', html)
    while '' in Url:
        Url.remove('')  # 移除空元素
    name = []
    url = []
    for i, j in zip(range(66, len(Url), 2), range(67, len(Url) + 1, 2)):
        try:
            name.append(Url[i])
            url.append(Url[j])
        except IndexError:
            pass
    source = []
    baseurl = 'https://render.alipay.com/p/c/17yq18lq3slc?source='
    for i in url:
        appname = re.findall('([A-Z]+_[A-Z]+)', i)
        source.append(baseurl + appname[0])
    for n, u in zip(name, source):
        option = Options()
        option.add_argument('--headless')
        browser = webdriver.Chrome()
        browser.get(u)
        print('进入 ' + n + ' 界面')
        browser.find_elements_by_xpath('.//a[@role="button"]')[0].click()
        browser.find_elements_by_id('J-mobile')[0].send_keys('13362345914')  # 输入手机号
        time.sleep(30)
        browser.find_elements_by_xpath('.//span[@role="button"]')[0].click()  # 发送验证码
        time.sleep(1)
        print('验证码发送成功！')
        time.sleep(2)
        print('输入验证码：', end='')
        code = input()
        browser.find_elements_by_id('J-code')[0].send_keys(code)
        time.sleep(2)
        browser.find_elements_by_xpath('.//a[@data-aspm-click="c63625.d131135"]')[0].click()  # 领取按钮
        print('领取成功，请等待3秒~~~')
        time.sleep(3)
        browser.quit()
