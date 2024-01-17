class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the sets
        result_set = set1.intersection(set2)
        
        # Convert the result set to a list
        result_list = list(result_set)
        
        return result_list

solution = Solution()

nums1_1, nums2_1 = [1, 2, 2, 1], [2, 2]
nums1_2, nums2_2 = [4, 9, 5], [9, 4, 9, 8, 4]

print(solution.intersection(nums1_1, nums2_1))  
print(solution.intersection(nums1_2, nums2_2))
