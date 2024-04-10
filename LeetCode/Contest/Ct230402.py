# -*- coding: utf-8 -*-
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        flag = False
        res = 0
        cnt0, cnt1 = 0, 0
        for i in range(n):
            if i > 0 and s[i] == '0' and s[i - 1] == '1':
                flag = True
            else:
                flag = False
            if flag:
                res = max(res, 2 * min(cnt0, cnt1))
                cnt0, cnt1 = 0, 0
                flag = False
            if s[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
        return res

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        mx = 0
        for k, v in counter.items():
            mx = max(mx, v)
        res = [[] for _ in range(mx)]
        for k, v in counter.items():
            while v > 0:
                res[v - 1].append(k)
                v -= 1
        return res

    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        f = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            for j in range(k + 1):
                if i == 0:
                    if j > 1:
                        f[i][j] = max(f[i][j - 1] + reward1[i], f[i][j] + reward2[i])
                else:
                    f[i][j] = f[i - 1][j] + reward2[i]
                    if j > 1:
                        f[i][j] = max(f[i][j], f[i - 1][j - 1] + reward1[i])
        print(f)
        return f[n - 1][k]


s = Solution()
# print(s.findTheLongestBalancedSubstring('01000111'))

# print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))

print(s.miceAndCheese(reward1=[1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2))
