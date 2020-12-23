def change(l1: list):
    for i in range(0,3):
        for j in range(i,3):
            t = l1[i][j]
            l1[i][j] = l1[j][i]
            l1[j][i] = t


if __name__ == '__main__':
    list = []
    list1 = []
    for i in range(0,3):
        list1 = input().split(' ')
        list.append(list1)
    change(list)
    s = 0
    for i in range(0,3):
        for j in range(0,3):
            print(list[i][j],end=' ')
            s += 1
            if s % 3 == 0:
                print()