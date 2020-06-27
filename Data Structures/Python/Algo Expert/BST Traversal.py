# O(n) Time || O(n) Space
def inorderTraversal(tree, array):
    if tree is not None:
        inorderTraversal(tree.left, array)
        array.append(tree.value)
        inorderTraversal(tree.right, array)
    return array

# O(n) Time || O(n) Space


def preorderTraversal(tree, array):
    if tree is not None:
        array.append(tree.value)
        preorderTraversal(tree.left, array)
        preorderTraversal(tree.right, array)
    return array

# O(n) Time || O(n) Space


def postorderTraversal(tree, array):
    if tree is not None:
        postorderTraversal(tree.left, array)
        postorderTraversal(tree.right, array)
        array.append(tree.value)
    return array


