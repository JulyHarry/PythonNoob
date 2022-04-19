# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-02 22:15
"""
from collections import defaultdict
from typing import List


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1 = int(current[0:2])
        h2 = int(correct[0:2])
        m1 = int(current[3:5])
        m2 = int(correct[3:5])
        sum = (h2 - h1) * 60 + m2 - m1
        ans = 0
        ans += sum // 60
        sum %= 60
        ans += sum // 15
        sum %= 15
        ans += sum // 5
        sum %= 5
        ans += sum
        return ans

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wr = defaultdict(int)
        lr = defaultdict(int)
        for w, l in matches:
            if not wr[w]:
                wr[w] = 1
            wr[l] = 2
            lr[l] += 1
        winner = []
        for a in wr.keys():
            if wr[a] == 1:
                winner.append(a)
        loseone = []
        for a in lr.keys():
            if lr[a] == 1:
                loseone.append(a)
        return [sorted(winner), sorted(loseone)]


s = Solution()
# print(s.convertTime("02:30", "02:31"))
matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
print(s.findWinners(matches))
