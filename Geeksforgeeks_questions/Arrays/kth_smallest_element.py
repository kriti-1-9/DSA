def kthSmallest(arr, k):
    maxElement = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxElement:
            maxElement = arr[i]
    freq = [0] * (maxElement + 1)
    for i in range(len(arr)):
        freq[arr[i]] += 1
    count = 0
    for i in range(maxElement + 1):
        if freq[i] != 0:
            count += freq[i]
            if count >= k:
                return i
    return -1