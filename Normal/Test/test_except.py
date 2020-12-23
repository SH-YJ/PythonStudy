import traceback

if __name__ == '__main__':
    try:
        l1 = {1, 2, 4}
        print(l1[9])
    except Exception as e:
        file = open('aa.txt', 'w', encoding='utf-8')
        traceback.print_exc(file=file)  # 将异常写入文件中
