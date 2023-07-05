class Solution:
    # O(N) Time | O(N) Space
    def rob(self, root: Optional[TreeNode]) -> int:

        def robHelper(node):
            if not node:
                return [0, 0]  # [withNode, withoutNode]

            left = robHelper(node.left)
            right = robHelper(node.right)

            withNode = node.val + left[1] + right[1]
            withoutNode = max(left) + max(right)
            return [withNode, withoutNode]

        return max(robHelper(root))
