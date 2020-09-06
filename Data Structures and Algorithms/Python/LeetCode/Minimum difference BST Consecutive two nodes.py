# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minVal = float('inf')
        node = root
        lastVal = node.val
        return min(self.getVal(node.right, minVal, lastVal), self.getVal(node.left, minVal, lastVal))
        
    def getVal(self, node, minVal, lastVal):
        if node is None:
            return minVal
        
        minVal = min(minVal, abs(node.val-lastVal))
        lastVal = node.val
        
        
        return min(self.getVal(node.right, minVal, lastVal) , self.getVal(node.left, minVal, lastVal))
        
        