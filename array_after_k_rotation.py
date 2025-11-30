"""Given an array arr[] and an integer k, rotate the array in place k times to the right (clockwise). In each rotation, the last element moves to the front, and all other elements shift one position to the right. Modify the array in place, do not return anything.
Input: arr[] = [1, 2, 3, 4, 5, 6], k = 2
Output: [5, 6, 1, 2, 3, 4]
Explanation:
=> We perform 2 right rotations (since k = 2):

After 1st rotation: Last element moves to front → [6, 1, 2, 3, 4, 5]
After 2nd rotation: Again, last element to front → [5, 6, 1, 2, 3, 4]
Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: [2, 3, 4, 5, 1]
Explanation:
=> We rotate the array 4 times to the right:

After 1st rotation: [5, 1, 2, 3, 4]
After 2nd rotation: [4, 5, 1, 2, 3]
After 3rd rotation: [3, 4, 5, 1, 2]
After 4th rotation: [2, 3, 4, 5, 1]
"""

# [Naive Approach] Using Recursion - O(n × k) Time and O(k) Space

