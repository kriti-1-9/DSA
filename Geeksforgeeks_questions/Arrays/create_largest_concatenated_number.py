from functools import cmp_to_key
def myCompare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1
    else:
        return 1
def findLargest(arr):
    numbers = [str(ele) for ele in arr]
    numbers.sort(key=cmp_to_key(myCompare))
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)