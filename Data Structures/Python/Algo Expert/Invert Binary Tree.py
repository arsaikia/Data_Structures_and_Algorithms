from collections import deque

# Recursive
# O(n) Time | O(n) Space
def invertBinaryTree( node ):
    if node is None: return
    invertBinaryTree(node.left)
    invertBinaryTree(node.right)
    node.left, node.right = node.right, node.left

# Iterative