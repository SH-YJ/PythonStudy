import requests
from bs4 import BeautifulSoup
import pypinyin  # 拼音

baseurl = 'https://{}.8684.cn/'  # {}内为城市名拼音


def getUrl(url):
    try:
        read = requests.get(url)
        read.raise_for_status()
        read.encoding = read.apparent_encoding
        return read.text
    except:
        return '连接失败！'


if __name__ == '__main__':
    print('请输入城市名称：', end='')
    cityname = input()
    pycityname = pypinyin.slug(cityname, separator='')  # 中文转拼音
    perfecturl = baseurl.format(pycityname)  # 输入后完整的地址
    html = getUrl(perfecturl)
    soup = BeautifulSoup(html, "html.parser")
    ll = soup.find_all('div', class_='list')[2].find_all('a')  # 线路分类
    line = []
    d_url = []
    for i in ll:
        line.append(i.text)  # 分类名称
        d_url.append(perfecturl + i['href'])  # 分类地址
    print('线路分类：')
    for i in range(0, len(line)):
        print('({}).{}'.format(i + 1, line[i]))
    dict1 = {}
    y = 1
    for x in d_url:
        dict1.setdefault(y,x)
        y += 1
    print('输入你的选择：',end='')
    choose = int(input())
    html1 = getUrl(dict1[choose])
    soup1 = BeautifulSoup(html1, 'html.parser')
    d_ll = soup1.find('div',class_='list clearfix').find_all('a')
    d_line = []  # 具体线路名称
    d_line_url = []  # 具体线路网址
    for i in d_ll:
        d_line.append(i.text)
        d_line_url.append(perfecturl + i['href'])
    for x,y in zip(d_line_url, d_line):
        html2 =getUrl(x)
        soup2 = BeautifulSoup(html2, 'html.parser')
        station = soup2.find('div',class_='bus-lzlist mb15').find_all('li')
        stationname = ''
        for j in range(len(station)):
            if j != len(station)-1:
                stationname += station[j].text + ' --> '
            else:
                stationname += station[j].text
        print(y)  # 线路名字
        print(stationname)  # 站台名称



