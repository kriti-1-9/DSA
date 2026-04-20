class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = n   # all single characters

        # length = 1
        for i in range(n):
            dp[i][i] = True

        # length = 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        # length >= 3
        for length in range(2, n):
            for start in range(n - length):
                end = start + length
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    res += 1

        return res