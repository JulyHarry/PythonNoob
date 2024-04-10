# -*- coding: utf-8 -*-
from typing import List


def leftRigthDifference(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for i in range(n):
        left[i + 1] = left[i] + nums[i]
    print(left)
    for i in range(n - 1, -1, -1):
        right[i] = right[i + 1] + nums[i]
    print(right)
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = abs(left[i] - right[i])
    print(ans)
    return ans


def divisibilityArray(word: str, m: int) -> List[int]:
    n = len(word)
    ans = [0] * n
    cur = 0
    for i in range(0, n):
        cur += int(word[i])
        cur %= m
        if cur == 0:
            ans[i] = 1
        cur *= 10
    return ans


def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    visit = set()
    l, r = 0, n - 1
    while l < r:
        m = (l + r + 1) // 2
        if nums[m] * 2 > nums[n - 1]:
            r = m - 1
        else:
            l = m
    print(l, nums[l])
    for right in range(n - 1, 0, -1):
        if right not in visit:
            while l >= 0:
                if nums[right] >= 2 * nums[l]:
                    visit.add(right)
                    visit.add(l)
                    l -= 1
                    break
                l -= 1
    return len(visit)


if __name__ == '__main__':
    # leftRigthDifference([10, 4, 8, 3])
    # print(divisibilityArray("1010", 10))
    # print(maxNumOfMarkedIndices(
    #     [1, 78, 27, 48, 14, 86, 79, 68, 77, 20, 57, 21, 18, 67, 5, 51, 70, 85, 47, 56, 22, 79, 41, 8, 39, 81, 59, 74,
    #      14, 45, 49, 15, 10, 28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8, 96, 78, 39, 92, 69, 55, 9, 44, 26, 76,
    # 40, 77, 16, 69, 40, 64, 12, 48, 66, 7, 59, 10]))
    print(maxNumOfMarkedIndices(
        [42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40]))
