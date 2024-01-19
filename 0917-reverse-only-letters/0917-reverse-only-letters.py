class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert the string to a list for easy manipulation
        s_list = list(s)
        
        # Initialize pointers for the start and end of the string
        start, end = 0, len(s_list) - 1

        while start < end:
            # Find the next non-letter character from the start
            while start < end and not s_list[start].isalpha():
                start += 1
            
            # Find the next non-letter character from the end
            while start < end and not s_list[end].isalpha():
                end -= 1

            # Swap the positions of the letters found
            s_list[start], s_list[end] = s_list[end], s_list[start]
            
            # Move the pointers
            start += 1
            end -= 1

        # Convert the list back to a string
        return "".join(s_list)

solution = Solution()
print(solution.reverseOnlyLetters("ab-cd"))  # Output: "dc-ba"
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))  # Output: "j-Ih-gfE-dCba"
print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # Output: "Qedo1ct-eeLg=ntse-T!"
