class Solution:
    def countBitsFlip(self, a, b):
        return bin(a^b).count('1')