if __name__ == '__main__':
    str = input()
    print(len(str))
    list = []
    for i in range(len(str)):
        if i != len(str) - 1:
            print(str[i],end=' ')
        else:
            print(str[i])
        list.append(str[i])
    list.reverse()
    for i in list:
        print(i,end='')
