# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-02-20 11:00
"""
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        d = sorted(set(c.keys()), reverse=True)
        res = ""
        while True:
            for i in range()


s = Solution()
a = "cczazcc"
s.repeatLimitedString(a, 2)
