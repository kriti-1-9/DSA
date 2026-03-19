# memoisation

# Stickle the thief wants to loot money from the houses arranged in a line. He cannot loot two consecutive houses and aims to maximize his total loot. Given an array, arr[] where arr[i] represents the amount of money in the i-th house. Determine the maximum amount he can loot.

""" Input: arr[] = [6, 5, 5, 7, 4]
Output: 15 """

"""Input: arr[] = [1, 5, 3]
Output: 5 """

"""Input: arr[] = [4, 4, 4, 4]
Output: 8"""

class solution:
    def maxLoot(self, arr[], dp[]):
        if(idx >= arr.length) return 0
        if(dp[idx] != -1) return dp[idx]
        steal = arr[idx] + maxLoot(arr, idx + 2, dp)
        skip = maxLoot(arr, idx + 1, dp)
        return dp[idx] = max(steal, skip)
    def findMaxSum(arr[]):
        dp = [-1 for i in range(arr.length)]
        return maxLoot(arr, 0, dp)  