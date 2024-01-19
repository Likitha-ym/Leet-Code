class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sort the array
        nums.sort()
        
        # Iterate over the sorted array and check for equal adjacent elements
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:
                return False
        
        return True

solution = Solution()
print(solution.divideArray([3,2,3,2,2,2]))
# Output: True

print(solution.divideArray([1,2,3,4]))
# Output: False
