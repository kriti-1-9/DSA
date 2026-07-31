class Solution(object):
    def groupAnagrams(self, arr):
        mp = {}

        for word in arr:
            freq = [0]*26
            for ch in word:
                freq[ord(ch)-ord('a')] += 1

            key = tuple(freq)

            if key not in mp:
                mp[key] = []

            mp[key].append(word)

        return list(mp.values())