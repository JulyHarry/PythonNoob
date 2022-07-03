from typing import List


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = len(str(num))
        res = 0
        for i in range(n - k + 1):
            cur = int(str(num)[i:i + k])
            if cur != 0 and num % cur == 0:
                res += 1
        return res

    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n + 1)
        for i in range(n):
            sum[i + 1] = sum[i] + nums[i]
        res = 0
        for i in range(1, n):
            if sum[i] >= sum[n] - sum[i]:
                res += 1
        return res


s = Solution()
# print(s.divisorSubstrings(24000000, 2))
print(s.waysToSplitArray([2, 3, 1, 0]))
