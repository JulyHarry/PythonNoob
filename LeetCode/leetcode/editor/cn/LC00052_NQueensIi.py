"""
ID  : n-queens-ii
DATE: 
"""
from LeetCode.test.timer_wrapper import timer

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other. 

 Given an integer n, return the number of distinct solutions to the n-queens 
puzzle. 

 
 Example 1: 
 
 
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
 

 Example 2: 

 
Input: n = 1
Output: 1
 

 
 Constraints: 

 
 1 <= n <= 9 
 

 Related Topics 回溯 👍 539 👎 0

"""

TEST_CASE = """
15
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        digs = [False] * (2 * n - 1)
        anti_digs = digs[:]
        ans = 0

        def dfs(m):
            if m == n:
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                if not (cols[j] or digs[x := m + j] or anti_digs[y := m - j + n - 1]):
                    cols[j] = True
                    digs[x] = True
                    anti_digs[y] = True
                    dfs(m + 1)
                    cols[j] = False
                    digs[x] = False
                    anti_digs[y] = False

        dfs(0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
