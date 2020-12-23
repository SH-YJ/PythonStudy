def num4(number):
    s = 0
    for n in number:
        s += 1
        if s != 4:
            print(int(n), end=' ')
        else:
            print(int(n),end='')


if __name__ == '__main__':
    num = input()
    num4(num)
