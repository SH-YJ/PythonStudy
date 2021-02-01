import pandas as pd

# 数据的读取,读取到的是一个DataFrame
data = pd.read_excel('Source/002.xlsx', header=1, index_col='ID')  # 若第一行不是列名，需要设置header=列名所在行,默认为0;若没有列名,设置header=None
# 读取数据时，会自动显示出一列索引，保存时也会一并保存，需要index_col=索引列名

data.columns = ['ID', 'Name', 'Address']  # 在没有列名时，人为设置列名

print(data.shape)  # 输出行与列的个数
print(data.columns)  # 输出每一列的列名，会自动忽略空白，被指定索引的ID不会输出
print(data.head(3))  # 默认输出头5行数据
print(data.tail(3))  # 默认输出最后5行数据
