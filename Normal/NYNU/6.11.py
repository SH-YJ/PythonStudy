def sqrt(x):
    i = x
    while i * i - x > 1e-5:
        i = 0.5 * (i + x / i)
    return i


if __name__ == '__main__':
    x = float(input())
    print('%.3f' % sqrt(x))
