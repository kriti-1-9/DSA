class Solution:
    def largestSwap(self, s):
        s = list(s)
        n = len(s)

        max_idx = n - 1
        left = right = -1

        for i in range(n - 1, -1, -1):

            if s[i] > s[max_idx]:
                max_idx = i

            elif s[i] < s[max_idx]:
                left = i
                right = max_idx

        if left == -1:
            return "".join(s)

        s[left], s[right] = s[right], s[left]

        return "".join(s)