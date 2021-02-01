import pandas as pd
from datetime import date, timedelta


def add_month(d: date, md):  # 按照月份递增
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


# 数据自动填充
book = pd.read_excel('Source/004.xlsx', skiprows=3, usecols='C:F',
                     dtype={'ID': str, 'ISBN': str, '是否有货': str, '日期': str})
# skiprows:跳过空行,usecols:使用哪几列数据,dtype:设置读取的数据类型,python不允许NaN转换为int，所以要转换为str

day = date(2020, 1, 1)
for i in book.index:
    book['ID'].at[i] = i + 1
    book['是否有货'].at[i] = 'Yes' if i % 2 == 0 else 'NO'
    book['日期'].at[i] = add_month(day, i)
    # 按天递增 day + timedelta(days=i)  # timedetla:参数可以是days及其以下的时间单位
    # 按年份递增 date(day.year + i,day.month, day.day)

book.set_index('ID', inplace=True)  # inplace=True 是否在原DataFrame上修改
book.to_excel('Source/004(complete).xlsx')
