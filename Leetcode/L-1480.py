class Solution(object):
    def runningSum(self, nums):
        ans=[]
        i=0
        sum=0
        while (i<len(nums)):
            sum=sum+nums[i]
            ans.append(sum)
            i=i+1

        return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        