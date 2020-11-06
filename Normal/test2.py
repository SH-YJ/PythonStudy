from pymongo import MongoClient

client = MongoClient()

Computer = client.Computer
Student = Computer.Student
Score = Computer.Score

a = input('请输入查询班级:')
# 统计班级人数
all_student = len(list(Score.aggregate([
    {
        '$lookup':
            {
                "from": "Student",
                "localField": "name",
                "foreignField": "name",
                "as": "new_array_2"
            }
    },
    {
        '$project':
            {
                'kind': 1,
                'new_array_2': {'class': 1}
            }
    },
    {
        '$match':
            {
                'kind': '一级',
                'new_array_2': {'class': int(a)}
            }
    }
])))
# 统计通过人数
pass_student = len(list(Score.aggregate([
    {
        '$lookup':
            {
                "from": "Student",
                "localField": "name",
                "foreignField": "name",
                "as": "new_array_1"
            }
    },
    {
        '$project':
            {
                'sum_score': 1,
                'kind': 1,
                'new_array_1': {'class': 1}
            }
    },
    {
        '$match':
            {
                'kind': '一级',
                'sum_score': {'$gte': 150},
                'new_array_1': {'class': int(a)}
            }
    }
])))

# 通过率
pass_rate = pass_student / all_student * 100
print(a, '班通过率为:', pass_rate, '%')
