# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], s = -inf, e = inf) -> bool:
        if not root: return True
        if not s < root.val < e: return False
        return self.isValidBST(root.left, s, root.val) and self.isValidBST(root.right, root.val, e)
