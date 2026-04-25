# using hashing

def findCommon(arr):
    n = len(arr)
    m = len(arr[0])
    cnt = {}
    for i in range(n):
        cnt[arr[i][0]] = cnt.get(arr[i][0], 0) + 1
        for j in range(1, m):
            if arr[i][j] != arr[i][j - 1]:
                cnt[arr[i][j]] = cnt.get(arr[i][j], 0) + 1
    for ele, c in cnt.items():
        if c == n:
            return ele
    return -1

# Expected Approach - using binary search

def findCommon(arr):
    n = len(arr)
    m = len(arr[0])
    ptr = [0] * n
    while True:
        mx = mat[0][ptr[0]]
        for i in range(1, n):
            mx = max(mx, mat[i][ptr[i]])
        allequal = True
        for i in range(n):
            if mat[i][ptr[i]] != mx:
                allequal = False
                break
        if allequal:
            return mx
        for i in range(n):
            if mat[i][ptr[i]] < mx:
                ptr[i] += 1
                if ptr[i] == m:   
                    return -1