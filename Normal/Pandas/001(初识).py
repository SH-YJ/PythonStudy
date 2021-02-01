import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3, 4], '姓名': ['小明', '小红', '小王', '小刚']})  # 创建数据框架，在括号添加数据
df = df.set_index('ID')  # 设置索引，默认索引，会多生成一列索引数据
df.to_excel('Source/001.xlsx')  # 创建excel文件
