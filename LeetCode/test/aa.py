# -*- coding: utf-8 -*-
import bisect
import heapq
import math
from collections import defaultdict, Counter
import time
from functools import cache
from itertools import accumulate
from math import isqrt, inf
from typing import List

from _heapq import *
from sortedcontainers import SortedList

from LeetCode.test.wrapper import timeit_log


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

    @timeit_log
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
    print(s.minimumSubarrayLength(nums=[2 * 10 ** 9, 2], k=0))
    # print(math.log(2, 2))
