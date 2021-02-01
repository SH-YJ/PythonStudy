import pandas as pd

# Series类似于dict,index即key，pd读取到的数据是Series类型的
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

df_dict = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})  # 以字典的形式写入数据,ABC为列名,123为索引
df_list = pd.DataFrame([s1, s2, s3])  # 以列表的形式写入数据,123为列名，ABC为索引

df_dict.to_excel('Source/003(dict).xlsx')
df_list.to_excel('Source/003(list).xlsx')

print(df_dict)
print(df_list)