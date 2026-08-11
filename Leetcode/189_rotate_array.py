class Solution(object):
    def reverse(self, arr, st, end):
        while st < end:
            arr[st], arr[end] = arr[end], arr[st]
            st += 1
            end -= 1
        return arr 

    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        return nums      