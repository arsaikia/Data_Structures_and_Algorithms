class Solution:
    # DFS - Post-order
    # O(N) Time | O(H) Space
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        leftNodeCount = self.maxDepth(root.left)
        rightNodeCount = self.maxDepth(root.right)

        return 1 + max(leftNodeCount, rightNodeCount)

########################################################

# DFS - Pre-order
# O(N) Time | O(H) Space


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def getNodeCount(node, depth):
            if not node:
                return depth

            left = getNodeCount(node.left, depth + 1)
            right = getNodeCount(node.right, depth + 1)
            return max(left, right)

        return getNodeCount(root, 0)
