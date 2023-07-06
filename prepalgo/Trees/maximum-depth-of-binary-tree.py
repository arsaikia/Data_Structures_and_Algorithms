class Solution:
    # DFS - Post-order
    # O(N) Time | Best - O(N/2), Worst - O(N) Space
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        leftNodeCount = self.maxDepth(root.left)
        rightNodeCount = self.maxDepth(root.right)

        return 1 + max(leftNodeCount, rightNodeCount)
