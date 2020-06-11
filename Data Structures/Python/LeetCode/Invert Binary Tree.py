# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree( root ):
    
    if root is None:
        return
    node = root
    invertTree(node.left)
    invertTree(node.right)
    
    node.left, node.right = node.right, node.left
    