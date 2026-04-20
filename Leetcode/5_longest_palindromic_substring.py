class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        start, maxLen = 0, 1

        for i in range(n):
            low, high = i, i
            while low >= 0 and high < n and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

            low, high = i, i + 1
            while low >= 0 and high < n and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

        return s[start:start + maxLen]