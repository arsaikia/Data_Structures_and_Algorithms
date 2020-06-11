# O(n) time || O(n) Space
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def branchSums(self, root):
        sums = []
        self.calculateBranchSums(root, 0, sums)

    def calculateBranchSums(self, node, runningSum, sums):
        if node is None:
            return

        runningSum += node.value
        if node.left is None and node.right is None:
            return sums.append(runningSum)

        self.calculateBranchSums(node.left, runningSum, sums)
        self.calculateBranchSums(node.right, runningSum, sums)
