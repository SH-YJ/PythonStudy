def func(x):
    if x < 1:
        y = x
    elif x >= 1 and x < 10:
        y = 2 * x - 1
    else:
        y = 3 * x - 11
    return y


if __name__ == '__main__':
    x = int(input())
    print(func(x))