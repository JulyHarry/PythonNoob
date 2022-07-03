from typing import List


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split(' ')
        for i in range(len(s)):
            if len(s[i]) > 1 and s[i].startswith('$'):
                try:
                    s[i] = s[i][0] + '%.2f' % (int(s[i][1:]) * (1 - discount * 0.01))
                except:
                    continue
        return ' '.join(s)

    def totalSteps(self, nums: List[int]) -> int:
        # pre = nums[0]
        # record = [0]
        # for i in range(1, len(nums)):
        #     if nums[i] >= pre:
        #         pre = nums[i]
        #         record.append(i)
        # record.append(len(nums))
        # res = 0
        # print(record)
        # for i in range(1, len(record)):
        #     res = max(res, record[i] - record[i - 1] - 1)
        # return res

        pre = nums[0]
        for i in range(1, len(nums)):
            while nums[i] < pre:





s = Solution()
sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
discount = 100
# print(s.discountPrices(sentence, discount))
nums = [5, 3, 2, 1]
print(s.totalSteps(nums))
