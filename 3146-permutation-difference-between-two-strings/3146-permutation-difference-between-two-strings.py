class Solution(object):
    def findPermutationDifference(self, s, t):
        if len(s)!=len(t):
            raise ValueError("String must be of the same length")
            
        score=0
        for i in s:
            index_s=s.index(i)
            index_t=t.index(i)
            score+=abs(index_s-index_t)
        return score
        
        
s="abc"
t="bac"
solution=Solution()        
result=solution.findPermutationDifference(s,t)
print(result)
        