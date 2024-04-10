"""
  51 - N 皇后
  
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。 
# 
#  n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 数组 回溯 👍 1642 👎 0

  2023-02-18 20:39:47
"""
from typing import *

TEST_CASE = """
4
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, dig, ndig = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
        ans = []
        cur = []

        def dfs(x):
            if x == n:
                res = [['.'] * n for _ in range(n)]
                for p, q in cur:
                    res[p][q] = 'Q'
                res1 = []
                for r in res:
                    res1.append(''.join(r))
                ans.append(res1)
                return
            for j in range(n):
                if col[j] or dig[x + j] or ndig[n + x - j - 1]:
                    continue
                col[j] = True
                dig[x + j] = True
                ndig[n + x - j - 1] = True
                cur.append([x, j])
                dfs(x + 1)
                col[j] = False
                dig[x + j] = False
                ndig[n + x - j - 1] = False
                cur.pop(-1)

        dfs(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
