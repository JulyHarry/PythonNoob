# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-22 21:43
"""

from typing import List, Counter


class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        print(cost)
        res = 0
        i = len(cost)
        while i >= 1:
            if i >= 1:
                res += cost[i - 1]
            if i >= 2:
                res += cost[i - 2]
            i -= 3
        return res

    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        a = [((2, 1), 4, 9), ((2, 2), 6, 7), ((1, 2), 3, 7)]
        a.sort()
        print(a)
        a.append()

    def numberOfWays(self, corridor: str) -> int:
        seat = 0
        dis = []
        cur = []
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seat += 1
                cur.append(i)
                if seat & 1 == 0:
                    dis.append(cur)
                    cur = []
        if seat & 1 == 1:
            return 0
        res = 1
        for i in range(1, len(dis)):
            res *= dis[i][0] - dis[i - 1][1]
            res %= 1000000007
        return res

    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1
        ans, mx = 0, 0
        for i, j in cnt.items():
            if j > mx:
                ans = i
        return ans

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        e = [[] for _ in range(8)]
        ans = [[] for _ in range(8)]
        for x, y in edges:
            e[x].append(y)

        def dfs(pre: List, node: int):
            for i in e[node]:
                ans[i].extend(pre)
                if len(e[i]) != 0:
                    dfs(ans[i], i)

        for node in range(8):
            dfs(node, node)
        return ans

    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            if k > 0:
                n = nums[i] - nums[i - 1]
                if n > k:
                    n = k
                k -= n
                ans += (n - 1) * nums[i] + n * (n - 1) // 2
        last = nums[-1] + 1
        while k > 0:
            ans += last
            last += 1
            k -= 1
        return ans


# cost = [6, 5, 7, 9, 2, 2]
# cost = [1, 2, 3]
# cost = [2]
# print(Solution().minimumCost(cost))
# Solution().highestRankedKItems([1], [2], [3], 2)
# nums = [2, 2, 2, 3]
# key = 2
# print(Solution().mostFrequent(nums, key))
# n = 8
# edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
# print(Solution().getAncestors(n, edgeList))

nums = [5, 6]
k = 6
print(Solution().minimalKSum(nums, k))
