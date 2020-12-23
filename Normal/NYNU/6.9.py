if __name__ == '__main__':
    m, n = input().split()
    s, h = 0, int(m)
    for i in range(1, int(n) + 1):
        s += h + h / 2
        h = h / 2
    s = s - h
    print('{:.2f} {:.2f}'.format(h, s))
