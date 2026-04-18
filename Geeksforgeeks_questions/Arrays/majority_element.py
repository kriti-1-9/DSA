def majorityElement(arr):
    n = len(arr)
    candidate = -1
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    count = 0
    for num in arr:
        if num == candidate:
            count += 1
    if count > n // 2:
        return candidate
    return -1