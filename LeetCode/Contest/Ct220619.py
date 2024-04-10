class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(26):
            if chr(ord('z') - i) in s and chr(ord('Z') - i) in s:
                return chr(ord('Z') - i)
        return ""

    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if num & 1 == 1 and k & 1 == 0:
            return -1
        if k == 0 and num % 10 != 0:
            return -1
        if k == 0 and num % 10 == 0:
            return 1
        i = num // 10
        for j in range(i, -1, -1):
            t = num
            res = 0
            while t > 0:
                if j * 10 + k == t:
                    res += 1
                    return res
                elif j * 10 + k < t:
                    res += 1
                    t -= j * 10 + k
                else:
                    break
                j -= 1
        return -1

    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = int(s[i])
        for len in range(1, n):
            for j in range(n - 1, -1, 0):
                i = j - len
                dp[i][j] = max(dp[i][j])


s = Solution()
aa = "aAbB"
# print(s.greatestLetter(aa))
num = 19
k = 3
# print(s.minimumNumbers(num, k))

ss = "1001010"
k = 5
print(s.longestSubsequence(ss, k))
