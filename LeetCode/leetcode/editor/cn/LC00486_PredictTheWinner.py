# -*- coding: utf-8 -*- 
"""
Description:  LC00486 - 预测赢家
URL:          https://leetcode-cn.com/problems/predict-the-winner/
Creator:      HarryUp
Create time:  2022-01-04 22:13:14
Content:
# 给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。 
# 
#  玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。每一回合，玩家从数组的任意一端取一个数字（即，nums[0
# ] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取
# 时，游戏结束。 
# 
#  如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。你可以假设每个玩家的玩法都会使他的分
# 数最大化。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,2]
# 输出：false
# 解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）
# 可选。 
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 false 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,5,233,7]
# 输出：true
# 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
# 最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 10⁷ 
#  
#  Related Topics 递归 数组 数学 动态规划 博弈 👍 511 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        print(dp)
        return dp[0][n - 1] > 0


# leetcode submit region end(Prohibit modification and deletion)

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = nums[i]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                l = nums[i] + dp[i + 1][j][1]
                r = nums[j] + dp[i][j - 1][1]
                if l >= r:
                    dp[i][j][0] = l
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = r
                    dp[i][j][1] = dp[i][j - 1][0]
        print(dp)
        return dp[0][n - 1][0] >= dp[0][n - 1][1]


s = Solution()
nums = [3,9,1,2]
print(s.PredictTheWinner(nums))
