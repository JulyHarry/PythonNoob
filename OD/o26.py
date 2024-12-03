# # 输入获取
# arr = list(map(int, input().split()))
#
#
# # 算法入口
# def getResult(arr):
#     n = len(arr)
#
#     # dp[i]表示：第i时刻可得的正向分
#     dp = [0] * n
#     # delay[i]表示：第i时刻被扣除的负向分
#     delay = [0] * n
#     # score[i]表示：第i时刻最终得分
#     score = [0] * n
#
#     dp[0] = arr[0]
#     score[0] = arr[0]
#
#     for i in range(1, n):
#         dp[i] = min(100, dp[i - 1] + arr[i])  # 最多上报100条
#         delay[i] = delay[i - 1] + dp[i - 1]
#         score[i] = dp[i] - delay[i]
#
#         # 达到100条时必须上报，此时完成首次上报，结束循环
#         if dp[i] >= 100:
#             break
#     print(dp, delay, score)
#     print(max(score))


# # 调用算法
# getResult(arr)
from itertools import accumulate

nums = list(map(int, input().split()))
pre = list(accumulate(nums, initial=0))
ans = 0
for i, num in enumerate(nums):
    ans = max(ans, pre(i + 1) - pre[i])
    print(f'$ {i} {num} {pre[i]} {ans}')
print(ans)
"""
1 7 29 34 13 23 17 29 18 2 34 1 8 23 56 23 12 7 17 23 46 57 38
"""
