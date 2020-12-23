if __name__ == '__main__':
    n = int(input())
    for i in range(2, n +1):
        if i == 2:
            print(i)
        if i % 2 != 0:
            sum = 0
            for j in range(2, i):
                if i % j == 0:
                    sum += 1
            if sum == 0:
                print(i)
