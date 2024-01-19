class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome_range(i, j):
            # Helper function to check if substring s[i:j+1] is a palindrome
            return all(s[k] == s[j - k + i] for k in range(i, j))

        # Iterate through the string
        for i in range(len(s) // 2):
            # Check if characters at symmetric positions are equal
            if s[i] != s[~i]:
                # If not equal, check if removing either character makes the rest a palindrome
                j = len(s) - 1 - i
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)

        # If no mismatch is found, the string is a valid palindrome
        return True

solution = Solution()
print(solution.validPalindrome("aba"))  # Output: True
print(solution.validPalindrome("abca"))  # Output: True
print(solution.validPalindrome("abc"))  # Output: False
