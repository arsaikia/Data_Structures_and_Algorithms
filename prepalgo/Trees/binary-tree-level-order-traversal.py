class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = collections.deque([[root]])
        res = []

        while q:
            level = q.popleft()
            currQNodes = []
            currLevelNodes = []

            for node in level:
                if node is None:
                    continue
                currQNodes.append(node.left)
                currQNodes.append(node.right)
                currLevelNodes.append(node.val)
            if currQNodes:
                q.append(currQNodes)
            if currLevelNodes:
                res.append(currLevelNodes)
        return res
