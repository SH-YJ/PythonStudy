if __name__ == '__main__':
    a = 2
    count = 1
    Sn = 0
    Tn = 0
    n = int(input())
    while count <= n:
        Tn += a
        Sn += Tn
        a = a*10
        count += 1
    print(Sn)