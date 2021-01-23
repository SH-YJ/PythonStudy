import os

title = 'D:/BaiduNetdiskDownload/070/'
if __name__ == '__main__':
    all70 = os.listdir(title)

    for i in all70:
        every = os.listdir(title + i)  # 每个系列的内容
        for j in every:
            filename = os.listdir(title + i+'/' + j + '/')
            sp = 1
            pic = 1
            for file in filename:
                try:
                    if file.endswith('mp4') is True:
                        os.renames(title + i + '/'+ j + '/' + file,
                                   title + i + '/'+ j + '/视频' + str(sp) + '.mp4')
                        sp = sp + 1
                    else:
                        if file == 'flj..one看小姐姐福利.jpg':
                            os.renames(title + i + '/'+ j + '/' + file,
                                       title + i + '/'+ j + '/封面.jpg')
                        else:
                            os.renames(title + i + '/'+ j + '/' + file,
                                       title + i + '/'+ j + '/' + str(pic) + '.jpg')
                            pic = pic + 1
                except:
                    print('出错')
