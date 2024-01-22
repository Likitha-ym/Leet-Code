class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        min_cost = [0] * n
        
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        
        for i in range(2, n):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        
        return min(min_cost[-1], min_cost[-2])
