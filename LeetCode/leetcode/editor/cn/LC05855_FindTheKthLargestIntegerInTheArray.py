# -*- coding: utf-8 -*- 
"""
Description:  LC05855 - 找出数组中的第 K 大整数
URL:          https://leetcode-cn.com/problems/find-the-kth-largest-integer-in-the-array/
Creator:      HarryUp
Create time:  2021-08-30 21:24:32
Content:
# 给你一个字符串数组 nums 和一个整数 k 。nums 中的每个字符串都表示一个不含前导零的整数。
#
#  返回 nums 中表示第 k 大整数的字符串。
#
#  注意：重复的数字在统计时会视为不同元素考虑。例如，如果 nums 是 ["1","2","2"]，那么 "2" 是最大的整数，"2" 是第二大的整数，"1
# " 是第三大的整数。
#
#
#
#  示例 1：
#
#
# 输入：nums = ["3","6","7","10"], k = 4
# 输出："3"
# 解释：
# nums 中的数字按非递减顺序排列为 ["3","6","7","10"]
# 其中第 4 大整数是 "3"
#
#
#  示例 2：
#
#
# 输入：nums = ["2","21","12","1"], k = 3
# 输出："2"
# 解释：
# nums 中的数字按非递减顺序排列为 ["1","2","12","21"]
# 其中第 3 大整数是 "2"
#
#
#  示例 3：
#
#
# 输入：nums = ["0","0"], k = 2
# 输出："0"
# 解释：
# nums 中的数字按非递减顺序排列为 ["0","0"]
# 其中第 2 大整数是 "0"
#
#
#
#
#  提示：
#
#
#  1 <= k <= nums.length <= 10⁴
#  1 <= nums[i].length <= 100
#  nums[i] 仅由数字组成
#  nums[i] 不含任何前导零
#
#  👍 7 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        自带方法
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=int, reverse=True)
        return nums[k - 1]

    # leetcode submit region end(Prohibit modification and deletion)
    # class MyCmp(str):
    #     def __lt__(o1, o2):
    #         if len(o1) == len(o2):
    #             for i in range(len(o1)):
    #                 if o1[i] != o2[i]:
    #                     return o1[i] < o2[i]
    #         else:
    #             return len(o1) < len(o2)
    # class my_cmp(str):
    #     def __lt__(a, b):
    #         if len(a) != len(b):
    #             return len(a) < len(b)
    #         else:
    #             for i in range(len(a)):
    #                 if a[i] != b[i]:
    #                     return a[i] < b[i]
    #
    #     def kthLargestNumber(self, nums: List[str], k: int) -> str:
    #         nums.sort(key=my_cmp, reverse=True)

    def kthLargestNumber2(self, nums, k):
        """
        自带方法
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=int)
        return nums[-k]

    def kthLargestNumber3(self, nums, k):
        """
        lamada函数
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        arrs = [int(n) for n in nums]
        return sorted(arrs)[-k]

    def kthLargestNumber4(self, nums, k):
        """
        自定义key
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=MyCmp)
        return nums[-k]


class MyCmp(str):
    def __lt__(o1, o2):
        if len(o1) == len(o2):
            for i in range(len(o1)):
                if o1[i] != o2[i]:
                    return o1[i] < o2[i]
        else:
            return len(o1) < len(o2)


s = Solution()
nums = ["1", "12", "3", "322", "111"]
print(s.kthLargestNumber4(nums, 2))
