class Solution:
    def isBinaryPalindrome(self, n):
        res = bin(n)[2:]
        st = 0
        end = len(res)-1
        while st < end:
            if res[st] != res[end]:
                return False
            st += 1
            end -=1
        return True