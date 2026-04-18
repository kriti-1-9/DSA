def pairInSortedRotated(arr, target):
    n = len(arr)
    i = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    if arr[i] <= arr[i + 1]:
        i += 1
    l = (i + 1) % n
    r = i
    while l != r:
        if arr[l] + arr[r] == target:
            return True
        if arr[l] + arr[r] < target:
            l = (l + 1) % n
        else:
            r = (r - 1 + n) % n
    return False