"""
  1027 - 最长等差数列
  
# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。 
# 
#  回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... <
#  ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么
# 序列 seq 是等差的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,6,9,12]
# 输出：4
# 解释： 
# 整个数组是公差为 3 的等差数列。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [9,4,7,2,10]
# 输出：3
# 解释：
# 最长的等差子序列是 [4,7,10]。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [20,1,15,3,10,5,8]
# 输出：4
# 解释：
# 最长的等差子序列是 [20,15,10,5]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 1000 
#  0 <= nums[i] <= 500 
#  
# 
#  Related Topics 数组 哈希表 二分查找 动态规划 👍 301 👎 0

  2023-04-22 23:10:59
"""
from functools import cache
from typing import *

TEST_CASE = """
[9,4,7,2,10]
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestArithSeqLength(self, a: List[int]) -> int:
        @cache
        def dfs(i: int) -> dict[int, int]:
            max_len = {}
            for j in range(i - 1, -1, -1):
                d = a[i] - a[j]  # 公差
                if d not in max_len:
                    max_len[d] = dfs(j).get(d, 1) + 1
            return max_len

        return max(max(dfs(i).values()) for i in range(1, len(a)))


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().longestArithSeqLength([0, 2, 1, 4]))
