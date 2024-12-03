'''
第一行输入为N，表示小华排成一排的积木总数。
接下来N行每行一个数字，表示小华排成一排的积木上数字。
'''
from collections import Counter

n = int(input())
nums = []
c = Counter()
for _ in range(n):
    x = int(input())
    nums.append(x)
    c[x] += 1
flag = False
for v in c.values():
    if v > 1:
        flag = True
        break
if not flag:
    print(-1)
s = 1
ans = 0
for l in range(n):
    for r in range(s, n):
        if nums[l] == nums[r]:
            print(nums[l], l, r, nums)
            s = r + 1
            ans = max(ans, r - l)
print(ans)
