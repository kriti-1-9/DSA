class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = 0
        res = 0
        hint = [0] * n

        for i in range(n):

            if i >= k:
                flip ^= hint[i-k]

            if arr[i] ^ flip == 0:
    
                if i + k > n:
                    return -1

                res += 1
                flip ^= 1
                hint[i] = 1

        return res