class Solution(object):
    def rearrangeArray(self, nums):
        pos = 0
        neg = 1

        result = [0] * len(nums)

        for num in nums:
            if num >= 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2

        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        