class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer to keep track of the position to swap non-zero elements
        non_zero_index = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero, swap it with the position pointed by non_zero_index
            if nums[i] != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1

solution = Solution()
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1) 

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2) 
