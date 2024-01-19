class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        consistent_count = 0
        
        for word in words:
            if all(char in allowed for char in word):
                consistent_count += 1
        
        return consistent_count

solution = Solution()
print(solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))  # Output: 2
print(solution.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))  # Output: 7
print(solution.countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))  # Output: 4
