def maxSubarraySum(arr):
    res = arr[0]
    maxEnding = arr[0]
    
    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    return res

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubarraySum(arr))