from LeetCode.test.wrapper import timer

nums = list(map(int, input().split()))


@timer
def get_results():
    ans = []
    path = []
    s = set()

    def dfs(i):
        if i >= 6:
            x1 = path[0] * path[1] * path[2]
            x2 = path[3] * path[4] * path[5]
            if x1 != x2:
                return
        if i == 9:
            x1 = path[0] * path[1] * path[2]
            x2 = path[3] * path[4] * path[5]
            x3 = path[6] * path[7] * path[8]
            y1 = path[0] * path[3] * path[6]
            y2 = path[1] * path[4] * path[7]
            y3 = path[2] * path[5] * path[8]
            d1 = path[0] * path[4] * path[8]
            d2 = path[2] * path[4] * path[6]
            if x1 == x2 == x3 == y1 == y2 == y3 == d1 == d2:
                ans.append(path.copy())
            return
        for n in nums:
            if n not in s:
                path.append(n)
                s.add(n)
                dfs(i + 1)
                path.pop()
                s.remove(n)

    dfs(0)
    ans.sort()
    return ans


for a in get_results():
    print(a)
