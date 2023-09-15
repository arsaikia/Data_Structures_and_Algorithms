# O(N^2) Time | O(N) Space
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    # base case
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])    # O(N)
    root.left = self.buildTree(preorder[1: idx + 1], inorder[: idx])
    root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
    return root

######################################################################

# O(N^2) Time | O(N) Space


def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    def buildTreeHelper(preorder, inorder):
        if not preorder or not inorder:
            return None

        val = preorder.popleft()
        root = TreeNode(val)
        idx = inorder.index(val)    # O(N)
        root.left = buildTreeHelper(preorder, inorder[: idx])
        root.right = buildTreeHelper(preorder, inorder[idx + 1:])
        return root

    dequePreorder = collections.deque(preorder)  # O(N)
    return buildTreeHelper(dequePreorder, inorder)

######################################################################


class Solution:
    # O(N) Time | O(N) Space
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dequePreorder = collections.deque(preorder)  # O(N)
        inorderIndex = {value: idx for idx,
                        value in enumerate(inorder)}   # O(N)

        def buildTreeHelper(left, right):
            if left > right:
                return None

            val = dequePreorder.popleft()
            root = TreeNode(val)
            idx = inorderIndex[val]

            root.left = buildTreeHelper(left, idx - 1)
            root.right = buildTreeHelper(idx + 1, right)
            return root

        return buildTreeHelper(0, len(inorder) - 1)
