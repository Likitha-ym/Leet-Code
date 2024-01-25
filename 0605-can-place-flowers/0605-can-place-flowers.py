class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
      
        i = 0
        length = len(flowerbed)
        planted = 0
        
        while i < length:
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1 
                    planted += 1
                    i += 1 
            i += 1
        
        return planted >= n

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
print(solution.canPlaceFlowers([1,0,0,0,1], 2))  # Output: False
