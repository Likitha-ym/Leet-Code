class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        ways_1, ways_2 = 1, 1
        
        for i in range(2, n + 1):
            current_ways = ways_1 + ways_2
            ways_1, ways_2 = ways_2, current_ways
        
        return ways_2
