"""
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
"""

# Efficient - DP
"""
def wildCard(txt, pat):
    n = len(txt)
    m = len(pat)
    prev = [False] * (m + 1)
    for i in range(n + 1):
        curr = [False] * (m + 1)
        if i == 0:
            curr[0] = True
        for j in range(1, m + 1):
            if i == 0:
                curr[j] = ((j > 0 and curr[j - 1]) or j == 0) \
                                        and (pat[j - 1] == '*')
            elif pat[j - 1] == '?' or txt[i - 1] == pat[j - 1]:
                curr[j] = prev[j - 1]
            elif pat[j - 1] == '*':
                curr[j] = prev[j] or curr[j - 1]
        prev = curr
    return prev[m]
"""

# Simple Traversal

"""def wildCard(txt, pat):
    n = len(txt)
    m = len(pat)
    i = 0
    j = 0
    startIndex = -1
    match = 0
    while i < n:
        if j < m and (pat[j] == '?' or pat[j] == txt[i]):
            i += 1
            j += 1
        elif j < m and pat[j] == '*':
            startIndex = j
            match = i
            j += 1
        elif startIndex != -1:
            j = startIndex + 1
            match += 1
            i = match
        else:
            return False
    while j < m and pat[j] == '*':
        j += 1
    return j == m"""
