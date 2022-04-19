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
        for i, num in enumerate(nums, 1):
            self.add(i, num)
        print(self.sums)

    def add(self, i: int, v: int):
        while i < self.n:
            self.sums[i] += v
            i += i & (-i)

    def update(self, i: int, v: int):
        self.add(i + 1, v - self.nums[i])
        self.nums[i] = v

    def sumRange(self, l: int, r: int):
        def calSum(i: int):
            sum = 0
            while i > 0:
                sum += self.sums[i]
                i -= i & (-i)
            return sum

        return calSum(r + 1) - calSum(l)


nums = [1, 3, 5, 22, 53, 55, 23, 24, 54, 32, 23, 56, 23, 4]
t = TreeArray(nums)
print(t.sums)
print(t.sumRange(4, 11))
t.update(4, -12)
print(t.sums)
print(t.sumRange(4, 11))
