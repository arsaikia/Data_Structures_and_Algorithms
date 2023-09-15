# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(N) Time | O(H) Space
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []

        while stack:
            curr, isVisited = stack.pop()

            # If node is none, skip
            if not curr:
                continue

            # If we are looking at the node second time, add to result
            if isVisited:
                res.append(curr.val)
                continue

            # If we are looking at the node for the first time, add it again as visited
            # add its right and left children
            stack.append((curr, True))
            stack.append((curr.right, False))
            stack.append((curr.left, False))
        return res
