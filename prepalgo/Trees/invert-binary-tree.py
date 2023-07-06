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


class Solution:
    # O(N) Time
    # O(H) Space  | Worst case Unbalanced Tree -> O(N)
    #             | Best case Balanced Tree -> O(N/2)
    def invertTreeIterativeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def BFS(root):
            q = collections.deque([root])

            while q:
                node = q.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    q.append(node.left)
                    q.append(node.right)
            return root

        return BFS(root)
