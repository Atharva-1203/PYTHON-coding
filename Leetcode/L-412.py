class Solution(object):
    def fizzBuzz(self, n):
        i=0
        answer=[]
        while(i<n):
            it=i+1
            if (it%3==0 and it%5==0):
                answer.append("FizzBuzz")
            elif it%3==0:
                answer.append("Fizz")
            elif it%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(it))
            i=i+1
        return answer


        """
        :type n: int
        :rtype: List[str]
        """
        