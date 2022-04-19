# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2021-08-29 11:31
"""
import heapq
from typing import List

# heap = []
# heapq.heappush(heap)
from numpy import long


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = [long(x) for x in nums]
        print(heap)
        return ""

#
# s = Solution()
# nums = ["1", "2", "10"]
# s.kthLargestNumber(nums, 3)


print(1+2)