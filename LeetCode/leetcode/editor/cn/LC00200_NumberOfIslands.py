"""
  200 - 岛屿数量
  
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2204 👎 0

  2023-06-18 21:08:56
"""
from typing import *

TEST_CASE = """
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fu = FindUnion(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i > 0 and grid[i - 1][j] == 1:
                        fu.union((i - 1) * n + j, i * n + j)
                    if j > 0 and grid[i][j - 1] == 1:
                        fu.union(i * n + j - 1, i * n + j)
        cnt = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt.add(fu.find(i * n + j))
        return len(cnt)


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
