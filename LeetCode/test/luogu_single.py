import bisect
import math
from itertools import accumulate

n = int(input())
ans = math.inf
xl, yl, p = [], [], []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x + y, x - y))
    xl.append(x + y)
    yl.append(x - y)
xl.sort()
yl.sort()
prex = list(accumulate(xl, initial=0))
prey = list(accumulate(yl, initial=0))
for x, y in p:
    kx = bisect.bisect_left(xl, x)
    ky = bisect.bisect_left(yl, y)
    sx = prex[n] - 2 * prex[kx + 1] + (2 * kx - n + 2) * x
    sy = prey[n] - 2 * prey[ky + 1] + (2 * ky - n + 2) * y
    ans = min(ans, sx + sy)
print(ans // 2)
