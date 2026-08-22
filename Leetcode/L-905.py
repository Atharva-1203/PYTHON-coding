class Solution(object):
    def sortArrayByParity(self, nums):
        l_e=[]
        l_o=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                l_e.append(nums[i])
            else:
                l_o.append(nums[i])
            
        l_e.extend(l_o)
        return l_e


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        