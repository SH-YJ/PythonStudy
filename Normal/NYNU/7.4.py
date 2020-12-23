if __name__ == '__main__':
    line = input().split(' ')
    insertnum = input()
    line.append(insertnum)
    for i in range(0, len(line)):
        line[i] = int(line[i])
    line.sort()
    for i in line:
        print(i)
