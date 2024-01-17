class Solution(object):
    def sortSentence(self, s):
        # Split the sentence into words
        words = s.split()
        
        # Sort the words based on the appended numbers
        sorted_words = sorted(words, key=lambda word: int(word[-1]))
        
        # Remove the numbers and join the words to reconstruct the original sentence
        original_sentence = ' '.join(word[:-1] for word in sorted_words)
        
        return original_sentence

# Example usage:
solution = Solution()

s1 = "is2 sentence4 This1 a3"
s2 = "Myself2 Me1 I4 and3"

print(solution.sortSentence(s1))  
print(solution.sortSentence(s2))  
