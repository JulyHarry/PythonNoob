# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-16 22:31
"""
import math
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minv = math.inf
        res = 0
        for num in nums:
            if abs(num) < minv:
                minv = abs(num)
                res = num
            elif abs(num) == minv:
                res = max(res, num)
        return res

    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        maxcost = max(cost1, cost2)
        mincost = min(cost1, cost2)
        res = 0
        n = total // maxcost
        for i in range(n + 1):
            res += (total - maxcost * i) // mincost + 1
        return res

    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        new_edges = [[] for _ in range(n)]
        for x, y in edges:
            new_edges[x].append(y)
            new_edges[y].append(x)
        max_val = -1

        def dfs(edges: List[List[int]], node: int, level: int, val: int, visited: List[bool]) -> None:
            if level == 3:
                val += scores[node]
                nonlocal max_val
                max_val = max(max_val, val)
            visited[node] = True
            for next_node in edges[node]:
                if not visited[next_node]:
                    dfs(edges, next_node, level + 1, val + scores[node], visited)

        for i in range(n):
            dfs(new_edges, i, 0, 0, [False] * n)
        return max_val


class ATM:

    def __init__(self):
        self.money = [0] * 5
        self.val = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, b in enumerate(banknotesCount):
            self.money[i] += b

    def withdraw(self, amount: int) -> List[int]:
        backup = self.money.copy()
        takeup = [0] * 5
        for i in range(4, -1, -1):
            if amount >= self.val[i]:
                j = amount // self.val[i]
                left = min(j, self.money[i])
                amount -= left * self.val[i]
                self.money[i] -= left
                takeup[i] += left
        if amount > 0:
            self.money = backup
            return [-1]
        return takeup


s = Solution()
# scores = [5, 2, 9, 8, 20]
# edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
scores = [18, 6, 4, 9, 8, 2]
edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5],
         [4, 5]]
# scores = [9, 20, 6, 4, 11, 12]
# edges = [[0, 3], [5, 3], [2, 4], [1, 3]]
# print(s.findClosestNumber(nums))
# print(s.waysToBuyPensPencils(500000, 10, 10))
print(s.maximumScore(scores, edges))

# a = ATM()
# a.deposit([0, 0, 1, 2, 1])
# print(a.withdraw(600))
# a.deposit([0, 1, 0, 1, 1])
# print(a.withdraw(600))
# print(a.money)
# print(a.withdraw(550))
# print(a.money)
