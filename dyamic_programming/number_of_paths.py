""" Given a grid of size m x n, the task is to determine the number of distinct paths from the top-left corner to the bottom-right corner. At each step, one can either move down or right. Given the integers m and n, return the number of unique paths from the top-left corner to the bottom-right corner.

Note: The test cases are designed such that the answer will always fit within a 32-bit integer.

Examples:

Input: m = 3, n = 3
Output: 6
Explanation: Let the given input 3*3 grid is filled as such:
A B C
D E F
G H I
The possible unique paths which exists to reach 'I' from 'A' following above conditions are as follows: ABCFI, ABEHI, ADGHI, ADEFI, ADEHI, ABEFI.
Input: m = 2, n = 3
Output: 3
Explanation: Let the given input 2*3 grid is filled as such:
A B C
D E F
The possible unique paths which exists to reach 'F' from 'A' following above conditions are as follows: ABCF, ADEF and ABEF.
Input: m = 1, n = 4
Output: 1
Explanation: Let the given input 1*4 grid is filled as such:
A B C D 
The only possible unique path is ABCD.
Constraints:
1 ≤ m ≤ 100
1 ≤ n ≤ 100 """

class NumberOfPaths:
    @staticmethod
    def unique_paths(m, n):
        # Create a 2D array to store the number of paths to each cell
        dp = [[0] * n for _ in range(m)]

        # There is only one way to reach any cell in the first row or first column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]