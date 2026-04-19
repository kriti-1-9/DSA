def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            if arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1
    return False