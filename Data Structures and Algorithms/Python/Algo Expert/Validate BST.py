# O(n) time || O(d) Space -> At one time there are a max of depth(d) frames on the call stack.
def validateBST(tree):
    return getValidatedBST(tree, float("-inf"), float("inf"))

def getValidatedBST(node, minValue, maxValue):
    if node is None:
        return True
    if node.value > maxValue or node.value < minValue:
        return False
    return getValidatedBST(node.left, minValue, node.value) and getValidatedBST(node.right, node.value, maxValue)
        