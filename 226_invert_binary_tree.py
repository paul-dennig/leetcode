from TreeNode import TreeNode

def invertTree(root):
    if (root == None):
        return None
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)
        return None

def test():
    input1 = TreeNode()
    print(input1)
    return None

test()
