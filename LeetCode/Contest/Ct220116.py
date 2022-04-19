# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-16 10:42
"""


class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        res = 0
        while target > 1:
            if maxDoubles > 0 and target & 1 == 0:
                target //= 2
                res += 1
                maxDoubles -= 1
            elif maxDoubles == 0:
                res += target - 1
                return res
            else:
                target -= 1
                res += 1
        print(res)
        return res


s = Solution()
print(s.minMoves(100, 1))
