# O(N^2) Time | O(H) Space
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

    if not inorder or not postorder:
        return None

    val = postorder.pop()
    root = TreeNode(val)
    idx = inorder.index(val)    # O(N)
    root.right = self.buildTree(inorder[idx + 1:], postorder)
    root.left = self.buildTree(inorder[: idx], postorder)

    return root

############################################################
# O(N) Time | O(H) Space


def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorderIndex = {value: idx for idx,
                    value in enumerate(inorder)}   # O(N)

    def buildTreeHelper(left, right):
        if left > right:
            return None

        root = TreeNode(postorder.pop())
        idx = inorderIndex[root.val]    # O(1)

        # IMPORTANT ! Build the right subtree first
        root.right = buildTreeHelper(idx + 1, right)
        root.left = buildTreeHelper(left, idx - 1)

        return root

    return buildTreeHelper(0, len(inorder) - 1)

############################################################
