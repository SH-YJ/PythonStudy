def fac(n):
    if n < 0:
        f = -1
    elif n == 0 or n == 1:
        f = 1
    else:
        f = fac(n - 1) * n
    return f


if __name__ == '__main__':
    n = int(input())
    Sn = 0
    for i in range(1, n+1):
        Sn += fac((i))
    print(Sn)
