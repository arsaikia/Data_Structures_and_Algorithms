def iterativeInorderTraversal(tree):
    result = []
    stack = []

    while stack or tree:
        if tree:

            stack.append(tree)
            tree = tree.left
        else:
            node = stack.pop()
            result.append(node.val)
            tree = node.right

    return result


if __name__ == "__main__":
    from binarytree import bst
    tree = bst(2)
    print(tree)
    print(iterativeInorderTraversal(tree))
