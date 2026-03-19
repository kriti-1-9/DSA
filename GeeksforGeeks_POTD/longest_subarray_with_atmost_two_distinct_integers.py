class Solution:
    def totalElements(self, arr):
        left = 0
        freq = {}
        max_len = 0
        
        for right in range(len(arr)):
            # Add element
            if arr[right] in freq:
                freq[arr[right]] += 1
            else:
                freq[arr[right]] = 1
            
            # Shrink window if more than 2 distinct
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len