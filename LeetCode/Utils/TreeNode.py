from typing import List

from LeetCode.Tree import TreeNode


def tree_build(treelist) -> TreeNode:
    if len(treelist) == 0:
        return None
    root = None
    list = treelist
    if isinstance(treelist, str):
        list = treelist[1:-1].replace(' ', '').split(',')
        try:
            root = TreeNode(int(list[0]))
        except:
            print('格式不正确, 当前值为: %s' % list[0])
    else:
        root = TreeNode(list[0])
    tree_generate(root, 0, len(list), list)
    return root


def tree_generate(root: TreeNode, i: int, n: int, treelist: List):
    left = 2 * i + 1
    if left < n and treelist[left] != 'null':
        try:
            root.left = TreeNode(int(treelist[left]))
        except:
            print('格式不正确, 当前值为: %s' % treelist[left])
        tree_generate(root.left, left, n, treelist)
    if left + 1 < n and treelist[left + 1] != 'null':
        try:
            root.right = TreeNode(int(treelist[left + 1]))
        except:
            print('格式不正确, 当前值为: %s' % treelist[left + 1])
        tree_generate(root.right, left + 1, n, treelist)


def tree_pretraversal(root: TreeNode) -> None:
    res = []

    def pre_traversal_dfs(root: TreeNode):
        nonlocal res
        if root is not None:
            res.append(root.val)
            pre_traversal_dfs(root.left)
            pre_traversal_dfs(root.right)

    pre_traversal_dfs(root)
    print(res)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# if __name__ == '__main__':
#     nums = [1, 0, 1, 0, 1, 0, 1, 2, 'null', 3]
#     nums1 = '[1, 0, 1, 0, 1, 0, 1, 2, null, 3]'
#     root = tree_build(nums)
#     tree_pretraversal(root)
#     root = tree_build(nums1)
#     tree_pretraversal(root)
