import copy

a = [20, [1, 2]]
# b = []
# for i in range(3):
#     a[0] = i
#     b.append(a.copy())
# print(b)
# print(id(b[0]), id(b[0][0]))
# print(id(b[1]), id(b[1][0]))
# print(id(b[2][0]))

c = copy.deepcopy(a)
a[1].append(3)
print(a, c)
