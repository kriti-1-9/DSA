# Using LPS of KMP algorithm

"""
def getLPSLength(s):
    n = len(s)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps[n-1]
"""

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
        hash1[0] = (hash1[0] + (ord(s[i]) - \
                ord('a') + 1) * p1) % mod1
        hash1[1] = (hash1[1] + (ord(s[i]) - \
                ord('a') + 1) * p2) % mod2
        hash2[0] = (hash2[0] * base1 + \
                (ord(s[n - i - 1]) - ord('a') + 1)) % mod1
        hash2[1] = (hash2[1] * base2 + \
                (ord(s[n - i - 1]) - ord('a') + 1)) % mod2
        if hash1 == hash2:
            ans = i + 1
        p1 = (p1 * base1) % mod1
        p2 = (p2 * base2) % mod2
    return ans