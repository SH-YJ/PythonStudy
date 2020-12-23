if __name__ == '__main__':
    pi = 3.14
    r, h = input().split()
    r = float(r)
    h = float(h)
    C1 = 2 * pi * r
    Sa = r * r * pi
    Sb = 4 * pi * r * r
    Va = 4 * pi * r * r * r / 3
    Vb = r * r * h * pi
    print('C1={:.2f}\nSa={:.2f}\nSb={:.2f}\nVa={:.2f}\nVb={:.2f}\n'.format(C1, Sa, Sb, Va, Vb),end='')
