# -*- coding: utf-8 -*- 
"""
Description:  LC00846 - 一手顺子
URL:          https://leetcode-cn.com/problems/hand-of-straights/
Creator:      HarryUp
Create time:  2021-12-30 22:40:13
Content:
# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。 
# 
#  给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，
# 返回 false 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# 输出：true
# 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 
# 
#  示例 2： 
# 
#  
# 输入：hand = [1,2,3,4,5], groupSize = 4
# 输出：false
# 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hand.length <= 10⁴ 
#  0 <= hand[i] <= 10⁹ 
#  1 <= groupSize <= hand.length 
#  
# 
#  
# 
#  注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-
# consecutive-numbers/ 
#  Related Topics 贪心 数组 哈希表 排序 👍 195 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        cnt = collections.defaultdict(int)
        res = 0
        hand.sort()
        for i in range(n):
            cnt[hand[i]] += 1
        for i in sorted(cnt.keys()):
            cur = cnt[i]
            if cnt[i]:
                for j in range(i, i + groupSize):
                    if cnt[j] < cur:
                        return False
                    cnt[j] -= cur
        return True


# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(s.isNStraightHand(hand, groupSize))
