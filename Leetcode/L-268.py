class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        sum=(n*(n+1))/2
        s=0
        for i in range(n):
            s=s+nums[i]
        return sum-s

        """
        :type nums: List[int]
        :rtype: int
        """
        