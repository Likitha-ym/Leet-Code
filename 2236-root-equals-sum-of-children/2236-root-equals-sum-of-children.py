class Solution(object):
    def checkTree(self, root):
        if root is None or (root.left is None and root.right is None):
            return True
        
        return root.val == (root.left.val + root.right.val)
