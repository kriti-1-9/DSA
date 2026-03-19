class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor = 0
        count = 0
        freq = {0:1}
        
        for num in arr:
            prefix_xor ^= num
            target = prefix_xor ^ k
            if target in freq:
                count += freq[target]
            
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count