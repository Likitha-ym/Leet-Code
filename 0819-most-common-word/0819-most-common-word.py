import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\b\w+\b', paragraph.lower())
        
        word_count = Counter(words)
        
        for banned_word in banned:
            del word_count[banned_word]
        
        return max(word_count, key=word_count.get)

solution = Solution()

paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned1 = ["hit"]

paragraph2 = "a."
banned2 = []

print(solution.mostCommonWord(paragraph1, banned1))  
print(solution.mostCommonWord(paragraph2, banned2))  
