# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-01-08 22:32
"""
from collections import defaultdict
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        num = title.split()
        res = []
        for n in num:
            res.append(str.upper(n[0]) + str.lower(n[1:]) if len(n) > 2 else n)
        return " ".join(res)

    def pairSum(self, head: Optional[ListNode]) -> int:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        res = 0
        for i in range(len(num) // 2):
            res = max(res, num[i] + num[len(num) - i])
        return res

    def longestPalindrome(self, words: List[str]) -> int:
        single = set()
        double = defaultdict(int)
        res = 0
        for word in words:
            if word[0] == word[1]:
                if word in single:
                    single.remove(word)
                    res += 4
                else:
                    single.add(word)
            else:
                if (w := word[::-1]) in double.keys():
                    double[w] -= 1
                    if double[w] == 0:
                        del double[w]
                    res += 4
                else:
                    double[word] += 1
        return res + (2 if single else 0)


s = Solution()
# print(s.capitalizeTitle("capiTalIze tHe titLe"))
words = ["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "of", "qf", "qf", "of"]
print(s.longestPalindrome(words))
