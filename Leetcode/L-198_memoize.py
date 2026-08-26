class Solution(object):
    def rec(self, nums,i,dp):
        if i<=-1:
            return 0
        if dp[i]!=-1:
            return dp[i]
             
        rob=nums[i]+self.rec(nums,i-2,dp)
        not_rob=self.rec(nums,i-1,dp)
        dp[i]=max(rob,not_rob)
        return max(rob,not_rob)
        return dp[i]


    def rob(self, nums):
        dp=[-1]*(len(nums)+1)

        return self.rec(nums,len(nums)-1,dp)

        

        """
        :type nums: List[int]
        :rtype: int
        """
        