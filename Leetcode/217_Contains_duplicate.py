class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        st = set()
        for i in range(n):
            if(nums[i] in st):
                return True
            else:
                st.add(nums[i])
        return False