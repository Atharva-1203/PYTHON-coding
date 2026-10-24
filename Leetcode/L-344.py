class Solution(object):
    def reverseString(self, s):
        start=0
        end=len(s)-1
        while start<end:
            temp=s[end]
            s[end]=s[start]
            s[start]=temp
            start+=1
            end-=1
        return s

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        