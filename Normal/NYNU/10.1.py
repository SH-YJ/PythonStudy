def swap(list1: list):
    small, big, s, b = list1[0], list1[0], 0, 0
    for i in range(0, len(list1)):
        if list1[i] >= big:
            big = list1[i]
            b = i
    t = list1[b]
    list1[b] = list1[0]
    list1[0] = t
    for i in range(0, len(list1)):
        if list1[i] <= small:
            small = list1[i]
            s = i
    t = list1[s]
    list1[s] = list1[9]
    list1[9] = t


def getnum():
    line = input().split()
    for i in range(len(line)):
        line[i] = int(line[i])
    return line


def out(line: list):
    for i in line:
        print(i, end=' ')


if __name__ == '__main__':
    line = getnum()
    swap(line)
    out(line)
