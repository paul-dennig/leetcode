# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maximum = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depthResult = self.maxDepth(root) - 1
        return max(self.maximum, depthResult)

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.maximum = max(self.maximum, left+right)
        return 1 + max(left, right)
