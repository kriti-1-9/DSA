def wildCardRec(text, pat, n, m, dp):
    if m == 0:
        return n == 0
    if dp[n][m] != -1:
        return dp[n][m]
    if n == 0:
        for i in range(m):
            if pat[i] != '*':
                dp[n][m] = False
                return False
        dp[n][m] = True
        return True
    if pat[m - 1] == text[n - 1] or pat[m - 1] == '?':
        dp[n][m] = wildCardRec(text, pat, n-1, m-1, dp)
        return dp[n][m]
    if pat[m - 1] == '*':
        dp[n][m] = wildCardRec(text, pat, n-1, m, dp) or wildCardRec(text, pat, m-1, n, dp)
        return dp[n][m]
    dp[n][m] = False
    return False

def wildCard(txt, pat):
    n = len(txt)
    m = len(pat)
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    return wildCardRec(txt, pat, n, m, dp)   