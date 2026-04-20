class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        freq = {}
        maxFreq = 0
        res = 0
        l = 0
        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])
            if r-l+1-maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res   