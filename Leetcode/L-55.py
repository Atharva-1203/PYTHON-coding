class Solution(object):
    def canJump(self, nums):
        maxInd=0
        for i in range(0,len(nums)):
            if(i>maxInd):
                return False
            maxInd=max(maxInd,i+nums[i])
            if(maxInd>=len(nums)):

                return True
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        