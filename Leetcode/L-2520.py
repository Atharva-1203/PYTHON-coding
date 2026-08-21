class Solution(object):
    def countDigits(self, num):
        count=0
        n=num
        while n>0:
            r=n%10
            if num%r==0:
                count=count+1
            n=n//10
        return count
        """
        :type num: int
        :rtype: int
        """
        