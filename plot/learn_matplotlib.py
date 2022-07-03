import matplotlib.pyplot as plt
from matplotlib import style

# matplotlib.rcParams['text.usetex'] = False
plt.figure(figsize=(10, 10), dpi=70)
style.use('ggplot')
x, y = 1, 100
plt.scatter(x, y, 50)
# plt.savefig('myplot4.pdf', dpi=700)
plt.show()
