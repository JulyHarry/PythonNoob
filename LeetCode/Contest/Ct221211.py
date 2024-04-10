# -*- coding: utf-8 -*-
import math
from typing import List, Counter


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for i in nums:
            tmp = 0
            lg = int(math.sqrt(i))
            if lg * lg == i and str(i) not in d and str(lg) in d:
                tmp = d[str(lg)]
            if str(i) not in d:
                d[str(i)] = tmp + 1
        length = max([d[k] for k in d])
        if length < 2:
            return -1
        return length


if __name__ == '__main__':
    s = Solution()
    num = [2, 4, 4, 2, 16, 81, 2, 65536]
    # num = [10, 2, 13, 16, 8, 9, 13]
    print(s.longestSquareStreak(num))
