def rotateclockwise(arr, k):
    n = len(arr)
    if n == 0:
        return
    k = k % n
    arr[n - k:] = reversed(arr[n - k:])
    arr[:n - k] = reversed(arr[:n - k])
    arr[:] = reversed(arr)