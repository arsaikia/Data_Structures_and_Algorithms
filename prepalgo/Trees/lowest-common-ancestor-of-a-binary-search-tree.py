class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            left, right, curr = p.val, q.val, root.val
            if left < curr and right < curr:
                root = root.left
            elif left > curr and right > curr:
                root = root.right
            else:
                return root
