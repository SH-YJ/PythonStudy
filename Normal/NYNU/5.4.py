def max(a, b, c):
    if a < b:
        m = b
    else:
        m = a
    if m < c:
        m = c
    return m


if __name__ == '__main__':
    a,b,c = input().split()
    print(max(int(a), int(b), int(c)),end='')