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
    score1_sum, score2_sum, score3_sum, max_score, index = 0, 0, 0, 0, 0
    score1_ave, score2_ave, score3_ave = 0, 0, 0
    for i in range(0, n):
        list.append([])
        line = input().split(' ')
        for j in line:
            list[i].append(j)
    for i in range(0, n):
        score1_sum += int(list[i][2])
        score2_sum += int(list[i][3])
        score3_sum += int(list[i][4])
        if int(list[i][2]) + int(list[i][3]) + int(list[i][4]) > max_score:
            max_score = int(list[i][2]) + int(list[i][3]) + int(list[i][4])
            index = i
    score1_ave, score2_ave, score3_ave = score1_sum // n, score2_sum // n, score3_sum // n
    print(score1_ave, score2_ave, score3_ave)
    for i in list[index]:
        print(i,end=' ')