class Solution(object):
    def findContentChildren(self, g, s):
      
        g.sort()
        s.sort()
        
        content_children = 0
        cookie_index = 0
        
        for greed in g:
            while cookie_index < len(s) and s[cookie_index] < greed:
                cookie_index += 1
            
            if cookie_index < len(s):
                content_children += 1
                cookie_index += 1
        
        return content_children

solution = Solution()
print(solution.findContentChildren([1,2,3], [1,1]))  # Output: 1
print(solution.findContentChildren([1,2], [1,2,3]))  # Output: 2
