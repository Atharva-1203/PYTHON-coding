class Solution(object):
    def reverse(self, x):
        flag = False
        if x < 0:
            x = -x
            flag = True

        rev = 0
        n = x

        while n > 0:
            digit = n % 10
            rev = (rev * 10) + digit
            n //= 10
        if flag:
            rev = -rev
        if rev < -(2**31) or rev > (2**31 - 1):
            return 0

        return rev


        """
        :type x: int
        :rtype: int
        """
        