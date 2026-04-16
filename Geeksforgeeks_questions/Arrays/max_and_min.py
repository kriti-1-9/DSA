# Naive Approach

"""
def findMinMax(arr):
    
    # Sort array
    sorted_arr = sorted(arr)
    return [sorted_arr[0], sorted_arr[-1]] 

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = findMinMax(arr)
    print("%d %d" % (result[0], result[1]))
"""
    
# Better Approach 1

"""
def findMinMax(arr):
    mini = float('inf') 
    maxi = float('-inf')
    
    # Find minimum and maximum
    for num in arr: 
        if num < mini:
            mini = num
        if num > maxi:
            maxi = num
    
    return [mini, maxi]

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = findMinMax(arr)
    print(result[0], result[1])
"""

# Better Approach 2

"""
def get_min_max(arr, low, high):
    result = [0, 0]
    
    # Base case: single element
    if low == high:
        result[0] = arr[low]
        result[1] = arr[low]
        return result
    
    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            result[0] = arr[low]
            result[1] = arr[high]
        else:
            result[0] = arr[high]
            result[1] = arr[low]
        return result
    
    mid = (low + high) // 2
    
    # Recurse on left half
    left = get_min_max(arr, low, mid) 
    
    # Recurse on right half
    right = get_min_max(arr, mid + 1, high)  
    
    # Combine min
    result[0] = min(left[0], right[0])  
    
    # Combine max
    result[1] = max(left[1], right[1])  
    
    return result

def find_min_max(arr):
    return get_min_max(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = find_min_max(arr)
    print("%d %d" % (result[0], result[1]))
"""