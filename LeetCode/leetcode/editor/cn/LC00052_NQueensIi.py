"""
  52 - N 皇后 II
  
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
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
#  Related Topics 回溯 👍 413 👎 0

  2023-02-18 19:30:55
"""

TEST_CASE = """
4
5
6
7
8
9
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        col, dig, ndig = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
        ans = 0

        def dfs(x):
            if x == n:
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                if col[j] or dig[x + j] or ndig[n + x - j - 1]:
                    continue
                col[j] = True
                dig[x + j] = True
                ndig[n + x - j - 1] = True
                dfs(x + 1)
                col[j] = False
                dig[x + j] = False
                ndig[n + x - j - 1] = False

        dfs(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
