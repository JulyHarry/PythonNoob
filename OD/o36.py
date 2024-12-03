from collections import deque, defaultdict

nodes = eval(input())


class node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


d = {(0, 0): node(-1)}
h = defaultdict(int)
for i, (x, y) in enumerate(nodes):
    c = node(i)
    if not d[(x, y)].l:
        d[(x, y)].l = c
    elif not d[(x, y)].r:
        d[(x, y)].r = c
    else:
        continue
    d[(x + 1, h[x + 1])] = c
    h[x + 1] += 1

root = d[(0, 0)]
q = deque([root])
ans = []
while q:
    node = q.popleft()
    if node:
        ans.append(str(node.v))
        q.append(node.l)
        q.append(node.r)
    else:
        ans.append('null')
j = len(ans) - 1
for i in range(len(ans) - 1, -1, -1):
    if ans[i] != 'null':
        j = i
        break
print(' '.join(ans[:j + 1]))
