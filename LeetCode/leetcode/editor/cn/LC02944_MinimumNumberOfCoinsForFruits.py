# 你在一个水果超市里，货架上摆满了玲琅满目的奇珍异果。 
# 
#  给你一个下标从 1 开始的数组 prices ，其中 prices[i] 表示你购买第 i 个水果需要花费的金币数目。 
# 
#  水果超市有如下促销活动： 
# 
#  
#  如果你花费 price[i] 购买了水果 i ，那么接下来的 i 个水果你都可以免费获得。 
#  
# 
#  注意 ，即使你 可以 免费获得水果 j ，你仍然可以花费 prices[j] 个金币去购买它以便能免费获得接下来的 j 个水果。 
# 
#  请你返回获得所有水果所需要的 最少 金币数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：prices = [3,1,2]
# 输出：4
# 解释：你可以按如下方法获得所有水果：
# - 花 3 个金币购买水果 1 ，然后免费获得水果 2 。
# - 花 1 个金币购买水果 2 ，然后免费获得水果 3 。
# - 免费获得水果 3 。
# 注意，虽然你可以免费获得水果 2 ，但你还是花 1 个金币去购买它，因为这样的总花费最少。
# 购买所有水果需要最少花费 4 个金币。
#  
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,10,1,1]
# 输出：2
# 解释：你可以按如下方法获得所有水果：
# - 花 1 个金币购买水果 1 ，然后免费获得水果 2 。
# - 免费获得水果 2 。
# - 花 1 个金币购买水果 3 ，然后免费获得水果 4 。
# - 免费获得水果 4 。
# 购买所有水果需要最少花费 2 个金币。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 1000 
#  1 <= prices[i] <= 10⁵ 
#  
# 
#  Related Topics 队列 数组 动态规划 单调队列 堆（优先队列） 👍 16 👎 0


from typing import *

TEST_CASE = """
[3,1,2]
[1,10,1,1]
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        f = [float('inf')] * n
        f[0] = 0
        for i, p in enumerate(prices):
            for j in range(1, min(i+1, n-i)):
                f[i+j] = min(f[i+j], f[i]+prices[i])
        return f[-1]


# leetcode submit region end(Prohibit modification and deletion)
