# Average: O(log N) Time || O(log N) Space
# Worst  : O(N) Time || O(N) Space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self, node):
        curr = node
        if curr is None:
            return
        print(curr.val)
        self.printTree(curr.left)
        self.printTree(curr.right)


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = float('inf')
        node = root
        return self.closestValueInBST(node, target, closest)

    def closestValueInBST(self, node, target, closest):
        if node is None:
            return closest

        if (abs(closest-target)) > (abs(node.val-target)):
            closest = node.val

        if target < node.val:
            return self.closestValueInBST(node.left, target, closest)
        elif target > node.val:
            return self.closestValueInBST(node.right, target, closest)
        else:
            return closest


if __name__ == "__main__":
    Tree = TreeNode(20)
    Tree.left = TreeNode(10)
    Tree.right = TreeNode(30)

    Tree.printTree(Tree)
