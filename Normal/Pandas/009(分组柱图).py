import pandas as pd
import matplotlib.pyplot as plt

# 数据可视化：分组柱状图
student = pd.read_excel('Source/009.xlsx')
student.sort_values(by='2017', inplace=True, ascending=False)
print(student)
# 使用pandas创建图表
student.plot.bar(x='Field', y=['2016', '2017'], color=['orange', 'purple'])
plt.title('留学生数量', fontsize=15, fontweight='bold')
plt.xlabel('领域', fontweight='bold')
plt.ylabel('数量', fontweight='bold')

ax = plt.gca()  # gca()获取x轴
ax.set_xticklabels(student['Field'], rotation='45', ha='right')
# roration 旋转度数，默认以中心旋转 ha:设置旋转起始点right,left,center

f = plt.gcf()  # gcf()获取图像
f.subplots_adjust(left=0.2, bottom=0.42)  # 设置图像间隔与tight_layout()功能差不多，只是更细

# plt.tight_layout()
plt.show()
