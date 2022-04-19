# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-10 01:17
"""

# -*- coding: utf-8 -*-
"""
Description:
Creator: HarryUp
Create time: 2022-04-09 23:17
"""
from typing import List


class TreeArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.sums = [0] * (self.n + 1)
        i = 0

        def initSum(index: int, v: int):
            while index < self.n:
                self.sums[index + 1] += v
                index += (index + 1) & (-index - 1)

        while i < self.n:
            initSum(i, self.nums[i])
            i += 1
        print(self.sums)

    def update(self, i: int, v: int):
        ov = self.nums[i]
        j = i
        while i < self.n:
            self.sums[i + 1] += v - ov
            i += (i + 1) & (-i - 1)
        self.nums[j] = v

    def sumRange(self, l: int, r: int):
        def calSum(i: int):
            sum = 0
            while i > 0:
                sum += self.sums[i]
                i &= i - 1
            return sum

        return calSum(r + 1) - calSum(l)


nums = [1, 3, 5, 22, 53, 55, 23, 24, 54, 32, 23, 56, 23, 4]
t = TreeArray(nums)
print(t.sums)
print(t.sumRange(4, 11))
t.update(4, -12)
print(t.sums)
print(t.sumRange(4, 11))
