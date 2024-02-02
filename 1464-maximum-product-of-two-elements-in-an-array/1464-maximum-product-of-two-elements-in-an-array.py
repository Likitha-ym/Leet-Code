class Solution(object):
    def maxProduct(self, nums):
        nums.sort()  # Sort the array in ascending order
        return (nums[-1] - 1) * (nums[-2] - 1)  
