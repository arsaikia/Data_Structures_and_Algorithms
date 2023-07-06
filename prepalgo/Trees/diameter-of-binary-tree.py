class Solution:
    # O(N) Time | O(N) Space
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def getTreeDiameter(node):
            if not node:
                return (0, 0)  # (runningCount, maxSoFar)

            leftRunningCount, leftMax = getTreeDiameter(node.left)
            rightRunningCount, rightMax = getTreeDiameter(node.right)

            currRunningCount = 1 + max(leftRunningCount, rightRunningCount)
            currMax = max(leftMax, rightMax, 1 +
                          leftRunningCount + rightRunningCount)
            return (currRunningCount, currMax)

        __, maxNodeCount = getTreeDiameter(root)
        return maxNodeCount - 1
