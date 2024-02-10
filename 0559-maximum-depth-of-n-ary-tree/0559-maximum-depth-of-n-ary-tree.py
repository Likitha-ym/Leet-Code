class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        
        return max_depth + 1
