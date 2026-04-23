# Naive Approach

"""
def getLPSLength(s):
    res = 0
    n = len(s)
    for length in range(1, n):
        j = n - length
        flag = True
        for k in range(length):
            if s[k] != s[j+k]:
                flag = False
                break
        if flag:
            res = length
    return res
"""

# Using LPS of KMP algorithm

def getLPSLength(s):
    n = length(s)
    lps = [0] * n
    len_ = 0
    i = 1
    while i < n:
        if s[i] == s[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i += 1
    return lps[n - 1]

# double hashing

def getLPSLength(s):
    base1, base2 = 31, 37
    mod1, mod2 = int(1e9 + 7), int(1e9 + 9)
    p1 = p2 = 1
    n = len(s)
    hash1 = [0, 0]
    hash2 = [0, 0]
    ans = 0
    for i in range(n - 1):
        hash1[0] = (hash1[0] + (ord(s[i]) - ord('a') + 1) * p1) % mod1
        hash1[1] = (hash1[1] + (ord(s[i]) - ord('a') + 1) * p2) % mod2
        hash2[0] = (hash2[0] * base1 + (ord(s[n - i - 1]) - ord('a') + 1)) % mod1
        hash2[1] = (hash2[1] * base2 + (ord(s[n - i - 1]) - ord('a') + 1)) % mod2
        if hash1 == hash2:
            ans = i + 1
        p1 = (p1 * base1) % mod1
        p2 = (p2 * base2) % mod2
    return ans