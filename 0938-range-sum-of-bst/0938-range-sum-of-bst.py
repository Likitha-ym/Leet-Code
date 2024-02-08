class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0
            
            if low <= node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            elif node.val < low:
                return dfs(node.right)
            else:
                return dfs(node.left)
        
        return dfs(root)
