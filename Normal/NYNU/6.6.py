if __name__ == '__main__':
    for i in range(100, 1000):
        hundred = i // 100
        ten = (i - hundred * 100) // 10
        single = i - hundred * 100 - ten * 10
        s = hundred * hundred * hundred + ten * ten * ten + single * single * single
        if s == i:
            print(i)
