class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the sentence into words
        words = s.split()

        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words into a string
        result = ' '.join(reversed_words)

        return result

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))  
print(solution.reverseWords("Mr Ding")) 
