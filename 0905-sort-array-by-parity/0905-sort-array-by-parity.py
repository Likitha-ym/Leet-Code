class Solution(object):
    def sortArrayByParity(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            # Find odd number from the left
            while left < right and nums[left] % 2 == 0:
                left += 1

            # Find even number from the right
            while left < right and nums[right] % 2 == 1:
                right -= 1

            # Swap the odd and even numbers
            nums[left], nums[right] = nums[right], nums[left]

        return nums

solution = Solution()

nums1 = [3, 1, 2, 4]
nums2 = [0]

print(solution.sortArrayByParity(nums1)) 
print(solution.sortArrayByParity(nums2)) 
