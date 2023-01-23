from TreeNode import TreeNode

def lowestCommonAncestor(root, p, q):
    if (p.val == root.val or q.val == root.val):
        return root
    if ((p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val)):
        return root
    if (p.val < root.val and q.val < root.val):
        return lowestCommonAncestor(root.left, p, q)
    if (p.val > root.val and q.val > root.val):
        return lowestCommonAncestor(root.right, p, q)

def test():
    six = TreeNode(6, None, None)
    two = TreeNode(2, None, None)
    eight = TreeNode(8, None, None)
    zero = TreeNode(0, None, None)
    four = TreeNode(4, None, None)
    seven = TreeNode(7, None, None)
    nine = TreeNode(9, None, None)
    three = TreeNode(3, None, None)
    five = TreeNode(5, None, None)
    six.left = two
    six.right = eight
    two.left = zero
    two.right = four
    four.left = three
    four.right = five
    eight.left = seven
    eight.right = nine

    p = TreeNode(2, None, None)
    q = TreeNode(4, None, None)

    res = lowestCommonAncestor(six, p, q)
    print(res.val)

test()
