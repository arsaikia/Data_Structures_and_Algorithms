# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        node = root
        runningSum = 0
        array = []
        self.findBranchSums(node,runningSum, array)
        return sum in array
    
    def findBranchSums(self, node, runningSum, array):
        if node is None:
            return
        runningSum += node.val
        if node.left is None and node.right is None:
            return array.append(runningSum)
        self.findBranchSums(node.left, runningSum, array)
        self.findBranchSums(node.right, runningSum, array)
        