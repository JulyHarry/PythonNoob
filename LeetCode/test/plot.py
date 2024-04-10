import numpy as np
import matplotlib.pyplot as plt

# 散点图
# x, y
points = [[1, 3], [2, 0], [5, 10], [6, -10]]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 绘制散点图
plt.scatter(x, y, s=25, alpha=0.75)

# # 隐藏坐标轴刻度
plt.xticks(range(min(x), max(x) + 1, 1))
plt.yticks(range(min(y), max(y) + 1, 1))

# 显示图像
plt.show()
