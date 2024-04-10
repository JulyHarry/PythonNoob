import math
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if s.startswith(word):
                res += 1
        return res

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n + 1)
        for i in range(1, len(sum)):
            sum[i] = sum[i - 1] + nums[i - 1]
        res = math.inf
        ans = 0
        for i in range(0, n):
            l, r = 0, 0
            l = sum[i + 1] // (i + 1)
            if i != n - 1:
                r = (sum[n] - sum[i + 1]) // (n - i - 1)
            if res > abs(l - r):
                ans = i
                res = abs(l - r)
        return ans


words = ["a", "b", "c", "ab", "bc", "abc"]
s1 = "abc"
nums = [2, 5, 3, 9, 5, 3]
s = Solution()
print(s.minimumAverageDifference(nums))
