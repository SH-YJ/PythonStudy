if __name__ == '__main__':
    str = input()  # python的字符串不支持修改，要修改将字符串转list
    line = list(str)
    for i in range(0, len(line)):
        if line[i] >= 'a' and line[i] < 'Z' or line[i] >= 'A' and line[i] < 'z':
            line[i] = chr(ord(line[i]) + 1)
        elif line[i] == 'z':
            line[i] = 'a'
        elif line[i] == 'Z':
            line[i] = 'A'
        else:
            line[i] = line[i]
    str = ''.join(line)  # 将list转为字符串
    print(str)