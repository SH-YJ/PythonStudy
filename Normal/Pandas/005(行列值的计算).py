import pandas as pd


# 计算列的值

def add_3(x):
    return x + 3


books = pd.read_excel('Source/005.xlsx', index_col='ID')
books['价格'] = books['原价'] * books['折扣']  # books为Series,多行同时相乘
for i in books.index:  # 也可以使用迭代，精确到单元格相乘
    books['价格'].at[i] = books['原价'].at[i] * books['折扣'].at[i]

books['原价'] = books['原价'] + 3  # 普通的方法改变值
books['原价'] = books['原价'].apply(add_3)  # 使用Series的apply()方法
books['原价'] = books['原价'].apply(lambda x: x + 3)  # 与上一行效果相同

books.to_excel('Source/005.xlsx')
