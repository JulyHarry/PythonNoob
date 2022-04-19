# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-09 10:28
"""


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.record = set()

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            self.record.add(ch)
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
            for r in self.record:
                node.record.add(r)
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word[:-1]:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return False
            node = node.children[ch]
        if word[-1] not in node.record:
            return True
        return False


class Solution:
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        newnums = nums * 2
        total = sum(nums)
        cur = 0
        max = cur
        for i in range(total):
            cur += nums[i]
        for i in range(total, n * 2):
            cur += newnums[i] - newnums[i - total]
            if max < cur:
                max = cur
        return total - max

    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        dict = set()
        res = 0
        t = Trie()
        for startWord in startWords:
            hash = [0] * 26
            for ch in startWord:
                hash[ord(ch) - ord('a')] = 1
            dict.add("".join(str(h) for h in hash))
            t.insert(startWord)
        for targetWord in targetWords:
            hash = [0] * 26
            for ch in targetWord:
                hash[ord(ch) - ord('a')] = 1
            t_hash = "".join(str(h) for h in hash)
            if t_hash in dict:
                res += 1
            else:
                if t.search(targetWord):
                    res += 1
        return res


s = Solution()
nums = [1, 1, 0, 1, 0]
# print(s.minSwaps(nums))
startWords = ["ant", "act", "tack"]
targetWords = ["acta", "actb"]
print(s.wordCount(startWords, targetWords))
