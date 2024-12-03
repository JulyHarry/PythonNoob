import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        ans = 0
        flag = False
        for i in range(k):
            if ans == n - 1:
                flag = True
            if ans == 0 and flag:
                flag = False
            if flag:
                ans -= 1
            else:
                ans += 1
        return ans

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        q = [0]
        n = len(rewardValues)
        rewardValues.sort()
        ans = 0
        while q:
            p = set()
            while q:
                cur = q.pop(0)
                i = bisect.bisect_right(rewardValues, cur)
                if i == len(rewardValues):
                    break
                for m in range(i, n):
                    p.add(cur + rewardValues[m])
                    ans = max(ans, cur + rewardValues[m])
            q = sorted(list(p))
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.numberOfChild(5, 6))
    # print(s.maxTotalReward([1, 1, 3, 3]))
    # print(s.maxTotalReward([1, 6, 4, 3, 2]))
    print(s.maxTotalReward([3, 10]))
