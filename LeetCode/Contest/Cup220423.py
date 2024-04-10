import math
from typing import List


class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        res = 0
        for typo, num in fruits:
            cnt = num // limit
            if num % limit != 0:
                cnt += 1
            res += cnt * time[typo]
        return res

    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[math.inf] * n for _ in range(m)]
        dp[start[0]][start[1]] = 0
        s = set()
        s.add((start[0], start[1]))

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or len(s) == 0:
                return
            i, j = s.pop()
            ch = matrix[i][j]
            l, r, u, d = 1, 1, 1, 1
            if ch == '<':
                l = 0
            elif ch == '>':
                r = 0
            elif ch == '^':
                d = 0
            else:
                u = 0
            if i > 0:
                x, y = i - 1, j
                cnt = min(dp[x][y], dp[i][j] + d)
                if dp[x][y] != cnt:
                    s.add((x, y))
                dp[x][y] = cnt
            if i < m - 1:
                x, y = i + 1, j
                cnt = min(dp[x][y], dp[i][j] + u)
                if dp[x][y] != cnt:
                    s.add((x, y))
                dp[x][y] = cnt
            if j > 0:
                x, y = i, j - 1
                cnt = min(dp[x][y], dp[i][j] + l)
                if dp[x][y] != cnt:
                    s.add((x, y))
                dp[x][y] = cnt
            if j < n - 1:
                x, y = i, j + 1
                cnt = min(dp[x][y], dp[i][j] + r)
                if dp[x][y] != cnt:
                    s.add((x, y))
                dp[x][y] = cnt
            for x, y in s.copy():
                dfs(x, y)

        dfs(start[0], start[1])
        return int(dp[end[0]][end[1]])

    def conveyorBelt1(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[math.inf] * n for _ in range(m)]
        dp[start[0]][start[1]] = 0
        s = []
        s.append((start[0], start[1]))

        while s:
            i, j = s.pop(0)
            if i < 0 or i >= m or j < 0 or j >= n:
                continue
            ch = matrix[i][j]
            l, r, u, d = 1, 1, 1, 1
            if ch == '<':
                l = 0
            elif ch == '>':
                r = 0
            elif ch == '^':
                d = 0
            else:
                u = 0
            if i > 0:
                x, y = i - 1, j
                cnt = min(dp[x][y], dp[i][j] + d)
                if dp[x][y] != cnt and (x, y) not in s:
                    s.append((x, y))
                dp[x][y] = cnt
            if i < m - 1:
                x, y = i + 1, j
                cnt = min(dp[x][y], dp[i][j] + u)
                if dp[x][y] != cnt and (x, y) not in s:
                    s.append((x, y))
                dp[x][y] = cnt
            if j > 0:
                x, y = i, j - 1
                cnt = min(dp[x][y], dp[i][j] + l)
                if dp[x][y] != cnt and (x, y) not in s:
                    s.append((x, y))
                dp[x][y] = cnt
            if j < n - 1:
                x, y = i, j + 1
                cnt = min(dp[x][y], dp[i][j] + r)
                if dp[x][y] != cnt and (x, y) not in s:
                    s.append((x, y))
                dp[x][y] = cnt

        return int(dp[end[0]][end[1]])

    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        res = 1
        cur = 1
        for i in range(1, len(runes)):
            if runes[i] - runes[i - 1] <= 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        res = max(res, cur)
        return res

    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        n = [0] * (len(rampart) - 1)
        for i in range(1, len(rampart)):
            n[i - 1] = rampart[i][0] - rampart[i - 1][1]
        mx = 0
        for i in range(1, len(n)):
            mx = max(mx, n[i] + n[i - 1])

        def check(x):
            left = 0
            for m in n:
                if m + left >= x:
                    left = 0
                elif left > 0:
                    return False
                else:
                    left = x - m - left
            return left <= 0

        l, r = 0, mx
        while l < r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m
        return l


if __name__ == '__main__':
    # matrix = [">^^>><<><>^^>><<><<<><>^^>>", "<^v>v>^^>><<<><>^^>><><v^><", "^v^<>>^^<<><>^^>>>><<><<<>^",
    #           "<^v>vv>^^>><<><^><v>^^>><<>", "^v^<><<>^^>v>^^>><<>><<><>^", "<^v>>^^>v>^^>><<>><<><vv^><",
    #           "<^v>vv>^^>><<><^><v>^^>><<>", "^v^<><<>^^>v>^^>><<>><<><>^", "<^v>>^^>v>^^>><<>><<><vv^><",
    #           "^v^<>^^>><<><><<>^^^>><<><>", "<^v>vv>^^>>^^>><<><><<><^><", "^v^<><<>^^>><<><>^^>><<><>^",
    #           ]
    # start = [0, 0]
    # end = [10, 17]
    # matrix = [">^^>", "<^v>", "^v^<"]
    # start = [0, 0]
    # end = [1, 3]
    s = Solution()
    # t1 = time.time()
    # print(s.conveyorBelt(matrix, start, end))
    # t2 = time.time()
    # print(t2 - t1)
    # print(s.runeReserve(runes=[1, 3, 5, 4, 1, 7, 8, 9, 10]))
    print(s.rampartDefensiveLine([[3, 5], [12, 29], [31, 38], [39, 42], [43, 44], [46, 47]]))
