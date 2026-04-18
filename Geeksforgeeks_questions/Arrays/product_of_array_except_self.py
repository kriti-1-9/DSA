# O(n) TC and O(1) SC

"""
def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    # Construct the prefProduct array
    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]

    # Construct the suffProduct array
    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]

    # Construct the result array using
    # prefProduct[] and suffProduct[]
    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res
"""

# Efficient approach: O(n) TC and O(1) SC

"""def productExceptSelf(arr):
    zeros = 0
    idx = -1
    prod = 1

    # Count zeros and track the index of the zero
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= arr[i]

    res = [0] * len(arr)

    # If no zeros, calculate the product for all elements
    if zeros == 0:
        for i in range(len(arr)):
            res[i] = prod // arr[i]
    # If one zero, set product only at the zero's index
    elif zeros == 1:
        res[idx] = prod

    return res
"""