class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0

solution = Solution()

nums1 = [2, 1, 2]
nums2 = [1, 2, 1, 10]

print(solution.largestPerimeter(nums1)) 
print(solution.largestPerimeter(nums2))  
