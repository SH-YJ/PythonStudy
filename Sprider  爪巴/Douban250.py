import urllib.error
import urllib.request
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}


def getUrl(url):
    request = urllib.request.Request(url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        return html
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            return e.code
        if hasattr(e, 'reason'):
            return e.reason


if __name__ == '__main__':
    html = getUrl("https://movie.douban.com/top250?start=0")
    Ch_movie_name = re.findall('<span class="title">([\u4E00-\u9FA5]+)</span>', html)  # 获得中文名
    Score = re.findall('<span class="rating_num" property="v:average">(.*?)</span>', html)
    d = {}
    for i, j in zip(Ch_movie_name, Score):
        xx = {i: j}
        d.update(xx)
    print(d)
