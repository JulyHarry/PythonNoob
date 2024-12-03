"""
ID  : 1  two-sum
DATE: 2024-12-03 10:06:48
"""
from typing import List

"""
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. 

 You may assume that each input would have exactly one solution, and you may 
not use the same element twice. 

 You can return the answer in any order. 

 
 Example 1: 

 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 

 Example 2: 

 
Input: nums = [3,2,4], target = 6
Output: [1,2]
 

 Example 3: 

 
Input: nums = [3,3], target = 6
Output: [0,1]
 

 
 Constraints: 

 
 2 <= nums.length <= 10⁴ 
 -10⁹ <= nums[i] <= 10⁹ 
 -10⁹ <= target <= 10⁹ 
 Only one valid answer exists. 
 

 
Follow-up: Can you come up with an algorithm that is less than 
O(n²)
 time complexity?

 Related Topics 数组 哈希表 👍 19118 👎 0

"""

TEST_CASE = """
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(len(nums)):
            if target - nums[i] in m.keys():
                return [i, m[target - nums[i]]]
            m[nums[i]] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)
