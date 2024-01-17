class Solution(object):
    def arrayPairSum(self, nums):
        # Sort the array
        nums.sort()

        # Pair adjacent elements and sum the minimum of each pair
        result_sum = sum(nums[i] for i in range(0, len(nums), 2))

        return result_sum

solution = Solution()

nums1 = [1, 4, 3, 2]
nums2 = [6, 2, 6, 5, 1, 2]

print(solution.arrayPairSum(nums1))  
print(solution.arrayPairSum(nums2)) 
