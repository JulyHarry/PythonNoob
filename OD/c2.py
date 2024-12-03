io = list(map(int, input().split()))
po = list(map(int, input().split()))
n = len(po)


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def build(p, i):
    if len(p) == 0:
        return None
    root = TreeNode(p[0])
    m = i.index(p[0])
    root.left = build(p[1:m + 1], i[:m])
    root.right = build(p[m + 1:], i[m + 1:])
    return root


root = build(po, io)
ans = []


def dfs(root):
    # ans.append(root.val)
    if root.left:
        dfs(root.left)
    ans.append(root.val)
    if root.right:
        dfs(root.right)


def rebuild(root):
    if root is None:
        return 0
    x = root.val
    root.val = rebuild(root.left) + rebuild(root.right)
    return root.val + x


rebuild(root)
dfs(root)
print(' '.join(map(str, ans)))
