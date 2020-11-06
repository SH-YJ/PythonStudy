from pymongo import MongoClient
import os

client = MongoClient()
Computer = client.Computer
Student = Computer.Student
Score = Computer.Score


def search_name(a):  # 姓名查询
    name = list(Score.find({'name': a}, {'_id': 0, "write_score": 1, "computer_score": 1, "sum_score": 1}))
    return name


def search_admit_id(i):  # 准考证号查询
    id = list(Score.find({'admission_id': int(i)}, {"_id": 0, "write_score": 1, "computer_score": 1}))
    return id


def search_id_card(a):  # 身份证号查询
    id_card = list(Score.find({'id_card': int(a)}, {"_id": 0, "write_score": 1, "computer_score": 1}))
    return id_card


if __name__ == "__main__":
    while 1:
        os.system("cls")
        print(" ---------------- ")
        print("|   1.查询 2.统计 |")
        print("|      3.退出    |")
        print(" ---------------- ")
        print("请选择功能：", end='')
        b = input()
        while b == '1':
            os.system("cls")
            print("|    进入查询界面      |")
            print("|     1.姓名          |")
            print("|     2.准考证号      |")
            print("|     3,身份证号      |")
            print("|     4.返回主界面    |")
            print("请输入你的选择：", end='')
            ai = input()
            if ai == '1':
                a = input("请输入查询的姓名：")
                print("详细信息如下：", end='')
                print(search_name(a))

            elif ai == '2':
                a = input("请输入查询的准考证号：")
                print("详细信息如下：", end='')
                print(search_admit_id(a))

            elif ai == '3':
                a = input("请输入查询的身份证号：")
                print("详细信息如下：", end='')
                print(search_id_card(a))

            else:
                break
