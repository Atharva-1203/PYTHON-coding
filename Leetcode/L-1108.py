class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")
        """
        :type address: str
        :rtype: str
        """
        