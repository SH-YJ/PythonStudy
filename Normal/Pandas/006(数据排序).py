import pandas as pd

# 数据排序
product = pd.read_excel('Source/006.xlsx', index_col='ID')
product.sort_values(by='价格', inplace=True, ascending=False)  # ascending:默认True从低到高排序，False从高到低排序
product.sort_values(by=['是否有价值', '价格'], inplace=True, ascending=[True, False])  # 多重排序
print(product)
