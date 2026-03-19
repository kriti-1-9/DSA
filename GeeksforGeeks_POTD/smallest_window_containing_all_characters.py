from collections import Counter

class Solution:
    def minWindow(self, s, p):

        if len(p) > len(s):
            return ""

        p_count = Counter(p)
        window = {}

        required = len(p_count)
        formed = 0

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in p_count and window[char] == p_count[char]:
                formed += 1

            while formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                window[s[left]] -= 1

                if s[left] in p_count and window[s[left]] < p_count[s[left]]:
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]