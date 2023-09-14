# Here we are traversing the whole list irrespective of k
# O(N) Time
# O(H) Space; H = Log(N) for a balanced tree
def kthSmallest(self, root, k):
    orderedNodes = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        orderedNodes.append(node.val)
        inorder(node.right)

    inorder(root)
    return orderedNodes[k - 1]

##############################################