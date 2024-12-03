"""

7
IN 1 1
IN 1 2
IN 1 3
IN 2 1
OUT 1
OUT 2
OUT 2

"""
import heapq

n = int(input())
h = [[] for _ in range(6)]
for i in range(n):
    x = input()
    if x[:2] == 'IN':
        io, p, v = x.split()
        p = int(p)
        v = int(v)
        heapq.heappush(h[p], (-v, i + 1))
    else:
        io, p = x.split()
        p = int(p)
        if h[p]:
            print(heapq.heappop(h[p])[1])
        else:
            print('null')
