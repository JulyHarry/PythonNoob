# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import re
from collections import defaultdict, Counter, deque
import time
from functools import cache, lru_cache
from itertools import accumulate
from math import isqrt, inf
from typing import List

from _heapq import *
from sortedcontainers import SortedList

from LeetCode.test.wrapper import timer_log


def lastNonEmptyString(s: str) -> str:
    d = Counter(s)
    mx = max(v for _, v in d.items())
    l = []
    for k, v in d.items():
        if v == mx:
            l.append(k)
    ans = ''
    for x in s[::-1]:
        if x in l and x not in ans:
            ans += x
    return ans


"""
f[0][4] = max(f[0][1] + f[2][4]
f[i][j] = 
"""


class Trie2:
    def __init__(self):
        self.children = [None] * 26
        self.children2 = [None] * 26

    def searchfix(self, prefix) -> int:
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return False
            node = node.children[ch]
        for ch in prefix[::-1]:
            ch = ord(ch) - ord("a")
            if not node.children2[ch]:
                return False
            node = node.children2[ch]
        return True

    def insert(self, word) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        for ch in word[::-1]:
            ch = ord(ch) - ord("a")
            if not node.children2[ch]:
                node.children2[ch] = Trie()
            node = node.children2[ch]
        print(word)


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j, k):
            if i >= j or i < 0 or j >= len(nums):
                return 1
            ans = 1
            if i + 1 <= j and nums[i + 1] + nums[i] == k:
                ans = max(ans, dfs(i + 2, j, k) + 1)
            if j - 1 >= i and nums[j - 1] + nums[j] == k:
                ans = max(ans, dfs(i, j - 2, k) + 1)
            if nums[i] + nums[j] == k:
                ans = max(ans, dfs(i + 1, j - 1, k) + 1)
            return ans

        n = len(nums)
        ans = max(dfs(2, n - 1, nums[0] + nums[1]), dfs(0, n - 3, nums[-1] + nums[-2]),
                  dfs(1, n - 2, nums[0] + nums[-1]))
        return ans

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        @cache
        def maxpre(s1, s2):
            s1, s2 = str(s1), str(s2)
            cnt = 0
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    cnt += 1
                else:
                    break
            return cnt

        ans = 0
        for a in arr1:
            for b in arr2:
                ans = max(ans, maxpre(a, b))

        return ans

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        s = defaultdict(int)
        m = len(mat)
        n = len(mat[0])
        dirc = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def traversal(i, j, d, res):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            res += str(mat[i][j])
            if len(res) > 1 and int(res) % 2 != 0:
                s[res] += 1
            traversal(i + d[0], j + d[1], d, res)

        def check(k):
            if k == 1: return False
            for i in range(2, int(k ** 0.5) + 1):
                if k % i == 0:
                    return False
            return True

        for i in range(m):
            for j in range(n):
                for d in dirc:
                    traversal(i, j, d, '')

        hp = [(-v, k) for k, v in s.items()]
        heapq.heapify(hp)
        mx = 0
        ans = -1
        while hp:
            if mx != 0 and hp[0][0] != mx:
                break
            v, k = heapq.heappop(hp)
            if check(int(k)):
                mx = v
                ans = max(ans, int(k))
        return ans

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a = set(arr1)
        b = set(arr2)
        if len(a) > len(b):
            build, query = b, a
        else:
            build, query = a, b
        t = Trie()
        for x in build:
            t.insert(x)
        ans = 0
        for y in query:
            ans = max(ans, t.searchPrefix(y))
        return ans

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans, n = 0, len(words)
        t = Trie()
        for i in range(n):
            t.insert(words[i])
            for j in range(i):
                if t.searchfix(words[j]):
                    ans += 1
        return ans

    def test_bisect(self, nums, a, lo, hi):
        x = bisect.bisect_left(nums, a, lo, hi)
        return x

    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        cnt = 0
        while nums[0] < k:
            f, s = heappop(nums), heappop(nums)
            a = 2 * min(f, s) + max(f, s)
            heappush(nums, a)
            cnt += 1
        return cnt

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, d in edges:
            g[x].append((y, d))
            g[y].append((x, d))

        def dfs(x, fa, l):
            nonlocal cur
            for y, d in g[x]:
                if y != fa:
                    if (l + d) % signalSpeed == 0:
                        cur += 1
                    dfs(y, x, l + d)

        ans = [0] * n
        for x in range(n):
            cnt = 0
            for y, d in g[x]:
                cur = 0
                dfs(y, x, d)
                if d % signalSpeed == 0:
                    cur += 1
                ans[x] += cnt * cur
                cnt += cur

        return ans

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        s = 0
        rd = set()
        for i, n in enumerate(nums):
            s += n
            if n ^ k > n:
                rd.add(i)

        for x, y in edges:
            if x in rd and y in rd:
                s += (nums[x] ^ k) + (nums[y] ^ k) - nums[x] - nums[y]
                rd.remove(x)
                rd.remove(y)
        if not rd:
            return s

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        for r in rd:
            mx = -1
            cur = 0
            for y in g[r]:
                if (nums[r] ^ k) - (nums[y] ^ k) > cur:
                    mx = y
                    cur = (nums[r] ^ k) - (nums[y] ^ k)
            s += cur - nums[mx] - nums[r]
        return s

    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]
        s1, s2 = SortedList([-nums[0]]), SortedList([-nums[1]])
        for i in range(2, len(nums)):
            c = nums[i]
            i1 = s1.bisect_left(-c)
            i2 = s2.bisect_left(-c)
            if i1 > i2:
                a1.append(c)
                s1.add(-c)
            elif i1 < i2:
                a2.append(c)
                s2.add(-c)
            elif i1 == i2 and len(a1) > len(a2):
                a2.append(c)
                s2.add(-c)
            else:
                a1.append(c)
                s1.add(-c)
        return a1 + a2

    def frogPosition(
            self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa, p, t):
            nonlocal ans
            if t < 0:
                return
            if target == x:
                if t == 0 or (t > 0 and len(g[x]) == 1 and fa in g[x]):
                    ans = p
            if fa not in g[x]:
                if len(g[x]) == 0:
                    return
                p = p / len(g[x])
            else:
                if len(g[x]) == 1:
                    return
                p = p / (len(g[x]) - 1)
            for y in g[x]:
                if y != fa:
                    dfs(y, x, p, t - 1)

        if n == 1: return 1
        ans = 0
        dfs(1, -1, 1, t)
        return ans

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa, d, an):
            if len(g[x]) == 1 and ((an, x) not in s or (x, an) not in s):
                ans[d] += 1
                s.add((an, x))
                s.add((x, an))
                return
            for y in g[x]:
                if y != fa:
                    dfs(y, x, d + 1, an)

        s = set()
        for i in range(1, n + 1):
            g[0] = [i]
            g[i].append(0)
            dfs(i, 0, 0, i)
            g[i].pop()

        return ans[1:]

    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = []

        def check(k, s):
            for j, a in enumerate(arr):
                if k != j and s in a:
                    return False
            return True

        for k, a in enumerate(arr):
            m = len(a)
            res = ""
            for i in range(m + 1):
                for j in range(i + 1, m + 1):
                    c = a[i:j]
                    print(c, res)
                    if (not res or c < res) and check(k, c):
                        res = c
                    if res:
                        break
            ans.append(res)

        return ans

    def beautifulPartitions(self, s: str, k: int, m: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        def is_prime(x):
            return x in "2357"

        def can_split(x):
            return x == 0 or x == n or is_prime(s[x]) and not is_prime(s[x - 1])

        if m * k > n or is_prime(s[-1]) or not is_prime(s[0]):
            return 0

        f = [[0] * (n + 1) for _ in range(k + 1)]
        f[0][0] = 1
        for i in range(1, k + 1):
            for j in range(m * i, n - (k - i) * m + 1):
                if can_split(j):
                    for l in range((i - 1) * m, j - m + 1):
                        if can_split(l):
                            f[i][j] += f[i - 1][l]
        return f[k][n] % MOD

    def minimumChanges(self, s: str, k: int) -> int:
        def cal(s):
            m = res = len(s)
            for i in range(1, m):
                if m % i == 0:
                    cnt = 0
                    for j in range(i):
                        q = s[j::i]
                        for l in range(len(q) // 2):
                            cnt += q[l] != q[-l - 1]
                    res = min(res, cnt)
                    if res == 0:
                        return 0
            return res

        n = len(s)
        f = [[inf] * (n + 1) for _ in range(k + 1)]
        f[0][0] = 0
        for i in range(1, k + 1):
            for j in range(i, n - k + i + 1):
                if i == 1:
                    f[i][j] = cal(s[:j])
                else:
                    for l in range(i, j - 1):
                        f[i][j] = min(f[i][j], f[i - 1][l] + cal(s[l:j]))
        return f[k][n]

    def distance(self, nums: List[int]) -> List[int]:
        c = defaultdict(list)
        for i, num in enumerate(nums):
            c[num].append(i)
        ans = [0] * len(nums)
        for s in c.values():
            n = len(s)
            pre = list(accumulate(s, initial=0))
            for i, q in enumerate(s):
                ans[q] = (2 * i - n) * q + pre[n] - 2 * pre[i]
        return ans

    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l = ans = 0
        cnt = defaultdict(int)
        for r in range(n):
            cnt[s[r]] += 1
            while cnt[s[r]] > 2:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

    def minOperations(self, k: int) -> int:
        ans = inf
        for i in range(2, k - 1):
            cnt1 = i - 1
            cnt2 = (k + i - 1) // i
            print(i, cnt1, cnt2)
            ans = min(ans, cnt1 + cnt2)
        return ans

    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # n = len(nums)
        h = []
        cnt = Counter()
        ans = []
        for n, f in zip(nums, freq):
            cnt[n] += f
            heappush(h, (-cnt[n], n))
            while h[0][0] != -cnt[h[0][1]]:
                heappop(h)
            ans.append(-h[0][0])
        return ans
        # sl = SortedList()
        # c = Counter()
        # ans = []
        # for n, f in zip(nums, freq):
        #     if c[n] in sl:
        #         sl.remove(c[n])
        #     c[n] += f
        #     sl.add(c[n])
        #     ans.append(sl[-1])
        # return ans

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tr = Trie()
        ans = []
        mn = 0
        for i, wc in enumerate(wordsContainer):
            tr.insert(wc[::-1], i)
            if len(wc) < len(wordsContainer[mn]):
                mn = i
        for wq in wordsQuery:
            pt = tr.searchPrefix(wq[::-1])
            if len(pt) > 0:
                i = pt[0]
            else:
                i = mn
            for x in pt[1:]:
                if len(wordsContainer[x]) < len(wordsContainer[i]):
                    i = x
            ans.append(i)
        return ans

    @timer_log
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = [0] * 31
        res = l = 0
        ans = inf
        for r, num in enumerate(nums):
            i = 0
            while num > 0:
                if num & 1:
                    cnt[i] += 1
                    if cnt[i] == 1:
                        res += 1 << i
                i += 1
                num >>= 1
            print(cnt)
            while res >= k and l <= r:
                ans = min(ans, r - l + 1)
                num2 = nums[l]
                i = 0
                while num2 > 0:
                    if num2 & 1:
                        cnt[i] -= 1
                        if cnt[i] == 0:
                            res -= 1 << i
                    i += 1
                    num2 >>= 1
                l += 1
        return -1 if ans == inf else ans

    def minimumLevels(self, possible: List[int]) -> int:
        s = sum(2 * p - 1 for p in possible)
        pre = 0
        for i, p in enumerate(possible[:-1]):
            pre += 2 * p - 1
            if pre * 2 > s:
                return i + 1
        return -1

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n)
        f[0] = 1
        for i, num in enumerate(nums[1:], start=1):
            f[i] = 1 + (f[i - 1] if num != nums[i - 1] else 0)
        return sum(f)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        cnt = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        for i in range(1, n):
            if f[i] == f[i - 1]:
                cnt[i] = cnt[i - 1] + 1
            else:
                cnt[i] = cnt[i - 1]
        return cnt[-1]

    def numberOfSpecialChars(self, word: str) -> int:
        s = [0] * 26
        for w in word:
            s[ord(w.lower()) - ord('a')] |= ord(w) - ord(w.lower()) + 1
        ans = 0
        for x in s:
            if x > 25:
                ans += 1
        return ans

    def numberOfSpecialChars1(self, word: str) -> int:
        l = [0] * 26
        u = [0] * 26
        for w in word:
            if ord('a') <= ord(w) <= ord('z'):
                if u[ord(w.upper()) - ord('A')] == 1:
                    l[ord(w) - ord('a')] = 0
                else:
                    l[ord(w) - ord('a')] = 1
            else:
                u[ord(w) - ord('A')] = 1
        ans = 0
        for x, y in zip(l, u):
            if x == y == 1:
                ans += 1
        return ans

    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * 10 for _ in range(n)]
        for j in range(n):
            d = defaultdict(int)
            for i in range(m):
                d[grid[i][j]] += 1
            for k in range(10):
                f[j][k] = m - d[k]

        g = [[inf] * 10 for _ in range(n)]
        g[0] = f[0]
        for i in range(1, n):
            for j in range(10):
                for k in range(10):
                    if j != k:
                        g[i][j] = min(g[i][j], g[i - 1][k] + f[i][k])

        return min(f[-1])

    def findAnswer(self, n, edges):
        graph = [[] for _ in range(n)]
        for i, (u, v, d) in enumerate(edges):
            graph[u].append((v, d, i))
            graph[v].append((u, d, i))

        d = [inf] * n
        d[0] = 0
        pq = [(0, 0)]
        while pq:
            cd, cn = heapq.heappop(pq)
            if cd > d[cn]:
                continue
            for nn, nd, _ in graph[cn]:
                if d[cn] + nd < d[nn]:
                    d[nn] = d[cn] + nd
                    heapq.heappush(pq, (d[nn], nn))

        answer = [False] * len(edges)
        visited = [False] * n

        def dfs(node, dist):
            if node == 0:
                visited[0] = True
                return
            for pn, pd, i in graph[node]:
                if dist - pd == d[pn]:
                    dfs(pn, dist - pd)
                    if visited[pn]:
                        answer[i] = True
                        visited[node] = True

        if d[-1] == inf:
            return answer
        dfs(n - 1, d[n - 1])

        return answer

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cur = []
        ans = []

        def dfs(i, j, m):
            # i: 当前值 j: 个数 m: 开始循环
            if i > n or j > k or m > 10:
                return
            if i == n and j == k:
                ans.append(cur.copy())
                return
            dfs(i, j, m + 1)
            cur.append(m)
            dfs(i + m, j + 1, m + 1)
            cur.pop()

        dfs(0, 0, 1)

        return ans

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1:
            return []
        changed.sort()
        cnt = Counter(changed)
        ans = []
        for i in range(n):
            c = changed[i]
            nw = 2 * c
            if cnt[c] > 0 and cnt[nw] > 0:
                cnt[nw] -= 1
                cnt[c] -= 1
                ans.append(changed[i])
        print(cnt)
        for v in cnt.values():
            if v != 0:
                return []
        return ans

    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            print(s[i])
            ans = dfs(i - 1)
            if i >= 1 and s[i - 1] != 0 and int(s[i - 1: i + 1]) <= 26:
                print(s[i - 1: i + 1])
                ans += dfs(i - 2)
            return ans

        return dfs(len(s) - 1)

    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank > 0:
            ans += mainTank // 5 * 5 * 10
            if mainTank < 5:
                break
            supply = min(additionalTank, mainTank // 5)
            mainTank = mainTank % 5 + supply
            additionalTank -= supply
        return ans

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        x = [[0, 2], [1, 3]]
        y = [[0, 2], [1, 3]]
        for s1, s2 in x:
            for t1, t2 in y:
                cnt1, cnt2 = 0, 0
                for a in grid[s1:s2]:
                    for b in a[t1:t2]:
                        if b == 'B':
                            cnt1 += 1
                        else:
                            cnt2 += 1

                if cnt1 == 3 or cnt2 == 3:
                    return True
        return False

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, j):
            if i == 0 and j == 0:
                return 1
            ans = 0
            for x in range(min(limit, i) + 1):
                for y in range(min(limit, j) + 1):
                    if x + y >= 1:
                        ans += dfs(i - x, j - y) % MOD
            return ans % MOD

        return dfs(one, zero)

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s = Counter(nums1)
        nums2.sort()
        ans = inf
        for a in nums1:
            c = s.copy()
            cur = nums2[0] - a
            flag = True
            for b in nums2:
                if c[b - cur] > 0:
                    c[b - cur] -= 1
                else:
                    flag = False
                    continue
            if flag:
                ans = min(ans, cur)
        return ans

    def minEnd(self, n: int, x: int) -> int:
        m = bin(x)[2:]
        t = bin(n - 1)[2:]
        ans = list(m)
        e = len(t) - 1
        for i in range(len(m) - 1, -1, -1):
            if m[i] == '0' and e >= 0:
                ans[i] = t[e]
                e -= 1
        if e >= 0:
            ans = list(t[:e + 1]) + ans
        return int(''.join(ans), 2)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        f = [[[-inf] * n for _ in range(n)] for _ in range(m)]
        f[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    for s in (-1, 0, 1):
                        p = j + s
                        if p < 0 or p >= n:
                            continue
                        for t in (-1, 0, 1):
                            q = k + t
                            if q < 0 or q >= n:
                                continue
                            v = grid[i][j] if j == k else grid[i][j] + grid[i][k]
                            f[i][j][k] = max(f[i][j][k], f[i - 1][p][q] + v)
        mx = 0
        for x in f[-1]:
            for y in x:
                if y > mx:
                    mx = y
        return mx

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        l = capacity
        i = 0
        while i < len(plants):
            if l < plants[i]:
                ans += 2 * i
                l = capacity
            print(l, i, ans)
            l -= plants[i]
            i += 1
            ans += 1
        return ans

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -math.inf
        for s in range(k):
            x = energy[s::k]
            f = [x[0]] + [-math.inf] * (len(x) - 1)
            for i in range(1, len(x)):
                f[i] = max(f[i - 1] + x[i], x[i])
            ans = max(ans, f[-1])
        return ans

        # for y in range(n):

        # return max(c for r in f for c in r)

    def distributeCandies(self, n: int, limit: int) -> int:
        @cache
        def dfs(i, k):
            if k <= 0 or i > limit * k:
                return 0
            if i <= limit and k == 1:
                return 1
            ans = 0
            for j in range(min(i + 1, limit + 1)):
                ans += dfs(i - j, k - 1)
            return ans

        return dfs(n, 3)

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda a: a[0])
        last = meetings[0][1]
        start = meetings[0][0]
        for i, (x, y) in enumerate(meetings):
            if last < x:
                days -= last - start + 1
                start = x
                last = y
            else:
                last = max(last, y)
        days -= last - start + 1
        return days

    def clearDigits(self, s: str) -> str:
        p = []
        for i, x in enumerate(s):
            if x.isdigit():
                p.pop()
            else:
                p.append(i)
        return ''.join([s[i] for i in p])

    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        cur = 0
        cnt = 0
        i = 1
        while cur < n:
            if skills[i % n] > skills[cur]:
                cur = i
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return cur
            i += 1
        return cur

    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 1

        @cache
        def dfs(i, k):
            ans = 1
            for j in range(i):
                if nums[i] == nums[j]:
                    ans = max(ans, dfs(j, k) + 1)
                elif k >= 1:
                    ans = max(ans, dfs(j, k - 1) + 1)
            nonlocal res
            res = max(res, ans)
            return ans

        for i in range(n):
            dfs(i, k)
        return res


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.st = [[] for _ in range(26)]

    def searchPrefix(self, prefix: int) -> List[int]:
        node = self
        pre = []
        for ch in str(prefix):
            c = ord(ch) - ord("a")
            if not node.children[c]:
                return pre
            pre = node.st[c]
            node = node.children[c]
        return pre

    def insert(self, word: int, i: int) -> None:
        node = self
        for ch in str(word):
            c = ord(ch) - ord("a")
            if not node.children[c]:
                node.children[c] = Trie()
            node.st[c].append(i)
            node = node.children[c]


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        h = math.floor(math.log(n, 2))
        pa = [[p] + [-1] * h for p in parent]
        for i in range(n):
            for j in range(h):
                if (p := pa[i][j]) != -1:
                    pa[i][j + 1] = pa[p][j]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        while k and node != -1:
            lb = k & -k
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb
        return node


