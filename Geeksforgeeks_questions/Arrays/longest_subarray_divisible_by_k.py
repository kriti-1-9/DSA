def longestSubarrayDivK(arr, k):
    n = len(arr)
    res = 0
    prefIdx = {}
    sum = 0
    for i in range(n):
        sum = (sum + arr[i]) % k
        if sum == 0:
            res = i + 1
        elif sum in prefIdx:
            res = max(res, i - prefIdx[sum])
        else:
            prefIdx[sum] = i
    return res