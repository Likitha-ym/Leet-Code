import re

class Solution(object):
    def isPalindrome(self, s):
        # Convert to lowercase and remove non-alphanumeric characters
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        # Check if the cleaned string is a palindrome
        return cleaned_s == cleaned_s[::-1]

solution = Solution()

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(solution.isPalindrome(s1))  # Output: True
print(solution.isPalindrome(s2))  # Output: False
print(solution.isPalindrome(s3))  # Output: True
