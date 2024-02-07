class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        result = []
        if root.left:
            result.extend(self.postorderTraversal(root.left))
        if root.right:
            result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root))  # Output: [3, 2, 1]
