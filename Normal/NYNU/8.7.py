def copy(str1):
    list = ['a','e','i','o','u']
    for s in str1:
        if s in list:
            print(s,end='')

if __name__ == '__main__':
    str1 = input()
    copy(str1)