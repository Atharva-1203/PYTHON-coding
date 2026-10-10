class Solution(object):
    def helper(self, x, n):
        if n == 0:
            return 1.0

        temp = self.helper(x, n // 2)
        temp *= temp

        if n % 2 != 0:
            temp *= x

        return temp

    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.helper(x, -n)

        return self.helper(x, n)