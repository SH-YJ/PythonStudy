if __name__ == '__main__':
    string = input()
    space = 0
    enlish = 0
    num = 0
    other = 0
    for i in string:
        if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z':
            enlish += 1
        elif i >= '1' and i <= '9':
            num += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    print(enlish, num, space, other)
