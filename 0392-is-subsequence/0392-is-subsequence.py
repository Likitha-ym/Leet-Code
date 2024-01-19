class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize pointers for s and t
        s_pointer, t_pointer = 0, 0
        
        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If characters match, move the s_pointer
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Move the t_pointer in any case
            t_pointer += 1
        
        # Check if all characters of s are found in order
        return s_pointer == len(s)

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc")) 
print(solution.isSubsequence("axc", "ahbgdc"))  
