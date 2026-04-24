# first approach

import sys
def calculateCost(curr, n, arr, k):
    if curr >= n:
        return 0
    sum = 0
    ans = sys.maxsize
    for i in range(curr, n):
        sum += arr[i]
        tot = sum + (i - curr)
        if tot > k:
            break
        if i != n - 1:
            temp = (k - tot) * (k - tot) + calculateCost(i + 1, n, arr, k)
            ans = min(ans, temp)
        else:
            ans = 0
    return ans
def solveWordWrap(arr, k):
    n = len(arr)
    return calculateCost(0, n, arr, k)
if __name__ == "__main__":
    arr = [3, 2, 2, 5]
    k = 6
    res = solveWordWrap(arr, k)
    print(res)
    
# Another approach - DP (memoization) - O(n^2)

def calculateCost(curr, n, arr, k, memo):
    if curr >= n:
        return 0
    if memo[curr] != -1:
        return memo[curr]
    sumChars = 0
    ans = float('inf')
    for i in range(curr, n):
        sumChars += arr[i]
        total = sumChars + (i - curr)
        if total > k:
            break
        if i != n - 1:
            temp = (k - total) * (k - total) + calculateCost(i + 1, n, arr, k, memo)
            ans = min(ans, temp)
        else:
            ans = 0
    memo[curr] = ans
    return ans
def solveWordWrap(arr, k):
    n = len(arr)
    memo = [-1] * n
    return calculateCost(0, n, arr, k, memo)