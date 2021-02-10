import urllib.parse as parse
from selenium import webdriver
import time
import urllib.request
import os
import sys


def Time_1():  # 进度条函数
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('{0}% |{1}'.format(int(i % 51) * 2, int(i % 51) * '■'))
        sys.stdout.flush()
        time.sleep(0.125)
    sys.stdout.write('\n')


def Music_search():
    print('-----------------------网易云----------------------------')
    url = 'https://music.163.com/#/search/m/?%s&type=1' % (parse.urlencode({'s': input('请输入歌曲名称：')}))

    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    page = driver.find_element_by_id('m-search')
    song_id_list = page.find_elements_by_xpath('.//div[@class="sn"]/div[@class="text"]/a')  # 得到所有歌曲的音频和视频
    song_name_list = page.find_elements_by_xpath('.//div[@class="sn"]/div[@class="text"]/a/b')
    song_id_list_1 = []  # 所有歌曲的音频

    for i in range(len(song_id_list)):
        song_id_list[i] = song_id_list[i].get_attribute('href')
        if 'song' in song_id_list[i]:
            song_id_list_1.append(song_id_list[i])

    for i in range(len(song_name_list)):
        song_name_list[i] = song_name_list[i].get_attribute('title')

    driver.close()
    return song_name_list, song_id_list_1  # 返回歌曲名称、歌曲id


def Downlad(music_name, url_1):
    id = url_1[url_1.find('id='):]
    url = 'https://music.163.com/song/media/outer/url?{}.mp3'.format(id)
    try:
        os.mkdir(path='./网易云下载')
    except Exception as e:
        print(e, '但不要紧，程序仍然继续执行！')
    finally:
        print('{}.mp3正在下载当中！请等待一下...'.format(music_name))
        Time_1()
        urllib.request.urlretrieve(url=url, filename='./网易云下载/{}.mp3'.format(music_name))
        print('{}.mp3已经下载完毕！'.format(music_name))
        print('请到当前文件夹下面查看！')


if __name__ == '__main__':
    list_1 = Music_search()
    print('符合要求的音乐如下：')
    for i in range(len(list_1[0])):
        print('-{}-{}'.format(i + 1, list_1[0][i]))
    i = int(input('请输入你想下载的音乐序号：'))
    Downlad(list_1[0][i - 1], list_1[1][i - 1])
