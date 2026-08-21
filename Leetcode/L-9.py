class Solution(object):
    def isPalindrome(self, x):
        num=x
        rev=0
        while num>0:
            r=num%10
            num=num//10
            rev=rev*10+r
        if rev==x:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
        