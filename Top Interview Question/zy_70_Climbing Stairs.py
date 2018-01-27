# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+2)
        #也可以这么写
        # dp = [0 for i in xrange(n)]
        dp[1] = 1
        dp[2] = 2

        i = 3 
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i++

        return dp[n] 

    