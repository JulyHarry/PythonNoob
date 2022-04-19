# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-02-19 23:19
"""
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1 == 1:
            return []
        res = []
        a = 2
        while a <= finalSum:
            if finalSum < 2 * a:
                res.append(finalSum)
                break
            finalSum -= a
            res.append(a)
            a += 2
        return res


s = Solution()
print(s.maximumEvenSplit(8))
