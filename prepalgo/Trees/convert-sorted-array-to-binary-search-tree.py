# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N) Time | O(1) Space - not considering return BST else O(N)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildBST(nums, l, r):
            if l > r:
                return None

            m = l + (r - l) // 2   # Overflow protection

            node = TreeNode(nums[m])
            node.left = buildBST(nums, l, m - 1)
            node.right = buildBST(nums, m + 1, r)

            return node

        return buildBST(nums, 0, len(nums) - 1)
