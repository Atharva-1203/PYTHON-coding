class Solution(object):
    def rec(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n] = self.rec(n - 1, dp) + self.rec(n - 2, dp)
        return dp[n]

    def fib(self, n):
        dp=[-1]*(n+1)

        return self.rec(n,dp)
        """
        :type n: int
        :rtype: int
        """
        