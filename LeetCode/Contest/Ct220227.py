# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-02-27 10:29
"""
from collections import Counter
from typing import List


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = Counter(s)
        b = Counter(t)
        c = (a - b) + (b - a)
        ans = 0
        for m in c:
            ans += c[m]
        return ans

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def can(now: int) -> bool:
            res = 0
            for t in time:
                res += now // t
                if res >= totalTrips:
                    return True
            return False

        time.sort()
        l, r = 1, 10000000
        while l < r:
            m = l + (r - l) // 2
            if can(m):
                r = m
            else:
                l = m + 1
        return l


s = Solution()
print(s.minSteps("lee", "de"))
# print(s.minimumTime([1, 2, 3], 5))
