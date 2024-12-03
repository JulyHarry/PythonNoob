from heapq import nsmallest
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        x = []
        for i, num in enumerate(nums):
            x.append((num, i))
        s = 0
        ans = []
        while k > 0:
            # print(s, n - k + 1)
            # print(x[s:n - k + 1], nsmallest(1, x[s:n - k + 1]))
            p = nsmallest(1, x[s:n - k + 1])[0]
            ans.append(p[0])
            s = p[1] + 1
            # print(s)
            k -= 1
        return ans

    def mostCompetitive2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        x = []
        for i, num in enumerate(nums):
            x.append((num, i))
        x.sort(key=lambda m: m[0])
        s = 0
        ans = []
        for i in range(n):
            if s <= x[i][1] <= n - k:
                ans.append(x[i][0])
                s = x[i][1] + 1
                k -= 1
                if k == 0:
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.mostCompetitive([3, 5, 2, 6], 2))
    # print(s.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
    print(s.mostCompetitive2([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3))
