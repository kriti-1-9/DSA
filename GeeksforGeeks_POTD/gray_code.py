class Solution:
    def graycode(self,n):
        res = []
        for i in range(1 << n):
            val = i ^ (i >> 1)
            res.append(format(val, f'0{n}b'))
        return res