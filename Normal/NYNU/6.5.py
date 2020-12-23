if __name__ == '__main__':
    a, b, c = input().split()
    An = 0
    Bn = 0
    Cn = 0
    for i in range(1, int(a) + 1):
        An += i
    for i in range(1, int(b) + 1):
        Bn += i * i
    for i in range(1, int(c) + 1):
        Cn += 1 / i
    print('%.2f' % (An + Bn + Cn))
