class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

solution = Solution()
string1 = ["h","e","l","l","o"]
solution.reverseString(string1)
print(string1) 

string2 = ["H","a","n","n","a","h"]
solution.reverseString(string2)
print(string2) 
