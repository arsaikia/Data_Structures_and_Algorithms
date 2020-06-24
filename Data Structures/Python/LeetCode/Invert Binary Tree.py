# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def invertTree(root):

    if root is None:
        return
    node = root
    invertTree(node.left)
    invertTree(node.right)

    node.left, node.right = node.right, node.left


def invertBst(root):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node is not None:
            swap(node)
            queue.append(node.left)
            queue.append(node.right)


def swap(node):
    node.left, node.right = node.right, node.left
