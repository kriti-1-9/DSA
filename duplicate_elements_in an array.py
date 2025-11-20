""" Given an array arr[] of integers of size n, where each element is in the range 1 to n and each element can occur at most twice, find all elements that appear twice in the array.

Examples: 

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur twice in the given array.

Input: arr[] = [3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty """

# [Naive Approach] Using Nested Loop - O(n2) Time and O(1) Space

""" def findDuplicates(arr):
    ans = []

    # traverse each element in the array
    for i in range(len(arr)):
        cnt = 0

        # vheck if element is already added to result
        for it in ans:
            if arr[i] == it:
                cnt += 1
                break

        # if already added, skip checking again
        if cnt:
            continue

        # check if current element appears again 
        # in the rest of the array
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
                break

        # if duplicate found, add to result
        if cnt:
            ans.append(arr[i])

    return ans


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    res = findDuplicates(arr)
    print(*res) """
    
# [Better Approach - 1] Sorting with Consecutive Comparison - O(n × log n) Time and O(1) Space

"""def findDuplicates(arr):
    
    # sort the array so that duplicates are adjacent
    arr.sort()

    ans = []

    # traverse the sorted array and check 
    # for consecutive duplicates
    for i in range(1, len(arr)):

        # If current element is same as previous
        if arr[i] == arr[i - 1]:

            # avoid adding the same duplicate multiple 
            # times
            if not ans or ans[-1] != arr[i]:
                ans.append(arr[i])

    return ans


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    res = findDuplicates(arr)
    print(*res) """

# [Better Approach - 2] Using Frequency Array - O(n) Time and O(n) Space

def findDuplicates(arr):
    
    n = len(arr)
    # frequency array with 1-based indexing
    freq = [0] * (n + 1)  
    ans = []

    # count frequencies using the array
    for num in arr:
        freq[num] += 1

    # collect elements that appear exactly twice
    for i in range(1, n + 1):
        if freq[i] == 2:
            ans.append(i)

    return ans

if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    res = findDuplicates(arr)

    for ele in res:
        print(ele, end=' ')
    print()