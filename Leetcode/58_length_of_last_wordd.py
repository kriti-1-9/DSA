class Solution(object):
    def lengthOfLastWord(self, s):
        lst = [i for i in s.split()]
        return len(lst[-1])        