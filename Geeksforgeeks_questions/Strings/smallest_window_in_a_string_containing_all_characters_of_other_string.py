# Better Approach: Binary Search 
"""
def isValid(s, p, mid):
    count = [0] * 256
    distinct = 0
    for x in p:
        if count[ord(x)] == 0:
            distinct += 1
        count[ord(x)] += 1
    curr_count = 0
    for i in range(len(s)):
        count[ord(s[i])] -= 1
        if count[ord(s[i])] == 0:
            curr_count += 1
        if i >= mid:
            count[ord(s[i - mid])] += 1
            if count[ord(s[i - mid])] == 1:
                curr_count -= 1
        if i >= mid - 1:
            if curr_count == distinct:
                return True, i - mid + 1
    return False, -1
def minWindow(s, p):
    m = len(s)
    n = len(p)
    if m < n:
        return ""
    minLength = float('inf')
    low, high = n, m
    idx = -1
    while low <= high:
        mid = (low + high) // 2
        valid, start = isValid(s, p, mid)

        if valid:
            if mid < minLength:
                minLength = mid
                idx = start
            high = mid - 1
        else:
            low = mid + 1
    if idx == -1:
        return ""
    return s[idx:idx + minLength]
"""

# Optimal Approach: Sliding Window

def minWindow(s, p):
    len1 = len(s)
    len2 = len(p)
    if len1 < len2:
        return ""
    countP = [0] * 256
    countS = [0] * 256
    for char in p:
        countP[ord(char)] += 1
    start = 0
    start_idx = -1
    min_len = float('inf')
    count = 0
    for j in range(len1):
        countS[ord(s[j])] += 1
        if countP[ord(s[j])] != 0 and countS[ord(s[j])] <= countP[ord(s[j])]:
            count += 1
        if count == len2:
            while countS[ord(s[start])] > countP[ord(s[start])] or countP[ord(s[start])] == 0:
                if countS[ord(s[start])] > countP[ord(s[start])]:
                    countS[ord(s[start])] -= 1
                start += 1
            length = j - start + 1
            if min_len > length:
                min_len = length
                start_idx = start
    if start_idx == -1:
        return "-1"
    return s[start_idx:start_idx + min_len]