# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 设置无头模式
option = Options()
option.add_argument('--headless')

browser = webdriver.Chrome(options=option)
browser.get('https://www.baidu.com/')
data =  browser.page_source
print(type(data))

browser.maximize_window()  # 界面最大化
# 网页截屏  此时此刻是存在于百度首页  默认是只截屏一部分
# browser.save_screenshot('baidu_.png')
browser.close()