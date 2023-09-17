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
        preorderIdx = 0
        inorderIndex = {value: idx for idx,
                        value in enumerate(inorder)}   # O(N)

        def buildTreeHelper(left, right):
            nonlocal preorderIdx

            if left > right:
                return None

            val = preorder[preorderIdx]
            preorderIdx += 1
            root = TreeNode(val)
            idx = inorderIndex[val]

            root.left = buildTreeHelper(left, idx - 1)
            root.right = buildTreeHelper(idx + 1, right)
            return root

        return buildTreeHelper(0, len(inorder) - 1)


#############################################################
# Let N be the length of the input arrays.

# Time complexity : O(N).

# Building the hashmap takes O(N) time, as there are NNN nodes to add, and adding items to a hashmap has a cost of  O(1), so we get N⋅O(1) = O(N)

# Building the tree also takes O(N) time. The recursive helper method has a cost of  O(1) for each call (it has no loops), and it is called once for each of the NNN nodes, giving a total of O(N).

# Taking both into consideration, the time complexity is O(N).

# Space complexity : O(N).

# Building the hashmap and storing the entire tree each requires O(N) memory.
# The size of the implicit system stack used by recursion calls depends on the height of the tree,
# which is O(N) in the worst case and O(logN) on average.
# Taking both into consideration, the space complexity is O(N).
