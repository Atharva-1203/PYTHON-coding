class Solution(object):
    def minCostClimbingStairs(self, cost):

        arr=[-1]*(len(cost)+1)
        def dp(i):
            if i==0:
                return cost[0]
            if i==1:
                return cost[1]
            if arr[i]!=-1:
                return arr[i]
            

            step_1=cost[i-1]+dp(i-1)
            step_2=cost[i-2]+dp(i-2)
            fin=min(step_1,step_2)
            arr[i]=fin
            return fin
        return dp(len(cost)-1)


        """
        :type cost: List[int]
        :rtype: int
        """
        