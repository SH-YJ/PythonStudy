class Year:

    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

    def Judge(self):
        if Sn.year % 4 == 0 and Sn.year % 100 != 0 or Sn.year % 400 == 0 and Sn.month > 2:
            return True
        else:
            return False

if __name__ == '__main__':
    every_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Sn = Year()
    line = input().split(' ')
    Sn.year = int(line[0])
    Sn.month = int(line[1])
    Sn.day = int(line[2])
    sum = Sn.day
    for i in range(0, Sn.month - 1):
        sum += every_month[i]
    if Sn.Judge() is True:
        sum += 1
        print(sum)
    else:
        print(sum)
