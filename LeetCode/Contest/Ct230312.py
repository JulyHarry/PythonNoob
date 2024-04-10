# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


def maxScore(nums: List[int]) -> int:
    ans, cur = 0, 0
    nums.sort(reverse=True)
    for num in nums:
        cur += num
        if cur > 0:
            ans += 1
        else:
            return ans
    return ans


def beautifulSubarrays(nums: List[int]) -> int:
    n = len(nums)
    xor = [0] * (n + 1)
    for i, num in enumerate(nums):
        xor[i + 1] = xor[i] ^ nums[i]
    print(xor)
    m = Counter(xor)
    ans = 0
    for k, v in m.items():
        if v >= 0:
            ans += v * (v - 1) // 2
    return ans


def findMinimumTime(tasks: List[List[int]]) -> int:
    tasks.sort(key=lambda t: t[1])
    print(tasks)


class mycomp(list):
    def __lt__(self, other):
        if self[0] != other[0]:
            return self[0] < other[0]
        else:
            return self[1] < other[1]


# nums = [-687767, -860350, 950296, 52109, 510127, 545329, -291223, -966728, 852403, 828596, 456730, -483632, -529386,
#         356766, 147293, 572374, 243605, 931468, 641668, 494446]
# print(maxScore(nums))

# nums = [4, 3, 1, 2, 4, 0, 7, 0, 2]
# print(beautifulSubarrays(nums))


tasks = [[2, 3, 1], [4, 5, 1], [1, 5, 2]]
print(findMinimumTime(tasks))
