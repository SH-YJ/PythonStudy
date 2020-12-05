import random
import string

if __name__ == '__main__':
    print(random.random())  # 随机生成0-1的浮点数
    print(random.randint(1, 10))  # 随机生成1-10的整数
    print(random.uniform(1.1, 5.4))  # 随机生成1.1-5.4的浮点数，区间可以不是整数
    print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
    print(random.randrange(1, 100, 2))  # 随机生成1-100间隔为2的随机奇数，0-100间隔为2的偶数

    a = [1,2,3,4,5]  # 将列表a的元素顺序打乱
    random.shuffle(a)
    print(a)

    # 从a-zA-Z0-9生成指定数量的随机字符
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(random_str)

    # 多个字符中选取指定数量的字符组成新字符串
    str_list = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
    print(''.join(random.sample(str_list, 6)))
