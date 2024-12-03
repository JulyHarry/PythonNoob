import heapq

n = int(input())
nums = [list(map(int, input().split(' '))) for _ in range(n)]
nums.sort(key=lambda x: (x[0], -x[1]))
h = []
ans = 0
for x, y in nums:
    if x > len(h):
        heapq.heappush(h, y)
        ans += y
    elif x == len(h):
        ans += y
        heapq.heappush(h, y)
        ans -= heapq.heappop(h)
print(ans)
