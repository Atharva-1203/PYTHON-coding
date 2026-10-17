
class Solution(object):
    def subsets(self, nums):
        result = []
        l = []

        def rec(n):
            if n == len(nums):
                result.append(l[:])
                return

            l.append(nums[n])
            rec(n + 1)

            l.pop()
            rec(n + 1)

        rec(0)
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        
        