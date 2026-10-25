
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        if n <= 1:
            return

        k %= n

        if k == 0:
            return

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
         