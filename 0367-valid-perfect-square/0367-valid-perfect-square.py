class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_squared = mid * mid
            
            if mid_squared == num:
                return True
            elif mid_squared < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
