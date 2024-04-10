i = 3
cnt = 1
while True:
    f = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            f = False
            break
    if f:
        print(i, cnt)
        cnt += 1
    if i == cnt:
        print("----------" + i)
        break
    i += 2
