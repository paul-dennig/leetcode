# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# conditions:
# 1: p or q is root
# 2: one is in p and one is in q
# 3: both ancestors are in p, or both ancestors are in q
# 4: they are in neither

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case 1
        if root == None: return None
        if root.val == p.val or root.val == q.val:
            return root

        # traverse:
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # case 2
        if left and right:
            return root

        # case 3
        if left:
            return left
        return right
