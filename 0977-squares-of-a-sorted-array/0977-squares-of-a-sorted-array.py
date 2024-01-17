class Solution(object):
    def sortedSquares(self, nums):
        squared_nums = [num ** 2 for num in nums]
        squared_nums.sort()
        return squared_nums

solution = Solution()

nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

print(solution.sortedSquares(nums1)) 
print(solution.sortedSquares(nums2)) 
