# O(n) time || O(d) Space -> At one time there are a max of depth(d) frames on the call stack.

def validateBST(tree):
    return validateBST_helper(tree, float('-inf'), float('inf'))


def validateBST_helper(node, minValue, maxValue):
    if node is None:
        return True
    if node.value > maxValue or node.value < minValue:
        return False
    return validateBST_helper(node.left, float('-inf'), node.value) \
        and validateBST_helper(node.right, node.value, float('inf'))
