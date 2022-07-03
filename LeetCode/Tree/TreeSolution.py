from typing import Optional

from LeetCode.Utils.TreeUtils import tree_build, TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def add(root: TreeNode, val: int):
            nonlocal res
            if root.left is None and root.right is None:
                res += 2 * val + root.val
                print(val)
                return
            if root.left is not None:
                add(root.left, val * 2 + root.val)
            if root.right is not None:
                add(root.right, val * 2 + root.val)

        add(root, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    root = tree_build('[1,0,1,0,1,0,1,0,null,1]')
    print(s.sumRootToLeaf(root))
