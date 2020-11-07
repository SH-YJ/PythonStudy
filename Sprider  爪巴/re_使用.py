import re
import requests
from urllib import request
import time
import os

# url

# 模拟浏览器请求资源
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
}

url = requests.get('https://www.taotuxp.com/xinggan')
html = url.text
print(html)

# dir_name = re.findall('<h1>(.*?)</h1>', html)[-1]
'''
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
'''
urls = re.findall('<a href="" class=".*?">', html)
print(urls)
'''
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = 'https://www.vmgirls.com/'+ requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
'''
