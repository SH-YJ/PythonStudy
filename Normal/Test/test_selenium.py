# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 设置无头模式
# option = Options()
# option.add_argument('--headless')

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
data = browser.page_source
print(data)
input = browser.find_element_by_id('kw').send_keys('python')
btn = browser.find_element_by_id('su').click()


browser.maximize_window()  # 界面最大化
# 网页截屏  此时此刻是存在于百度首页  默认是只截屏一部分
browser.save_screenshot('baidu.png')

# browser.close()