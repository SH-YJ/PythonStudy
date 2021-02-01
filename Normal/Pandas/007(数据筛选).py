import pandas as pd


def age(a):
    return 18 <= a < 25


def score(s):
    return 80 <= s < 95


# 数据筛选、过滤
student = pd.read_excel('Source/007.xlsx', index_col='ID')
student = student.loc[student['Age'].apply(age)].loc[student['Score'].apply(score)]
# loc：在index的标签上进行索引(即是在index上寻找相应的标签，不是下标)，范围包括start和end
# iloc：在index的位置上进行索引(即是按照普通的下标寻找),不包括end.
# ix：先在index的标签上索引，索引不到就在index的位置上索引(如果index非全整数),不包括end。
print(student)
