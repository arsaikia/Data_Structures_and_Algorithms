def iterativeInorderTraversal(tree):
    result = []
    stack = []

    while stack or tree:
        if tree:
            result.append(tree.val)
            stack.append(tree)
            tree = tree.left
        else:
            node = stack.pop()
            tree = node.right

    return result


if __name__ == "__main__":
    from binarytree import bst
    tree = bst(2)
    print(tree)
    print(iterativeInorderTraversal(tree))
