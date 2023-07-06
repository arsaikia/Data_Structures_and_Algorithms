class Solution:
    # O(N) Time
    # O(H) Space  | Worst case Unbalanced Tree -> O(N)
    #             | Best case Balanced Tree -> O(N/2)
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def recursivePreorder(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            recursivePreorder(node.left)
            recursivePreorder(node.right)

            return node

        return recursivePreorder(root)
