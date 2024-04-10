# 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i 个机器人充电时间
# 为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。 
# 
#  运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes)
#  是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。 
# 
#  请你返回在 不超过 budget 的前提下，你 最多 可以 连续 运行的机器人数目为多少。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
# 输出：3
# 解释：
# 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。
# 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 
# 25 。
# 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
# 输出：0
# 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  chargeTimes.length == runningCosts.length == n 
#  1 <= n <= 5 * 10⁴ 
#  1 <= chargeTimes[i], runningCosts[i] <= 10⁵ 
#  1 <= budget <= 10¹⁵ 
#  
# 
#  Related Topics 队列 数组 二分查找 前缀和 滑动窗口 堆（优先队列） 👍 32 👎 0
from collections import deque
from typing import *

TEST_CASE = """
[3,6,1,3,4]
[2,1,3,4,5]
25
[11,12,19]
[10,8,7]
19
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        l, ans, rc = 0, 0, 0
        q = deque()
        for r, ct in enumerate(chargeTimes):
            while q and ct > chargeTimes[q[-1]]:
                q.pop()
            q.append(r)
            rc += runningCosts[r]
            while q and chargeTimes[q[0]] + (r - l + 1) * rc > budget:
                while q and q[0] <= l:
                    q.popleft()
                rc -= runningCosts[l]
                l += 1
            if q and chargeTimes[q[0]] + (r - l + 1) * rc <= budget:
                ans = max(ans, r - l + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
