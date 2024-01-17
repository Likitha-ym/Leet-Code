class Solution(object):
    def arrayRankTransform(self, arr):
        # Create a sorted list of unique elements
        unique_elements = sorted(set(arr))
        
        # Create a dictionary to store the rank of each unique element
        rank_dict = {element: rank + 1 for rank, element in enumerate(unique_elements)}
        
        # Map the ranks to the original array
        ranks = [rank_dict[element] for element in arr]
        
        return ranks


solution = Solution()

arr1 = [40, 10, 20, 30]
arr2 = [100, 100, 100]
arr3 = [37, 12, 28, 9, 100, 56, 80, 5, 12]

print(solution.arrayRankTransform(arr1))  
print(solution.arrayRankTransform(arr2)) 
print(solution.arrayRankTransform(arr3))  
