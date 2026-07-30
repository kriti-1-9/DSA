n = len(arr)
    index = 0

    for bit in range(31, -1, -1):
        if index >= n:
            break

        max_index = index

        for i in range(index, n):
            if (arr[i] & (1 << bit)) and \
               arr[i] > arr[max_index]:
                max_index = i

        if (arr[max_index] & (1 << bit)) == 0:
            continue

        arr[index], arr[max_index] = \
            arr[max_index], arr[index]

        for i in range(n):
            if i != index and \
               (arr[i] & (1 << bit)):
                arr[i] ^= arr[index]

        index += 1

    ans = 0

    for num in arr:
        ans ^= num

    return ans