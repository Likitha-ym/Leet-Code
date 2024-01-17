class Solution(object):
    def maximumProduct(self, nums):
        # Sort the array
        nums.sort()

        # Calculate two potential maximum products
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        max_product2 = nums[0] * nums[1] * nums[-1]

        # Return the maximum of the two potential maximum products
        return max(max_product1, max_product2)

solution = Solution()

nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4]
nums3 = [-1, -2, -3]

print(solution.maximumProduct(nums1)) 
print(solution.maximumProduct(nums2))  
print(solution.maximumProduct(nums3))  
