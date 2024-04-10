import time
from collections import Counter
from typing import List


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        max = 0
        res = ''
        while i < len(number):
            try:
                i = number.index(digit, i)
            except:
                break
            tmp = number[0:i] + number[i + 1:]
            if max < int(tmp):
                res = tmp
                max = int(tmp)
            i += 1
        return res

    def minimumCardPickup(self, cards: List[int]) -> int:
        l, r = 0, 0
        d = Counter()
        res = len(cards) + 1
        while r < len(cards):
            d[cards[r]] += 1
            if d[cards[r]] & 1 == 0:
                while l < r:
                    d[cards[l]] -= 1
                    if d[cards[l]] & 1 == 1:
                        res = min(res, r - l + 1)
                        l += 1
                        break
                    else:
                        l += 1
            r += 1
        if res == len(cards) + 1:
            return -1
        return res

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        r = 0
        o = 0
        s = set()
        while r < len(nums):
            if nums[r] % p == 0:
                o += 1
            l = 0
            t = o
            while l <= r:
                if t <= k:
                    s.add(tuple(nums[l:r + 1]))
                if nums[l] % p == 0:
                    t -= 1
                l += 1
            r += 1
        return len(s)

    def appealSum(self, s: str) -> int:
        res = len(s) * (len(s) + 1) // 2
        l = 0
        return res


number = "551"
digit = "5"
# cards = [3, 4, 2, 3, 4, 7]
cards = [77, 10, 11, 51, 69, 83, 33, 94, 0, 42, 86, 41, 65, 40, 72, 8, 53, 31, 43, 22, 9, 94, 45, 80, 40, 0, 84, 34, 76,
         28, 7, 79, 80, 93, 20, 82, 36, 74, 82, 89, 74, 77, 27, 54, 44, 93, 98, 44, 39, 74, 36, 9, 22, 57, 70, 98, 19,
         68, 33, 68, 49, 86, 20, 50, 43]
nums = [1, 2, 3, 4]
k = 4
p = 1
ss = "leet"
s = Solution()
a = time.time()
print(s.appealSum(ss))
b = time.time()
print(b - a)
