import bisect
import math
import sys
from collections import defaultdict
from itertools import accumulate

from LeetCode.test.wrapper import timeit_print, timeit_log

sys.setrecursionlimit(600000)


def a2():
    n, m = sys.stdin.readline().strip().split(' ')
    n, m = int(n), int(m)
    nums = sys.stdin.readline().strip().split(' ')
    nums = list(map(int, nums))
    query = sys.stdin.readline().strip().split(' ')
    query = list(map(int, query))
    ans = [0] * m

    def find(x):
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= x:
                r = m
            else:
                l = m + 1
        return l + 1 if nums[l] == x else -1

    for i, q in enumerate(query):
        ans[i] = find(q)

    print(' '.join(map(str, ans)))


def a3():
    n, m = sys.stdin.readline().strip().split(' ')
    n, c = int(n), int(m)
    nums = list(map(int, sys.stdin.readline().strip().split(' ')))
    nums.sort()
    ans = 0
    for num in nums:
        ans += bisect.bisect_right(nums, num - c) - bisect.bisect_left(nums, num - c)
    print(ans)


def a4():
    n = int(input())
    xmx, xmn = -math.inf, math.inf
    ymx, ymn = -math.inf, math.inf
    for _ in range(n):
        x, y = map(int, input().split(' '))
        xmx = max(xmx, x + y)
        xmn = min(xmn, x + y)
        ymx = max(ymx, y - x)
        ymn = min(ymn, y - x)
    print(max(xmx - xmn, ymx - ymn))


def a5():
    n = int(input())
    ans = math.inf
    xl, yl, p = [], [], []
    for _ in range(n):
        x, y = map(int, input().split())
        p.append((x + y, x - y))
        xl.append(x + y)
        yl.append(x - y)
    xl.sort()
    yl.sort()
    prex = list(accumulate(xl, initial=0))
    prey = list(accumulate(yl, initial=0))
    for x, y in p:
        kx = bisect.bisect_left(xl, x)
        ky = bisect.bisect_left(yl, y)
        sx = prex[n] - 2 * prex[kx] + (2 * kx - n) * x
        sy = prey[n] - 2 * prey[ky] + (2 * ky - n) * y
        ans = min(ans, sx + sy)
    print(ans // 2)


@timeit_log
def p3379_file():
    with open('/Users/hang/Downloads/P3379_1.in', 'r') as fr, open('test.out', 'w') as fw:
        n, m, root = map(int, fr.readline().split(' '))
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            x, y = map(int, fr.readline().split(' '))
            g[x].append(y)
            g[y].append(x)
        h = n.bit_length()
        pa = [[-1] * h for _ in range(n + 1)]
        depth = [0] * (n + 1)

        @timeit_log
        def build_tree(x, fa, d):
            pa[x][0] = fa
            depth[x] = d
            for y in g[x]:
                if y != fa:
                    build_tree(y, x, d + 1)

        build_tree(root, -1, 0)

        for j in range(h - 1):
            for i in range(n + 1):
                if (p := pa[i][j]) != -1:
                    pa[i][j + 1] = pa[p][j]

        def get_kth_ancestor(node, k):
            while k and node != -1:
                lb = k & (-k)
                node = pa[node][lb.bit_length() - 1]
                k ^= lb
            return node

        for _ in range(m):
            x, y = map(int, fr.readline().split(' '))
            if depth[x] < depth[y]:
                x, y = y, x
            x = get_kth_ancestor(x, depth[x] - depth[y])
            if x == y:
                # print(x)
                fw.write(str(x) + '\n')
            else:
                for i in range(h - 1, -1, -1):
                    p, q = pa[x][i], pa[y][i]
                    if p != q:
                        x, y = p, q
                # print(pa[x][0])
                fw.write(str(pa[x][0]) + '\n')


def p3379():
    n, m, root = map(int, input().split(' '))
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, input().split(' '))
        g[x].append(y)
        g[y].append(x)
    h = n.bit_length()
    pa = [[-1] * h for _ in range(n + 1)]
    depth = [0] * (n + 1)

    @timeit_print
    def build_tree(x, fa, d):
        pa[x][0] = fa
        depth[x] = d
        for y in g[x]:
            if y != fa:
                build_tree(y, x, d + 1)

    build_tree(root, -1, 0)

    for j in range(h - 1):
        for i in range(n + 1):
            if (p := pa[i][j]) != -1:
                pa[i][j + 1] = pa[p][j]

    def get_kth_ancestor(node, k):
        while k and node != -1:
            lb = k & (-k)
            node = pa[node][lb.bit_length() - 1]
            k ^= lb
        return node

    for _ in range(m):
        x, y = map(int, input().split(' '))
        if depth[x] < depth[y]:
            x, y = y, x
        x = get_kth_ancestor(x, depth[x] - depth[y])
        if x == y:
            print(x)
        else:
            for i in range(h - 1, -1, -1):
                p, q = pa[x][i], pa[y][i]
                if p != q:
                    x, y = p, q
            print(pa[x][0])


if __name__ == '__main__':
    p3379_file()
