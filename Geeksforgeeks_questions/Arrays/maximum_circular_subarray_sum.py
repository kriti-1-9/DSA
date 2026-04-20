# Better Approach O(n) time and O(n) space

"""
def maxCircularSum(arr):
    n = len(arr)
    suffixSum = arr[n - 1]
    maxSuffix = [0] * (n + 1)
    maxSuffix[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffixSum += arr[i]
        maxSuffix[i] = max(maxSuffix[i + 1], suffixSum)

    circularSum = arr[0]

    normalSum = arr[0]

    currSum = 0
    prefix = 0

    for i in range(n):
        
        currSum = max(currSum + arr[i], arr[i])
        normalSum = max(normalSum, currSum)
        
        prefix += arr[i]
        circularSum = max(circularSum, prefix + maxSuffix[i + 1])

    return max(circularSum, normalSum)
"""

# Expected Approach O(n) time and O(1) space

"""def maxCircularSum(arr):
    
    totalSum = 0    
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
    
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum) 
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        totalSum += arr[i]
    
    normalSum = maxSum
    circularSum = totalSum - minSum
    if minSum == totalSum:
        return normalSum
    
    return max(normalSum, circularSum)"""