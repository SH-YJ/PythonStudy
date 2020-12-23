if __name__ == '__main__':
    list = input().split()
    for i in range(0, len(list)):
        list[i] = int(list[i])
    list.sort()
    for i in list:
        print(i)
