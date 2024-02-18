class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        expected_sum = n * n * (n * n + 1) // 2  
        
        seen = set()
        repeated_value = None
        
        grid_sum = 0
        for row in grid:
            for num in row:
                if num in seen:
                    repeated_value = num
                else:
                    seen.add(num)
                grid_sum += num
        missing_value = expected_sum - grid_sum + repeated_value
        
        return [repeated_value, missing_value]
