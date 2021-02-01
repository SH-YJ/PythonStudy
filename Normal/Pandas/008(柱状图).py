import pandas as pd
import matplotlib.pyplot as plt

# 数据可视化：柱状图
student = pd.read_excel('Source/008.xlsx')
student.sort_values(by='Number', inplace=True, ascending=False)
print(student)
# 使用pandas创建图表
student.plot.bar(x='Field', y='Number', color='red', title='A Title')

# 使用matplotlib创建图表
plt.bar(student.Field, student.Number, color='orange')

plt.xticks(student.Field, rotation='90')  # rotation 旋转角度，默认以中心旋转
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('A title')
plt.tight_layout()  # 紧凑型布局
plt.show()  # pandas与 matplotlib创建的图表都需要这句话
