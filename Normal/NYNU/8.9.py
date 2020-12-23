def statistics(str1):
    enlish, num, space, other = 0, 0, 0, 0
    for s in str1:
        if s >= 'A' and s <= 'Z' or s >= 'a' and s <= 'z':
            enlish += 1
        elif s >= '1' and s <= '9':
            num += 1
        elif s == ' ':
            space += 1
        else:
            other += 1
    print(enlish,num,space,other)


if __name__ == '__main__':
    str1 = input()
    statistics(str1)
