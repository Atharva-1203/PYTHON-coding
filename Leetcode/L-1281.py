class Solution(object):
    def subtractProductAndSum(self, n):
        nums = n
        digit_sum = 0
        prod = 1

        while nums > 0:
            r = nums % 10
            digit_sum = digit_sum + r
            prod = prod * r
            nums = nums // 10

        return prod - digit_sum