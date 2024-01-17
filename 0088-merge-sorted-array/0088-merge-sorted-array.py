class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Start merging from the end
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

solution = Solution()

nums1_1, m_1, nums2_1, n_1 = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
nums1_2, m_2, nums2_2, n_2 = [1], 1, [], 0
nums1_3, m_3, nums2_3, n_3 = [0], 0, [1], 1

solution.merge(nums1_1, m_1, nums2_1, n_1)
solution.merge(nums1_2, m_2, nums2_2, n_2)
solution.merge(nums1_3, m_3, nums2_3, n_3)

print(nums1_1) 
print(nums1_2) 
print(nums1_3) 
