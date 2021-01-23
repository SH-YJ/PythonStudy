from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('http://47.93.252.151/acm-rank')
    time.sleep(5)
    tr = browser.find_element_by_xpath('.//preceding-sibling::tr[@class="ivu-table-row"]')
    t = tr.find_element_by_xpath('.//preceding-sibling::td/')
    print(t.text)