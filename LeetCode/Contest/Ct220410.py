# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-10 10:30
"""
import math
from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, num: int) -> int:
        odd = [i for i in str(num) if int(i) & 1 == 1]
        even = [i for i in str(num) if int(i) & 1 == 0]
        odd.sort(reverse=True)
        even.sort(reverse=True)
        res = ''
        po, pe = 0, 0
        for i in str(num):
            if int(i) & 1 == 1:
                res += odd[po]
                po += 1
            else:
                res += even[pe]
                pe += 1
        print(res)
        return int(res)

    def minimizeResult(self, expression: str) -> str:
        sp = expression.find("+")
        min = math.inf

        def getInt(i: str, flag) -> int:
            if i == '':
                if flag:
                    return 1
                else:
                    return 0
            return int(i)

        res = '(' + expression + ')'
        for i in range(0, sp):
            for j in range(sp + 2, len(expression) + 1):
                a1 = expression[0:i]
                b1 = expression[i: sp]
                c1 = expression[sp + 1:j]
                d1 = expression[j:len(expression)]
                a = getInt(a1, True)
                b = getInt(b1, False)
                c = getInt(c1, False)
                d = getInt(d1, True)
                if a * (b + c) * d < min:
                    res = expression[0:i] + '(' + expression[i:j] + ')' + expression[j:len(expression)]
                    min = a * (b + c) * d
        return res

    def maximumProduct(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        m = sorted([i for i in c.keys()])
        i = 0
        while k > 0:
            if k >= c[m[i]]:
                k -= c[m[i]]
                c[m[i] + 1] += c[m[i]]
                c[m[i]] = 0
            else:
                c[m[i]] -= k
                c[m[i] + 1] = k
                k = 0
            i += 1
        res = 1
        for i in c.keys():
            res *= i ** c[i] % 1000000007
        return res


s = Solution()
print(s.maximumProduct([0, 4], 5))
