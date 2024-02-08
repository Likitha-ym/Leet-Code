class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if not original:
            return None
        if original == target:
            return cloned
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result
        return self.getTargetCopy(original.right, cloned.right, target)
