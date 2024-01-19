class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize variables
        prev_count, curr_count, result = 0, 1, 0

        # Iterate through the string
        for i in range(1, len(s)):
            # If the current character is equal to the previous character, increment count
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                # Update result based on minimum of previous and current count
                result += min(prev_count, curr_count)
                # Update previous count with current count
                prev_count = curr_count
                # Reset current count to 1 for the new character
                curr_count = 1

        # Add the minimum of previous and current count for the last iteration
        result += min(prev_count, curr_count)

        return result

solution = Solution()
print(solution.countBinarySubstrings("00110011"))  
print(solution.countBinarySubstrings("10101")) 
