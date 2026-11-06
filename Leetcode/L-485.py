class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr_count=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_count+=1
                ans=max(curr_count,ans)
            else:
                curr_count=0
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        