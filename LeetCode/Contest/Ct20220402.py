# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-02 22:15
"""
import time
from typing import List


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = start ^ goal
        cnt = 0
        while a > 0:
            a &= a - 1
            cnt += 1
        return cnt

    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        d = [0] * n
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * i
        for i in range(n // 2 + 1):
            d[i] = f[n - 1] // f[i] // f[n - i - 1]
        for i in range(n - 1, n // 2 - 1, -1):
            d[i] = d[n - 1 - i]
        for i, j in enumerate(nums):
            ans += d[i] * j % 10
        return ans % 10


s = Solution()
# print(s.minBitFlips(10, 7))
n = 5
nums = [0] * n
for i in range(n):
    nums[i] = i
a = time.time()
print(s.triangularSum(nums))
b = time.time()
print(b - a)
