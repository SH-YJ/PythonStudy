if __name__ == '__main__':
    str = input()
    list = []
    for i in str:
        list.append(i)
    list.reverse()
    for i in list:
        print(i,end='')