class SnapshotArray:

    def __init__(self, length: int):
        self.s = 0
        self.n = [{0: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.n[index][self.s] = val

    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        l = self.find(index, snap_id)
        print(l)
        return self.n[index][l]

    def find(self, index, snapid):
        nums = list(self.n[index].keys())
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] <= snapid:
                l = m
            else:
                r = m - 1
        return nums[l]


if __name__ == '__main__':
    s = Solution()

    # print(s.maxOperations([3, 2, 1, 2, 3, 4]))
    # print(s.maxOperations([3, 2, 6, 1, 4]))
    # print(s.maxOperations([1, 1, 2, 3, 2, 2, 1, 3, 3]))
    # print(s.longestCommonPrefix([3, 26], [7, 26]))
    # print(s.mostFrequentPrime([[1, 1], [9, 9], [1, 1]]))
    # print(s.mostFrequentPrime([[9, 7, 8], [4, 6, 5], [2, 8, 6]]))
    # # print(s.mostFrequentPrime([[7]]))
    # print(s.longestCommonPrefix([1, 10, 100], [1000]))
    # print(s.longestCommonPrefix([1, 10, 100], [1000, 0]))
    # print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    # for i in range(0, 12):
    #     print(i, s.test_bisect([0, 2, 4, 6, 8, 10], i, 3, 11), s.test_bisect([0, 2, 4, 6, 8, 10], i, 0, 6))
    # print(s.minOperations([2, 11, 10, 1, 3], 10))
    # print(s.countPairsOfConnectableServers([[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], 1))
    # print(s.countPairsOfConnectableServers([[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]], 3))
    # print(s.countPairsOfConnectableServers([[1, 0, 1], [2, 1, 1], [3, 2, 4], [4, 0, 3], [5, 4, 1], [6, 5, 3]], 2))
    # print(s.maximumValueSum([1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))
    # print(s.maximumValueSum([7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
    # print(s.resultArray([2, 1, 3, 3]))
    # print(s.resultArray([5, 14, 3, 1, 2]))
    # print(s.resultArray([2, 38, 2]))
    # print(s.resultArray([3, 3, 3, 3]))
    # print(s.frogPosition(9, [[2, 1], [3, 2], [4, 3], [5, 3], [6, 5], [7, 3], [8, 4], [9, 5]], 9, 1))
    # print(s.countSubgraphsForEachDiameter(n=4, edges=[[1, 2], [2, 3], [2, 4]]))
    # print(s.shortestSubstrings(["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"]))
    # print(s.minimumChanges(
    #     "cccbabacaaaaababccacaaabacbbaccbbccacbcaaaaccccabaababbaaabaaabbbcacaababaaabbbbbaaabacaabacabbccabbaccccbbbccbaacbacabbacbacbbbbacacbacabacbbccaaccccbcbbcccabbaaabaccccbacccccabbccacbbccbabbaccbcaaab",
    #     54))
    # print(s.minimumChanges("abacc", 2))
    # print(s.mostFrequentIDs(nums=[2, 3, 2, 1], freq=[3, 2, -3, 1]))
    # print(s.mostFrequentIDs(nums=[5, 5, 3], freq=[2, -2, 1]))
    # print(s.stringIndices(wordsContainer=["abcd", "bcd", "xbcd"], wordsQuery=["cd", "bcd", "xyz"]))
    # print(s.stringIndices(wordsContainer=["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"]))
    # print(bin(30))
    # print(s.minimumSubarrayLength(nums=[2 * 10 ** 9, 2], k=0))
    # print(math.log(2, 2))
    # print(ord('a'), ord('A'))
    # print(s.minimumOperations([[1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1]]))
    # print(s.findAnswer(n=3, edges=[[2, 1, 6]]))
    # print(s.combinationSum3(2, 12))
    # print(s.findOriginalArray([1, 3, 4, 2, 6, 8, 7, 8]))
    # print(s.numDecodings("226"))
    # a = r"[0-9a-f]+"
    # x = '123admyffc79pt'
    # print(re.split(a, x))
    # print(s.distanceTraveled(5, 1))
    # t = SnapshotArray(1)
    # # t.set(0, 5)
    # t.snap()
    # t.snap()
    # t.set(0, 4)
    # t.snap()
    # # t.get(0, 1)
    # t.set(0, 12)
    # # t.get(0, 1)
    # t.snap()
    # print(t.n)
    # print(t.get(0, 3))
    # print(s.canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
    # print(s.canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]))
    # print(s.numberOfStableArrays(1, 1, 2))
    # print(s.numberOfStableArrays(1, 2, 1))
    # print(s.numberOfStableArrays(3, 3, 2))
    # print(s.numberOfStableArrays(19, 15, 15))
    # print(s.minimumAddedInteger(nums1=[4, 20, 16, 12, 8], nums2=[14, 18, 10]))
    # print(s.minimumAddedInteger(nums1=[3, 5, 5, 3], nums2=[7, 7]))
    # print(s.minimumAddedInteger([9, 9, 1, 1, 1], [5, 5, 5]))
    # print(s.minEnd(3, 19))
    # print(s.minEnd(4, 19))
    # print(s.minEnd(5, 19))
    # print(s.minEnd(10, 19))
    # print(s.minEnd(3, 2))
    # print(s.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    # print(s.wateringPlants([2, 2, 3, 3], 5))
    # print(s.distributeCandies(3, 3))
    # print(s.countDays(10, [[5, 7], [1, 3], [9, 10]]))
    # print(s.clearDigits("cab34"))
    # print(s.findWinningPlayer([4, 18, 17, 20, 15, 12, 8, 5], 1))
    # print(s.findWinningPlayer([16, 4, 7, 17], 1000324))
    # print(s.findWinningPlayer([4, 2, 6, 3, 9], k=2))
    # print(s.findWinningPlayer([2, 5, 4], k=3))
    print(s.maximumLength([1, 2, 3, 4, 5, 1], 0))
    print(s.maximumLength([3, 3, 2], 0))
    print(s.maximumLength([1, 2, 1, 1, 3], 2))
