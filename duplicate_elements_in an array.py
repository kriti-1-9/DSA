""" Given an array arr[] of integers of size n, where each element is in the range 1 to n and each element can occur at most twice, find all elements that appear twice in the array.

Examples: 

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur twice in the given array.

Input: arr[] = [3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty """

def findDuplicates(arr):
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
    print(*res)