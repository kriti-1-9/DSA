def countPS(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(2, n):
        for j in range(n - i - 1):
            k = i + j - 1
            if s[j] == s[k]:
                dp[j][k] = dp[j][k - 1] + dp[j + 1][k] + 1
            else:
                dp[j][k] = dp[j][k - 1] + dp[j + 1][k] - dp[j + 1][k - 1]
    return dp[0][n - 1]