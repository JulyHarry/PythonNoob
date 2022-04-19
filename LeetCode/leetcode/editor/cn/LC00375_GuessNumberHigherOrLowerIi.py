# -*- coding: utf-8 -*- 
"""
Description:  LC00375 - 猜数字大小 II
URL:          https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/
Creator:      HarryUp
Create time:  2022-01-04 23:03:11
Content:
# 我们正在玩一个猜数游戏，游戏规则如下： 
# 
#  
#  我从 1 到 n 之间选择一个数字。 
#  你来猜我选了哪个数字。 
#  如果你猜到正确的数字，就会 赢得游戏 。 
#  如果你猜错了，那么我会告诉你，我选的数字比你的 更大或者更小 ，并且你需要继续猜数。 
#  每当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。如果你花光了钱，就会 输掉游戏 。 
#  
# 
#  给你一个特定的数字 n ，返回能够 确保你获胜 的最小现金数，不管我选择那个数字 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：16
# 解释：制胜策略如下：
# - 数字范围是 [1,10] 。你先猜测数字为 7 。
#     - 如果这是我选中的数字，你的总费用为 $0 。否则，你需要支付 $7 。
#     - 如果我的数字更大，则下一步需要猜测的数字范围是 [8,10] 。你可以猜测数字为 9 。
#         - 如果这是我选中的数字，你的总费用为 $7 。否则，你需要支付 $9 。
#         - 如果我的数字更大，那么这个数字一定是 10 。你猜测数字为 10 并赢得游戏，总费用为 $7 + $9 = $16 。
#         - 如果我的数字更小，那么这个数字一定是 8 。你猜测数字为 8 并赢得游戏，总费用为 $7 + $9 = $16 。
#     - 如果我的数字更小，则下一步需要猜测的数字范围是 [1,6] 。你可以猜测数字为 3 。
#         - 如果这是我选中的数字，你的总费用为 $7 。否则，你需要支付 $3 。
#         - 如果我的数字更大，则下一步需要猜测的数字范围是 [4,6] 。你可以猜测数字为 5 。
#             - 如果这是我选中的数字，你的总费用为 $7 + $3 = $10 。否则，你需要支付 $5 。
#             - 如果我的数字更大，那么这个数字一定是 6 。你猜测数字为 6 并赢得游戏，总费用为 $7 + $3 + $5 = $15 。
#             - 如果我的数字更小，那么这个数字一定是 4 。你猜测数字为 4 并赢得游戏，总费用为 $7 + $3 + $5 = $15 。
#         - 如果我的数字更小，则下一步需要猜测的数字范围是 [1,2] 。你可以猜测数字为 1 。
#             - 如果这是我选中的数字，你的总费用为 $7 + $3 = $10 。否则，你需要支付 $1 。
#             - 如果我的数字更大，那么这个数字一定是 2 。你猜测数字为 2 并赢得游戏，总费用为 $7 + $3 + $1 = $11 。
# 在最糟糕的情况下，你需要支付 $16 。因此，你只需要 $16 就可以确保自己赢得游戏。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：0
# 解释：只有一个可能的数字，所以你可以直接猜 1 并赢得游戏，无需支付任何费用。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 2
# 输出：1
# 解释：有两个可能的数字 1 和 2 。
# - 你可以先猜 1 。
#     - 如果这是我选中的数字，你的总费用为 $0 。否则，你需要支付 $1 。
#     - 如果我的数字更大，那么这个数字一定是 2 。你猜测数字为 2 并赢得游戏，总费用为 $1 。
# 最糟糕的情况下，你需要支付 $1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 200 
#  
#  Related Topics 数学 动态规划 博弈 👍 452 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0
            elif dp[i][j] != 0:
                return dp[i][j]
            else:
                dp[i][j] = 0x3f3f3f3f
                for k in range(i, j + 1):
                    dp[i][j] = min(max(dfs(i, k - 1), dfs(k + 1, j)) + k, dp[i][j])
                return dp[i][j]

        dfs(1, n)
        return dp[1][n]


# leetcode submit region end(Prohibit modification and deletion)

def getMoneyAmount2(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        for j in range(i + 1, n + 1):
            dp[i][j] = 0x3f3f3f3f
            for k in range(i, j + 1):
                dp[i][j] = min(dp[i][j], max(dp[i][k - 1], dp[k + 1 if k + 1 <= n else n][j]) + k)
    return dp[1][n]


def getMoneyAmount3(self, n):
    """
    :type n: int
    :rtype: int
    """

    f = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
    return f[1][n]


s = Solution()
print(s.getMoneyAmount(200))