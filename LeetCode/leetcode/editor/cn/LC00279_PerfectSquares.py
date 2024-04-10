"""
  279 - 完全平方数
  
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  
# 
#  Related Topics 广度优先搜索 数学 动态规划 👍 1561 👎 0

  2022-12-24 20:23:03
"""
import math
from typing import *

TEST_CASE = """
4
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[0] = 1
        for j in range(1, n + 1):
            for i in range():
                if j >= sq[i] * sq[i]:
                    dp[j] = min(dp[j], dp[j - sq[i] * sq[i]] + 1)
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1]; // 默认初始化值都为0
        for (int i = 1; i <= n; i++) {
            dp[i] = i; // 最坏的情况就是每次+1
            for (int j = 1; i - j * j >= 0; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1); // 动态转移方程
            }
        }
        return dp[n];
    }
}
