if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(1,n+1):
        list.append(i)
    for i in range(len(list)):
        list[i] = int(list[i])
    out_peo = 0
    k = 0
    j = 0
    while out_peo < n - 1:
        if list[j] != 0:
            k += 1
        if k == 3:
            list[j] = 0
            out_peo += 1
            k = 0
        j += 1
        if j == n:
            j = 0
    for i in list:
        if i != 0:
            print(i)