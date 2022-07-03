from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        pre = 0
        for w in words[0]:
            pre += ord(w) ** 2
        res.append(words[0])
        for i in range(1, len(words)):
            cur = 0
            for w in words[i]:
                cur += ord(w) ** 2
            if cur != pre:
                res.append(words[i])
            pre = cur
        return res

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        s = special
        s.sort()
        res = 0
        res = max(res, s[0] - bottom)
        for i in range(1, len(s)):
            res = max(res, s[i] - s[i - 1] - 1)
        res = max(res, top - s[-1])
        return res

    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        
        for num in nums:
            print(bin(num)[2:])
        return 0


s = Solution()
words = ["abba", "baba", "bbaa", "cd", "cd"]
# print(s.removeAnagrams(words))
bottom = 1
top = 50
special = [12, 24, 38, 48]
# print(s.maxConsecutive(bottom, top, special))
nums = [16, 17, 71, 62, 12, 24, 14]
print(s.largestCombination(nums))

# res = 1 << 22 - 1
# print(res)
