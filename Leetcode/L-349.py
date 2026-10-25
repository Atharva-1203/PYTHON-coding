class Solution(object):
    def intersection(self, nums1, nums2):
        x1=set(nums1)
        x2=set(nums2)
        l=list(x1.intersection(x2))
        return l
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        