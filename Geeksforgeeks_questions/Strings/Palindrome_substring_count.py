def countPS(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            res += 1

    for i in range(2, n):
        for j in range(n - i):
            if s[j] == s[j + i] and dp[i - 1][j + 1]:
                dp[i][j] = True
                res += 1
    return res