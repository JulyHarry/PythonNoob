"""
  1254 - 统计封闭岛屿的数目
  
# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。 
# 
#  请返回 封闭岛屿 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,
# 0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 230 👎 0

  2023-06-18 19:35:45
"""
from collections import deque
from typing import *

TEST_CASE = """
[[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
"""


# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fu = FindUnion(m * n)
        for x in range(m):
            if grid[x][0] == 0:
                fu.union(0, x * n)
            if grid[x][n - 1] == 0:
                fu.union(0, x * n + n - 1)
        for x in range(n):
            if grid[0][x] == 0:
                fu.union(0, x)
            if grid[m - 1][x] == 0:
                fu.union(0, n * (m - 1) + x)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0 and grid[i - 1][j] == 0:
                        fu.union((i - 1) * n + j, i * n + j)
                    if j > 0 and grid[i][j - 1] == 0:
                        fu.union(i * n + j - 1, i * n + j)
        cnt = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt.add(fu.find(i * n + j))
        res = len(cnt)
        if fu.find(0) in cnt:
            res -= 1
        return res

    def closedIsland2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q = deque([(i, j)])
                    closed = True
                    while q:
                        x, y = q.popleft()
                        grid[x][y] = 1
                        if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                            closed = False
                        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                                q.append((nx, ny))
                    if closed:
                        cnt += 1
        return cnt


class FindUnion:
    def __init__(self, n):
        self.cnt = n
        self.root = [i for i in range(n)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(self.root[x])
        ry = self.find(self.root[y])
        if rx != ry:
            self.root[rx] = ry
            self.cnt -= 1

    def count(self):
        return self.cnt

# leetcode submit region end(Prohibit modification and deletion)
