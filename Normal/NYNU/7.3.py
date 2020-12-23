if __name__ == '__main__':
    list = []
    list1 = []
    for i in range(0,3):
        list = input().split(' ')
        list1.append(list)
    sum1 = int(list1[0][0]) + int(list1[1][1]) + int(list1[2][2])
    sum2 = int(list1[2][0]) + int(list1[1][1]) + int(list1[0][2])
    print(sum1,sum2)
