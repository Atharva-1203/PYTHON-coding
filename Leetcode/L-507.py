class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        div_sum = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                div_sum += i

                other = num // i
                if other != i:
                    div_sum += other

            i += 1
        
        return div_sum == num

        """
        :type num: int
        :rtype: bool
        """
        