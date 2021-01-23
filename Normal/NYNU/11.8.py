class Student:
    def __init__(self):
        self.id = 0
        self.score = 0


if __name__ == '__main__':
    stu = Student()
    n, m = input().split(' ')
    list_a = []
    list_b = []
    for j in range(int(n)):
        stu.id, stu.score = input().split(' ')
        list_a.append([])
        list_a[j].append(stu.id)
        list_a[j].append(stu.score)
    for j in range(int(m)):
        stu.id, stu.score = input().split(' ')
        list_b.append([])
        list_b[j].append(stu.id)
        list_b[j].append(stu.score)
    for i in list_b:
        list_a.append(i)
    for i in range(len(list_a)):  # 将所有数据转换为整型
        for j in range(2):
            list_a[i][j] = int(list_a[i][j])
    list_a.sort()
    for i in range(len(list_a)):
        print(list_a[i][0], list_a[i][1])
