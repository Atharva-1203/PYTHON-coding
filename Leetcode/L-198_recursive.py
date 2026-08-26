class Solution(object):
    def rec(self, nums,i):
        if i<=-1:
            return 0
        
        rob=nums[i]+self.rec(nums,i-2)
        not_rob=self.rec(nums,i-1)
        return max(rob,not_rob)


    def rob(self, nums):
        dp=[-1]*(len(nums)+1)

        return self.rec(nums,len(nums)-1)

        

        """
        :type nums: List[int]
        :rtype: int
        """
        