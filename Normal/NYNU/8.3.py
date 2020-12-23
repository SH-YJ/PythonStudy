def prime(n):
    if n == 1:
        return 'not prime'
    elif n == 2 or n == 3:
        return 'prime'
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return 'not prime'
            elif i == n // 2:
                return 'prime'


if __name__ == '__main__':
    n = int(input())
    print(prime(n))
