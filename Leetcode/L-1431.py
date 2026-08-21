class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        i = 0
        max_candies = candies[0]

        while i < len(candies):
            if candies[i] > max_candies:
                max_candies = candies[i]
            i += 1

        ans = [False] * len(candies)

        for j in range(len(candies)):
            if candies[j] + extraCandies >= max_candies:
                ans[j] = True

        return ans


        

        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        