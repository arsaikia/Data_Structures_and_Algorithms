from collections import deque


# Recursive
# O(n) Time | O(logn) Space
def invertBinaryTree(node):
    if node is None:
        return
    invertBinaryTree(node.left)
    invertBinaryTree(node.right)
    node.left, node.right = node.right, node.left


# Iterative
# O(n) Time | O(n) Space
def invertTree(root):
    dq = deque([root])
    while len(dq):
        node = dq.popleft()
        if node is None:
            continue

        node.left, node.right = node.right, node.left
        dq.append(node.left)
        dq.append(node.right)
