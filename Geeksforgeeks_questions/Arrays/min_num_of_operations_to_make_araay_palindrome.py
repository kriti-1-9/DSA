def finMinOps(arr, n):
    ans = 0
    i, j = 0, n-1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] > arr[j]:
            j -= 1
            arr[j] += arr[j+1]
            ans += 1
        else:
            i += 1
            arr[i] += arr[i-1]
            ans += 1
    return ans