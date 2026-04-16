def findMinDiff(arr, m):
    n = len(arr)
    arr.sort()
    minDiff = float('inf')
    for i in range(n - m + 1):
        diff = arr[i + m -1] - arr[i]
        if diff < minDiff:
            minDiff = diff
    return minDiff

if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    m = 7
    print(findMinDiff(arr, m))