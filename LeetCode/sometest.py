# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2021-12-27 23:46
"""


#
# def mostCommonWord(paragraph: str, banned: List[str]) -> str:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
#         nums = []
#
#         def dfs(root: Optional[TreeNode]) -> None:
#             if not root:
#                 return
#             nums.append(root.val)
#             dfs(root.left)
#             dfs(root.right)
#
#         dfs(root)
#         nums.sort()
#         ans = 0
#         for type, x, y in ops[::-1]:
#             if type == 1:
#                 i = bisect.bisect_left(nums, x)
#                 j = bisect.bisect(nums, y)
#                 if i > j:
#                     continue
#                 ans += j - i
#                 nums[i:j] = []
#         return ans
#
#
# s = Solution()
# a1 = TreeNode(2)
# a2 = TreeNode(3)
# a3 = TreeNode(4)
# a4 = TreeNode(5)
# a1.left = a2
# a1.right = a3
# a3.right = a4
# print(s.getNumber(a1, [[1, 2, 3]]))

l = [1, 2]
m = [3, 5]
print(zip(l, m))
