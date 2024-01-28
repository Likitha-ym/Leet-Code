class Solution(object):
    def findRelativeRanks(self, score):
        index_dict = {score[i]: i for i in range(len(score))}
        
        sorted_scores = sorted(score, reverse=True)
        
        result = [0] * len(score)
        
        for i in range(len(sorted_scores)):
            if i == 0:
                result[index_dict[sorted_scores[i]]] = "Gold Medal"
            elif i == 1:
                result[index_dict[sorted_scores[i]]] = "Silver Medal"
            elif i == 2:
                result[index_dict[sorted_scores[i]]] = "Bronze Medal"
            else:
                result[index_dict[sorted_scores[i]]] = str(i + 1)
        
        return result

solution = Solution()
result_example1 = solution.findRelativeRanks([5, 4, 3, 2, 1])
print(result_example1)  # Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

result_example2 = solution.findRelativeRanks([10, 3, 8, 9, 4])
print(result_example2)  # Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
