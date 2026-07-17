class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        case1 = helper(nums[:-1])  # exclude last
        case2 = helper(nums[1:])   # exclude first

        return max(case1, case2)        