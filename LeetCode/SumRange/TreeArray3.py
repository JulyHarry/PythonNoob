# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-17 01:57
"""
from typing import List


class TreeArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def sumRange(self, left: int, right: int):
        return self.query(right + 1) - self.query(left)

    def query(self, index: int) -> int:
        res = 0
        while index > 0:
            res += self.sums[index]
            index -= self.lowbit(index)
        return res

    def add(self, index: int, val: int):
        while index <= len(self.nums):
            self.sums[index] += val
            index += self.lowbit(index)

    def change(self, index, val: int):
        self.add(index, val - nums[index])

    def lowbit(self, index: int):
        return index & -index


nums = [1, 2, 3, 4, 5, 6, 7]
t = TreeArray(nums)
print(t.sums)
t.change(2, 5)
print(t.sumRange(1, 3))
