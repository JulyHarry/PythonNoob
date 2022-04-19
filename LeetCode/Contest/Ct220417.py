from collections import Counter
from typing import List


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            new_s = ""
            for i in range(0, n, k):
                cur = s[i:i + k]
                res = 0
                for a in cur:
                    res += int(a)
                new_s += str(res)
            s = new_s
            n = len(s)
        return s

    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for k, v in c.items():
            flag = True
            for i in range(v // 3, -1, -1):
                if (v - i * 3) % 2 == 0:
                    flag = False
                    res += int(i + (v - i * 3) / 2)
                    break
            if flag:
                return -1
        return res

    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid2 = [[0] * n for _ in range(m)]
        grid5 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt2 = 0
                cur = grid[i][j]
                while cur > 0:
                    if cur % 2 == 0:
                        cnt2 += 1
                        cur //= 2
                    else:
                        break
                grid2[i][j] = cnt2
                cnt5 = 0
                cur = grid[i][j]
                while cur > 0:
                    if cur % 5 == 0:
                        cnt5 += 1
                        cur //= 5
                    else:
                        break
                grid5[i][j] = cnt5

        # print(grid2)
        # print(grid5)
        row = [[[0, 0] for _ in range(n + 1)] for _ in range(m)]
        col = [[[0, 0] for _ in range(n)] for _ in range(m + 1)]
        # grid5 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row[i + 1][j][0] += row[i][j][0] + grid2[i][j]
                row[i + 1][j][1] += row[i][j][1] + grid5[i][j]

        for i in range(m):
            for j in range(n):
                col[i][j + 1][0] += col[i][j][0] + grid2[i][j]
                col[i][j + 1][1] += col[i][j][1] + grid5[i][j]
        for x in row:
            print(x)
        print("-------")
        for y in col:
            print(y)
        res = 0
        for i in range(m):
            for j in range(n):
                left = [col[i][j + 1][0] - col[i][0][0], col[i][j + 1][1] - col[i][0][1]]
                right = [col[i][n][0] - col[i][j - 1][0], col[i][n][1] - col[i][j - 1][1]]
                up = [row[i + 1][j][0] - row[0][j][0], row[i + 1][j][1] - row[0][j][1]]
                down = [row[m][j][0] - row[i - 1][j][0], row[m][j][1] - row[i - 1][j][1]]
                lu = min(left[0] + up[0], left[1] + up[1])
                ld = min(left[0] + down[0], left[1] + down[1])
                ru = min(right[0] + up[0], right[1] + up[1])
                rd = min(right[0] + down[0], right[1] + down[1])
                res = max(res, lu, ld, ru, rd)
        return res


s = Solution()
print(1)
print(s.maxTrailingZeros(
    # [[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]
    [[5, 2], [4, 10]]
))
