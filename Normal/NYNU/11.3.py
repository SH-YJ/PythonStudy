class Student:
    def __init__(self):
        self.id = 0
        self.name = 0
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0


if __name__ == '__main__':
    stu = Student()
    n = int(input())
    list = []
    for i in range(0, n):
        list.append([])
        line = input().split(' ')
        for j in line:
            list[i].append(j)
    for i in range(0, n):
        for j in range(5):
            if j != 4:
                print(list[i][j], end=',')
            else:
                print(list[i][j])
