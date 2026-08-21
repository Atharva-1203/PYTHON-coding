class Solution(object):
    def tribonacci(self, n):
        a = 0
        b = 1
        c = 1

        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c

        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
        """
        :type n: int
        :rtype: int
        """
        