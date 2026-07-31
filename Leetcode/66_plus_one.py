class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        # traverse from least-significant digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1   # no carry needed
                return digits
            # digit is 9 → becomes 0, carry continues
            digits[i] = 0

        # if we are here, all digits were 9 → e.g. 999 -> 1000
        return [1] + digits