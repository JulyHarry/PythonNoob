# import matplotlib.pyplot as plt
# from matplotlib import style
#
# # matplotlib.rcParams['text.usetex'] = False
# plt.figure(figsize=(10, 10), dpi=70)
# style.use('ggplot')
# x, y = 1, 100
# plt.scatter(x, y, 50)
# # plt.savefig('myplot4.pdf', dpi=700)
# plt.show()

#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 创建数据
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# # 创建一个图和两个坐标轴
# fig, (ax1, ax2) = plt.subplots(2)
#
# # 在第一个坐标轴上绘制正弦波
# ax1.plot(x, y1)
# ax1.set_title('Sine Wave')
# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)')
#
# # 在第二个坐标轴上绘制余弦波
# ax2.plot(x, y2)
# ax2.set_title('Cosine Wave')
# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x)')
#
# # 保存图像
# fig.savefig('two_subplots.png')
#
# # 显示图像
# plt.show()
