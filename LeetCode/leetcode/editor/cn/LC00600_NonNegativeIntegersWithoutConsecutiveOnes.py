"""
  600 - 不含连续1的非负整数
  
# 给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 5
# 输出: 5
# 解释: 
# 下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。 
# 
#  示例 2: 
# 
#  
# 输入: n = 1
# 输出: 2
#  
# 
#  示例 3: 
# 
#  
# 输入: n = 2
# 输出: 3
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= n <= 10⁹ 
#  
# 
#  Related Topics 动态规划 👍 312 👎 0

  2023-03-21 20:34:52
"""
from functools import cache

TEST_CASE = """
3
234
88888
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]

        @cache
        def dfs(i, isnum, hasone):
            if i == len(s):
                return 1
            res = 0
            up = int(s[i]) if isnum else 1
            for x in range(up + 1):
                if x == 0:
                    res += dfs(i + 1, isnum and x == up, False)
                elif not hasone:
                    res += dfs(i + 1, isnum and x == up, x == 1)
            return res

        return dfs(0, True, False)

# leetcode submit region end(Prohibit modification and deletion)
