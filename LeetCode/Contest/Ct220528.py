from collections import Counter
from typing import List


class Solution:
    def digitCount(self, num: str) -> bool:
        d = Counter()
        for n in num:
            d[int(n)] += 1
        print(d)
        for i, n in enumerate(num):
            if d[i] != int(n):
                return False
        return True

    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        m = [0] * len(messages)
        for i in range(len(messages)):
            m[i] = len(messages[i].split(' '))
        a = max(m)
        print(a)
        res = []
        for i in range(len(m)):
            if m[i] == a:
                res.append(senders[i])
        print(res)
        return sorted(res, reverse=True)[0]


s = Solution()
# print(s.digitCount('1210'))
messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]
senders = ["Alice", "userTwo", "userThree", "Alice"]
print(s.largestWordCount(messages, senders))
