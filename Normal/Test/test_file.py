import os

if __name__ == '__main__':
    file =  open('test.txt','w',encoding='utf-8')  # 设置编码格式utf-8
    file.write('测试\ntest')
    file.close()

