class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
    
    # Step 1: Transform array
        prefix = [0] * (n + 1)
    
        for i in range(n):
            val = 1 if arr[i] > k else -1
            prefix[i + 1] = prefix[i] + val
    
    # Step 2: Build decreasing stack
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)
    
    # Step 3: Traverse from right
        max_len = 0
    
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                max_len = max(max_len, j - stack[-1])
                stack.pop()
    
        return max_len