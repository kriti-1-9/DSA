class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lastIndex = {}
        start = 0
        res = 0

        for end in range(len(s)):
            if s[end] in lastIndex:
                start = max(start, lastIndex[s[end]] + 1)

            lastIndex[s[end]] = end
            res = max(res, end - start + 1)

        return res