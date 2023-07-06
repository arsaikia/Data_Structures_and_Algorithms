class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getTreeDepth(node):
            if not node:
                return (True, 0)    # (isBalanced, depth)

            leftIsBalanced, leftDepth = getTreeDepth(node.left)
            rightIsBalanced, rightDepth = getTreeDepth(node.right)

            isCurrNodeBalanced = leftIsBalanced and rightIsBalanced and abs(
                leftDepth - rightDepth) < 2
            currDepth = max(leftDepth, rightDepth) + 1

            return (isCurrNodeBalanced, currDepth)

        isRootBalanced, __ = getTreeDepth(root)
        return isRootBalanced
