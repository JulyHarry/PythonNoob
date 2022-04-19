# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2022-04-10 13:57
"""
from typing import List


class Solution:
    def uniqueMorseRepresentationsI(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        return len(set("".join(MORSE[ord(w) - ord('a')] for w in word) for word in words))

    def uniqueMorseRepresentationsII(self, words: List[str]) -> int:
        d = set()
        map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for word in words:
            res = ''
            for w in word:
                res += map[ord(w) - ord('a')]
            d.add(res)
        return len(d)
