# t = int(input())
#
# for _ in range(t):
#     n, k = map(int, input().split())
#
#
#     # red 0 blue 1
#
#     def dfs(n, k):
#         if n == 1:
#             return 0
#         if k <= (1 << n - 2) - 1:
#             return 1 - dfs(n - 1, k)
#         else:
#             return dfs(n - 1, k - (1 << n - 2))
#
#     print(dfs(n, k))
# print('blue' if dfs(n, k) else 'red')
from functools import cache


# 验证程序
def dfs(n, k):
    if n == 1:
        return 0
    if k <= (1 << n - 2) - 1:
        return 1 - dfs(n - 1, k)
    else:
        return dfs(n - 1, k - (1 << n - 2))


def reverse(a):
    ans = []
    for x in a:
        ans.append(str(ord('1') - ord(x)))
    return ''.join(ans) + a


@cache
def getnstr(n):
    x = '0'
    for i in range(n - 1):
        x = reverse(x)
    return x


def compare(n, k):
    s = getnstr(n)
    print('正确' if int(s[k]) == dfs(n, k) else '错误')


for i in range(500):
    compare(10, i)
