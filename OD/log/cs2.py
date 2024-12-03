n = int(input())
lu = int(input())
nums = input().split()


def getAns(nums, lu):
    cur, ans = 0, 0
    for x in map(int, nums):
        cur += x
        if x == lu and x < 0:
            cur -= 1
        elif x == lu and x > 0:
            cur += x + 1
        ans = max(ans, cur)
    return ans


if n != len(nums):
    print(12345)
else:
    print(getAns(nums, lu))
