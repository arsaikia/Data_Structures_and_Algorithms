


# Average: O(log N ) Time || O(1) Space
# Worst  : O(N) Time || O(1) Space
def findClosestBST( tree, target ):
    closest = float('inf')
    if abs(tree.value-target) < abs(closest-target):
        closest = tree.value
    if target < tree.left.value:
        findClosestBST(tree.left, target)
    elif target > tree.right:
        findClosestBST(tree.right, target)
    else:
        return closest