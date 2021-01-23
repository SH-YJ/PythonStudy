if __name__ == '__main__':
    n = int(input())
    line = input().split(' ')
    m = int(input())
    for i in range(0,m):
        print(line[n-m+i],end=' ')
    for i in range(0,n-m):
        print(line[i],end=' ')