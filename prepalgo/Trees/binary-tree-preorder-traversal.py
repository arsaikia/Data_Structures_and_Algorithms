# O(N) Time | O(N) Space
def recursivePreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def recursivePreorder(node):
        if not node:
            return

        result.append(node.val)
        recursivePreorder(node.left)
        recursivePreorder(node.right)

        return node

    recursivePreorder(root)
    return result

# O(N) Time | O(N) Space


def iterativePreorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return

    res = []
    stack = [root]

    while stack:
        currNode = stack.pop()
        if not currNode:
            continue
        res.append(currNode.val)
        stack.extend([currNode.right, currNode.left])
    return res
