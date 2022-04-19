# -*- coding: utf-8 -*- 
"""
Description:  LC00318 - 最大单词长度乘积
URL:          https://leetcode-cn.com/problems/maximum-product-of-word-lengths/
Creator:      HarryUp
Create time:  2021-11-17 12:18:34
Content:
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为
# 每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2: 
# 
#  
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。 
# 
#  示例 3: 
# 
#  
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] 仅包含小写字母 
#  
#  Related Topics 位运算 数组 字符串 👍 240 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from functools import reduce
from itertools import product


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = [reduce(lambda x, y: x | 1 << (ord(y) - ord('a')), word, 0) for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in zip(masks, words) if x[0] & y[0] == 0),
                   default=0)


# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
words = ["ab", "aa", 'cd']
print(s.maxProduct(words))
