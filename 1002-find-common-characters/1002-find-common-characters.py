from collections import Counter

class Solution(object):
    def commonChars(self, words):
        if not words:
            return []

        common_counts = Counter(words[0])

        for word in words[1:]:
            word_counts = Counter(word)
            common_counts &= word_counts  
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)

        return result

solution = Solution()

words1 = ["bella", "label", "roller"]
words2 = ["cool", "lock", "cook"]

print(solution.commonChars(words1))  
print(solution.commonChars(words2)) 
