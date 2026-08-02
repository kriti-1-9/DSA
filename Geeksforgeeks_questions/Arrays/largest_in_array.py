class Solution:
    def largest(self, arr):
        ans = arr[0]
        for i in range(1, len(arr)):
            ans = max(ans, arr[i])
        return ans