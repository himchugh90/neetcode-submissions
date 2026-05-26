class Solution:
    def climbStairs(self, n: int) -> int:
        m={}
        if n<=2:
            return n
        if n in m:
            return m[n]
        m[1] = 1
        m[2] = 2
        for i in range(3,n+1):
            m[i] = m[i-1] + m[i-2]
        return m[n]
        
        
        # if n<=2:
        #     return n
        # dp=[0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2
        # # memo={}
        # # for i in range(n):
        # # if i in memo:
        # #     return memo[i]
        
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        #     # memo[i] = dp[i]
        # return dp[n]






























        # dp = [0] * (n+1)
        # # dp[0] = 0
        # if n<=2:
        #     return n
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[n] = dp[n-1] + dp[n-2]
        # return dp[n]
        