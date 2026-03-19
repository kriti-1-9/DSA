class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Step 1: XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        
        max_xor = current_xor
        
        # Step 2: Slide window
        for i in range(k, n):
            current_xor ^= arr[i - k]   # remove old
            current_xor ^= arr[i]       # add new
            max_xor = max(max_xor, current_xor)
        
        return max_xor