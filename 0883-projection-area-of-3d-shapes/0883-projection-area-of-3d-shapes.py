class Solution(object):
    def projectionArea(self, grid):
        xy_area = 0
        yz_area = 0
        zx_area = 0
        
        for i in range(len(grid)):
            max_zx = 0 
            max_yz = 0  
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    xy_area += 1  
                max_zx = max(max_zx, grid[i][j])  
                max_yz = max(max_yz, grid[j][i]) 
            zx_area += max_zx 
            yz_area += max_yz 
        
        return xy_area + yz_area + zx_area
