"""Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.

Examples:

Input: cost[] = [10, 15, 20]
Output: 15 """

# Python program to count number of 
# ways to reach nth stair.

def minCostRecur(i, cost):
    
    # Base case
    if i == 0 or i == 1:
        return cost[i]
    
    return cost[i] + min(minCostRecur(i - 1, cost), 
                         minCostRecur(i - 2, cost))

def minCostClimbingStairs(cost):
    n = len(cost)
    
    if n == 1:
        return cost[0]
    
    # Return minimum of cost to 
    # reach (n-1)th stair and 
    # cost to reach (n-2)th stair
    return min(minCostRecur(n - 1, cost), 
               minCostRecur(n - 2, cost))

if __name__ == "__main__":
    cost = [16, 19, 10, 12, 18]
    print(minCostClimbingStairs(cost))