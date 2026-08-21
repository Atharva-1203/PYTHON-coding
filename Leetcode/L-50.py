class Solution(object):
    def myPow(self, x, n):
        if n<0:
            return 1/self.myPow(x,n*(-1))
        if n==0:
            return 1
        y=self.myPow(x,n//2)
        if n%2==0:
            return y*y
        else:
            return y*y*x
        
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        