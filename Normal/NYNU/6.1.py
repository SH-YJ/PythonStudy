def gcd(x, y):
    m = max(x, y)
    n = min(x, y)
    while m % n:
        m, n = n, m % n
    return n


def lcm(x, y):
    m = max(x, y)
    n = min(x, y)
    while m % n:
        m, n = n, m % n
    return x * y // n


if __name__ == '__main__':
    x, y = input().split()
    print(gcd(int(x),int(y)),lcm(int(x),int(y)))