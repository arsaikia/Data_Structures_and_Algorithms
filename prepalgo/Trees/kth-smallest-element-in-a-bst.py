# Recursive
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

# Iterative
# Here we are traversing the whole list irrespective of k
# O(N) Time
# O(H) Space for stack space; H = Log(N) for a balanced tree


def kthSmallest(self, root, k):
    orderedNodes = []

    def inorder(node):
        curr, stack = root, []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            orderedNodes.append(curr.val)
            curr = curr.right

    inorder(root)
    return orderedNodes[k - 1]
##############################################

# Iterative
# Here we are traversing only k times, so practical time complexity will be better
# O(N) Time
# O(H) Space; H = Log(N) for a balanced tree


def kthSmallest(self, root, k):
    curr, stack = root, []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1

        if k == 0:
            return curr.val

        curr = curr.right
