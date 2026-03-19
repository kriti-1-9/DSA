# memoisation

class solution:
    dp = []
    def fibo(self, n):
        if(n <= 1) return n
        if(dp[n] != -1) return dp[n]
        ans = fibo(n-1) + fibo(n-2)
        dp[n] = ans
        return ans
    
    def nthFibonacci(self, n):
        dp = [-1 for i in range(n+1)]
        return fibo(n)