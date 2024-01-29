class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Base case: If the root is None, return None
        if root is None:
            return None
        
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursive call on left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
