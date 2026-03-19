class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
    
        prefix = 0
        max_len = 0
        hashmap = {}
    
        for i in range(n):
            prefix += (a1[i] - a2[i])
        
        # If prefix becomes 0 → whole span from 0 to i
            if prefix == 0:
                max_len = i + 1
        
        # If prefix seen before → subarray between indices
            if prefix in hashmap:
                max_len = max(max_len, i - hashmap[prefix])
            else:
                hashmap[prefix] = i
    
        return max_len