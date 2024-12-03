import heapq
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter
from functools import cache
from itertools import accumulate
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def test_sort(self, nums):
        nums.sort(key=lambda x: (x[0], -x[1]))
        print(nums)

    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])
        profit = 0
        ans = 0
        hp = []
        s = defaultdict(int)
        for x, y in items:
            if k:
                profit += x
                s[y] += 1
                heapq.heappush(hp, (x, y))
                k -= 1
            elif y not in s and s[hp[0][1]] > 1:
                lastx, lasty = heapq.heappop(hp)
                profit += x - lastx
                s[y] += 1
                s[lasty] -= 1
                heapq.heappush(hp, (x, y))
            ans = max(ans, profit + len(s) ** 2)
        return ans

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        for num in nums:
            s2[num] += 1
        m1 = -1
        m2 = -1
        for i in range(n - 1):
            s1[nums[i]] += 1
            s2[nums[i]] -= 1
            if s1[nums[i]] * 2 > i + 1:
                m1 = nums[i]
            for k, v in s2.items():
                if v * 2 > n - i - 1:
                    m2 = v
            if m1 != -1 and m1 == m2:
                return i
        return -1

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        t = Trie()
        for f in forbidden:
            t.insert(f[::-1])
        l = 0
        ans = 0
        for r in range(len(word)):
            while l <= r and t.query(''.join(reversed(word[l:r + 1]))):
                l += 1
            ans = max(ans, r - l + 1)
        return ans

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for h in hours:
            ans += d[(24 - h) % 24]
            d[h % 24] += 1
        return ans

    def maximumTotalDamage(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        dp = {}

        for p in nums:
            # 计算当前咒语的最大值
            max_val = p
            # 检查 p-2, p-1, p+1, p+2 的最大值
            for delta in [-2, -1, 1, 2]:
                if p + delta in dp:
                    max_val = max(max_val, dp[p + delta] + p)
            dp[p] = max_val

        return max(dp.values())

    def longestConsecutive(self, nums: List[int]) -> int:
        p = {}
        c = {}
        for num in nums:
            p[num] = num
            c[num] = 1

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            p[px] = py
            c[py] += c[px]

        def query(x):
            if x + 1 in p:
                union(x, x + 1)
            if x - 1 in p:
                union(x, x - 1)

        for num in nums:
            query(num)

        return max(c.values())

    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            while l < r and nums[l] != 0:
                l += 1
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            while i and x == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = x + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = list(accumulate(nums))
        c = Counter(pre)
        for i, p in enumerate(pre):
            ans += c[p - k]
        return ans

    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        d = Counter()
        l = 0
        res = []
        cnt = len(s)

        def check():
            for i, v in c.items():
                if d[i] < v:
                    return False
            return True

        for r, x in enumerate(s):
            d[x] += 1
            while check():
                if r - l + 1 < cnt:
                    cnt = r - l + 1
                    res = [l, r + 1]
                d[s[l]] -= 1
                l += 1
        if len(res) > 0:
            return s[res[0]: res[1]]
        return []

    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = Counter(p)
        sc = Counter()
        ans = []
        l = 0

        for r, x in enumerate(s):
            sc[x] += 1
            while sc >= pc:
                if sc == pc:
                    ans.append(l)
                sc[s[l]] -= 1
                l += 1
        return ans


class Trie:
    def __init__(self):
        self.ch = [None] * 26
        self.end = [False] * 26

    def insert(self, s):
        cur = self
        for x in s:
            c = ord(x) - ord('a')
            if not cur.ch[c]:
                cur.ch[c] = Trie()
            cur = cur.ch[c]
        cur.end[c] = True

    def query(self, s):
        cur = self
        for x in s:
            c = ord(x) - ord('a')
            if not cur.ch[c]:
                return False
            cur = cur.ch[c]
            if cur.end[c]:
                return True
        return False


s = Solution()
# s.test_sort([[1, 3], [-2, 2], [5, 2], [-6, -1], [-2, -2]])
# print(s.findMaximumElegance([[6, 4], [1, 1], [5, 2], [5, 4]], 3))
# s.minimumIndex([1, 2, 1])
# t = Trie()
# t.insert("abc")
# t.insert("abcd")
# t.insert("eccss")
# print(t.query('abc'))
# print(t.query('abce'))
# print(t.query('eccss'))
# print(t.query('abcd'))
# print(t.query('ab'))
# print(t.query('ecc'))
# print(t.query('ss'))
# print(t.query('as'))
# print(s.maximumTotalDamage([7, 1, 6, 3]))
# print(s.maximumTotalDamage([1, 1, 3, 4]))
# print(s.maximumTotalDamage([7, 1, 6, 6]))
# print(s.maximumTotalDamage([7, 1, 6, 6]))
print(s.findAnagrams(s="cbaebabacd", p="abc"))
