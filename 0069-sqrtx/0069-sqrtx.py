class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # When the loop ends, 'right' will be the floor value of the square root
        return right
