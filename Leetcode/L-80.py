class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        start=1
        if(n==2):
            return n
        for i in range(2,n):
            if(nums[start-1]!=nums[i]):
                start+=1
                nums[start]=nums[i]
        return start+1
        """
        :type nums: List[int]
        :rtype: int
        """
        