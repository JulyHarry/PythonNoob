# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        n = len(supplies)
        j = n
        k = supplies.copy()
        while j > n // 2:
            m = 2001
            index = 0
            for i in range(len(k) - 1):
                cur = k[i] + k[i + 1]
                if cur < m:
                    index = i
                    m = cur
            k = k[:index] + [m] + k[index + 2:]
            j -= 1
        return k

    def adventureCamp(self, expeditions: List[str]) -> int:
        init = expeditions[0]
        visit = set()

        def countlog(s):
            if s:
                cnt = 0
                vs = s.split('->')
                for x in vs:
                    if x not in visit:
                        visit.add(x)
                        cnt += 1
                return cnt if cnt > 0 else -1
            return -1

        countlog(init)
        res = -1
        mx = -1
        for i in range(1, len(expeditions)):
            c = countlog(expeditions[i])
            if c > mx:
                res = i
                mx = c
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.supplyWagon(supplies=[7, 3, 6, 1, 8]))
    print(s.adventureCamp(["", "Gryffindor->Slytherin->Gryffindor", "Hogwarts->Hufflepuff->Ravenclaw"]))
