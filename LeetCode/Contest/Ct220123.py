# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-23 10:26
"""

from collections import deque
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        res = []
        for i in range(len(pos)):
            res.append(pos.popleft())
            res.append(neg.popleft())
        return res

    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0:
                if nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i]:
                    res.append(nums[i])
            elif i == len(nums) - 1:
                if nums[i - 1] != nums[i] - 1 and nums[i - 1] != nums[i]:
                    res.append(nums[i])
            elif (nums[i - 1] != nums[i] - 1 and nums[i - 1] != nums[i]) and (
                    nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i]):
                res.append(nums[i])
        return res

    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0

        for i in range(0, 1 << n):
            if self.judge(i, statements):
                print(bin(i))
                res = max(res, bin(i).count("1"))
        return res

    def judge(self, condition: int, statements: List[List[int]]) -> bool:
        n = len(statements)
        isGood = [2] * n  # 0-bad 1-good 2-no matter
        for i in range(0, n):
            cur = 1 << i
            if cur & condition != 0:
                if isGood[i] == 0:
                    return False
                isGood[i] = 1
                for j in range(n):
                    status = statements[i][j]
                    if status != 2:
                        if isGood[j] == 2:
                            isGood[j] = status
                        else:
                            if isGood[j] != status:
                                return False
        return True


s = Solution()
# nums = [3, 1, -2, -5, 2, -4]
# print(s.rearrangeArray(nums))
# nums = [10, 6, 5, 8, 4, 10]
# print(s.findLonely(nums))
statements = [[2, 2, 2, 2], [1, 2, 1, 0], [0, 2, 2, 2], [0, 0, 0, 2]]
print(s.maximumGood(statements))
# 1
