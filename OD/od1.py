"""
a b 逆序 中位数
"""
a = [3, 2, 1]
b = [4]

cnt = 0
i, j = 0, 0
l = len(a) + len(b)

while cnt < l // 2 - 1:
    if i < len(a) and j < len(b) and a[i] >= b[j]:
        i += 1
    elif j < len(b):
        j += 1
    cnt += 1

if l % 2:
    if a[i] >= b[j]:
        print(a[i])
    else:
        print(b[j])

else:
    if j == len(b):
        print((a[i] + a[i + 1]) / 2)
    elif i == len(a):
        print((b[j] + b[j + 1]) / 2)
    else:
        print((a[i] + b[j]) / 2)
