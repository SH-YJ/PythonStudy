if __name__ == '__main__':
    n = int(input())
    a, b, c, sn = 1, 1, 0, 0
    for i in range(1, n + 1):
        c = a+b
        sn += c/a
        b = a
        a = c
    print('%.2f'%sn)