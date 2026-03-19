class Solution:
	def pushZerosToEnd(self, arr):
        insert_pos = 0
    
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[insert_pos] = arr[insert_pos], arr[i]
                insert_pos += 1