class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        
        def postorder_helper(node):
            if node:
                if node.children:
                    for child in node.children:
                        postorder_helper(child)
                result.append(node.val)
        
        postorder_helper(root)
        
        return result
