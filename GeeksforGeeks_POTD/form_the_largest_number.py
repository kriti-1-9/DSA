class Solution:

	def findLargest(self, arr):
        
        # Convert to string
        arr = list(map(str, arr))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come first
            elif a + b < b + a:
                return 1   # b should come first
            else:
                return 0
        
        # Sort using comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Edge case: if largest is "0"
        if arr[0] == "0":
            return "0"
        
        return "".join(arr)